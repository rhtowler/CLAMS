
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import dbConnection
import Clamsbase2Functions
from ui.xga import ui_CLAMSProcess
import CLAMShaul
import CLAMScatch
import CLAMSspecimen
import CLAMSlength
import CLAMSSpeciesFix
from PyQt4 import QtSql
from acquisition.serial import SerialMonitor
import messagedlg
import listseldialog,  codendstatusdlg


class CLAMSProcess(QDialog, ui_CLAMSProcess.Ui_clamsProcess):

    def __init__(self, parent=None):
        #  set up the GUI
        super(CLAMSProcess, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # initialize variables
        self.reloadFlag=False
        self.db=parent.db
        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeEvent
        self.settings=parent.settings
        self.workStation=parent.workStation
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.backLogger=parent.backLogger
        self.testing=parent.testing
        self.partitions=[]
        self.activePartition=None
        self.methotFlag=False

        #  setup reoccuring dlgs
        self.message = messagedlg.MessageDlg(self)

        modules=parent.modules

        # get scientist
        query=QtSql.QSqlQuery("SELECT personnel.scientist FROM personnel WHERE personnel.active=1"
                              " ORDER BY personnel.scientist", self.db)
        self.sciList=[]

        # populate scientist list
        while query.next():
            self.sciList.append(query.value(0).toString())
        self.listDialog = listseldialog.ListSelDialog(self.sciList, self)
        self.listDialog.label.setText('Identify yourself, please.')

        #  First get the user's name
        needScientist=True
        while needScientist:
            if self.listDialog.exec_():
                if (self.listDialog.itemList.currentRow() < 0):
                    #  no name selected
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                            "Please select your name, or a suitable substitue if yours" +
                                            " cannot be found.", 'info')
                    self.message.exec_()
                else:
                    needScientist=False
                    self.scientist = self.listDialog.itemList.currentItem().text()
        p=self.scientist.split(' ')
        self.firstName=p[0]
        self.codendstate=codendstatusdlg.CodendStatusDlg(self)
        #  color palettes
        self.blue=QPalette()
        self.blue.setColor(QPalette.ButtonText,QColor(0, 0, 255))
        self.black=QPalette()
        self.black.setColor(QPalette.ButtonText,QColor(0, 0, 0))

        # Play opening sound if workstation 1
        #if self.workStation=='1':
        #    parent.startSound.play()

        #  indicate active processing
        query = QtSql.QSqlQuery("UPDATE workstations SET status='open' WHERE workstation_ID=" + self.workStation)

        # set up button colors
        self.haulBtn.setPalette(self.black)
        self.catchBtn.setPalette(self.black)
        self.lengthBtn.setPalette(self.black)
        self.specBtn.setPalette(self.black)

        # set label box colors to white
        self.haulLabel.palette().setColor(self.haulLabel.backgroundRole(), QColor(255, 255, 255))
        self.errorIcon=QPixmap()
        self.errorIcon.load(self.settings[QString('IconDir')]+"\\error.bmp")

        #  Set up the signals and slots
        self.connect(self.partitionBox, SIGNAL("activated(int)"), self.getPartition)
        self.connect(self.haulBtn, SIGNAL("clicked()"), self.getHaul)
        self.connect(self.catchBtn, SIGNAL("clicked()"), self.getCatch)
        self.connect(self.specBtn, SIGNAL("clicked()"), self.getSpecimen)
        self.connect(self.lengthBtn, SIGNAL("clicked()"), self.getLength)
        self.connect(self.fixSpeciesBtn, SIGNAL("clicked()"), self.goFixSpecies)
        self.connect(self.editCodendStateBtn, SIGNAL("clicked()"), self.editCodendState)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)

        #  set up the window
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.setGeometry((screen.width() - window.width()) / 2,
                         (screen.height() - window.height()) / 2,
                         window.width(), window.height())
        self.setMinimumSize(window.width(), window.height())
        self.setMaximumSize(window.width(), window.height())
        self.windowAnchor = ((screen.height() - window.height()) / 2, window.height())
        self.settings.update({QString("WindowAnchor"):window.y() + window.height()})
        self.haulLabel.setText(self.activeHaul)

        #  Set the visbility of the action buttons based on the actions specified for this station
        self.haulBtn.hide()
        self.catchBtn.hide()
        self.lengthBtn.hide()
        self.specBtn.hide()
        if 'haul' in modules:
            self.haulBtn.show()
        if 'catch' in modules:
            self.catchBtn.show()
        if 'length' in modules:
            self.lengthBtn.show()
        if 'specimen' in modules:
            self.specBtn.show()
        self.haulBtn.setEnabled(True)

        #  enable buttons based on reload
        query = QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE event_id=" + self.activeHaul +
                                " AND ship=" + self.ship + " AND survey=" + self.survey +
                                " AND event_parameter='PartitionWeightType'")
        if query.first():# data exists
            self.reloadFlag = True
            self.catchBtn.setEnabled(True)
            query = QtSql.QSqlQuery('SELECT sample_id FROM samples WHERE event_id=' + self.activeHaul +
                                    ' AND ship=' + self.ship + ' AND survey=' + self.survey)# there weight data
            if query.next():
                self.lengthBtn.setEnabled(True)
                self.specBtn.setEnabled(True)


        #  set up the serial devices attached to this workstation
        self.setupSerialDevices()

        # enable entry of non-codend partition data before trawl codend is on deck
        self.catchBtn.setEnabled(True)

        #  set up the partitions business
        self.setupAllPartitions()


    def setupAllPartitions(self):
        '''
        setupPartitions populates the partition drop down menu with  the appropriate partition options
        '''

        self.partitions=[]
        self.partitionBox.clear()
        #  get the possible partitions for this gear
        query = QtSql.QSqlQuery("SELECT GEAR_PARTITIONS.PARTITION, EVENTS.GEAR FROM GEAR_OPTIONS, GEAR_PARTITIONS, EVENTS WHERE" +
                                " (GEAR_PARTITIONS.PARTITION = GEAR_OPTIONS.PARTITION) and (GEAR_OPTIONS.GEAR = EVENTS.GEAR)" +
                                " and ((EVENTS.SHIP = " + self.ship + " ) AND (EVENTS.SURVEY = " + self.survey + ") AND" +
                                " (EVENTS.EVENT_ID = " + self.activeHaul + ") AND (GEAR_PARTITIONS.PARTITION_TYPE = 'Catch'))" +
                                "  ORDER BY GEAR_PARTITIONS.PARTITION ASC")

        #  loop thru partitions and populate partition dropdown
        while query.next():
            partition = query.value(0).toString()
            #  get the partitions with a valid weight type
            self.partitionBox.addItem(partition)
            self.partitions.append(partition)

        #  check to make sure we found something to process for this event
        if (len(self.partitions) == 0):
            #  no partitions? - must have the wrong event
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                    self.firstName + ", I am unable to find any catch partitions " +\
                    "to process. Did you select the correct event?", 'info')
            self.message.exec_()
            return

        #  set (or unset) the default value in the partition drop down
        if len(self.partitions)>1:
            #  if there is more than one option - clear the current selection to force the user to select a partition
            self.partitionBox.setCurrentIndex(-1)
        else:
            #  if there is only one option, select it
            self.partitionBox.setCurrentIndex(0)
            self.partitionBox.setEnabled(False)
            self.activePartition = self.partitions[0]


    def getPartition(self):
        self.activePartition=self.partitionBox.currentText()
        # bring up codend status dlgs - first check if already entered
        query = QtSql.QSqlQuery("SELECT * FROM event_data WHERE ship = " + self.ship +
                " AND survey = " + self.survey+" and event_id = "+self.activeHaul+" AND partition = '"+
                self.activePartition + "' AND event_parameter = 'CodendStatus'")
        if not query.first():
            # value has not been recorded for this partition - display the dialog
            self.codendstate.exec_()
            codendstatus=self.codendstate.state_value
            query = QtSql.QSqlQuery("INSERT INTO event_data (ship, survey, event_id, partition, event_parameter, parameter_value) VALUES("+self.ship+
                        ","+self.survey+","+self.activeHaul+",'"+self.activePartition+"' ,'CodendStatus','"+codendstatus+"')")


    def setupSerialDevices(self):
        '''
        setupSerialDevices creates an instance of SerialMonitor and configures it accordingly.
        SerialMonitor is the CLAMS serial acquisition class which oversees all serial acquisition.
        It creates monitoring threads for each configured serial device and handles the polling
        and parsing of serial data received from the devices.
        '''

        #  create an instance of the serial monitor
        self.serMonitor=SerialMonitor.SerialMonitor()

        #  query the devices attached to this station
        query=QtSql.QSqlQuery("SELECT MEASUREMENT_SETUP.DEVICE_ID, DEVICES.DEVICE_NAME " +
                                         "FROM MEASUREMENT_SETUP INNER JOIN DEVICES ON " +
                                         "MEASUREMENT_SETUP.DEVICE_ID = DEVICES.DEVICE_ID WHERE " +
                                         "MEASUREMENT_SETUP.WORKSTATION_ID = " +  self.workStation +
                                         " AND MEASUREMENT_SETUP.DEVICE_INTERFACE = 'Serial'" +
                                         " GROUP BY MEASUREMENT_SETUP.DEVICE_ID, DEVICES.DEVICE_NAME")

        #  loop thru the devices querying their parameters and adding them to serial monitor
        while query.next():
            #  query the connection parameters for this device
            deviceID = str(query.value(0).toString())
            deviceName = str(query.value(1).toString())
            query1 = QtSql.QSqlQuery("SELECT DEVICE_PARAMETER, PARAMETER_VALUE FROM device_configuration" +
                                     " WHERE DEVICE_ID = " + deviceID)

            #  loop thru the parameters and stick in a dictionary
            connPar = {}
            while query1.next():
                connPar.update({query1.value(0).toString():query1.value(1).toString()})

            #  extract the parameters
            try:
                #  extract the required parameters
                port = int(connPar[QString('SerialPort')]) - 1
                baud = int(connPar[QString('BaudRate')])
            except:
                QMessageBox.critical(self, "ERROR", "<font size = 14> Incomplete serial configuration" +
                                     "data in 'device_configuration' for device " + deviceName + "." +
                                     " The device will not be enabled.")
                continue

            #  extract the optional parameters
            parseType = str(connPar.get(QString('ParseType'), 'None'))
            parseExp = str(connPar.get(QString('ParseExpression'), ''))
            parseIndex = int(connPar.get(QString('ParseIndex'), 0))
            cmdPrompt = str(connPar.get(QString('CommandPrompt'), ''))
            if (parseType.lower() == 'regex'):
                try:
                    #  the regex parser requires both the expression and the index
                    parseExp = str(connPar[QString('ParseExpression')])
                    parseIndex = int(connPar[QString('ParseIndex')])
                except:
                    QMessageBox.critical(self, "ERROR", "<font size = 14> Incomplete regex configuration" +
                                         "data in 'device_configuration' for device " + deviceName + "." +
                                         " The device will not be enabled.")
                    continue

            #  add the device to the serial monitor
            try:
                self.serMonitor.addDevice(deviceID, port, baud, parseType, parseExp, parseIndex, cmdPrompt)
            except Exception, e:
                print("ERROR ADDING SERIAL DEVICE:" + str(e) + ":" + str(e.parent))

        try:
            #  start the serial monitor
            self.serMonitor.startMonitoring()
        except Exception, e:
            #  report Serial port initialization errors

            #  first get the human readable device names
            devNames = []
            for badDevice in e.devNames:
                query = QtSql.QSqlQuery("SELECT device_name FROM devices" +
                                        " WHERE device_id=" + badDevice)
                query.first()
                devNames.append(str(query.value(0).toString()))

            #  construct the error text
            if (len(devNames) == 1):
                errText = 'Error opening device ' + str(devNames[0])
            else:
                errText = 'Error opening devices ' + ', '.join(devNames)

            #  display a warning dialog
            QMessageBox.warning(self, "Serial Port Error", "<font size = 14>" + errText +
                                ". These devices will be not be enabled.")


    def editCodendState(self):

        query = QtSql.QSqlQuery("SELECT * FROM event_data WHERE ship = "+self.ship+
                        " and survey = "+self.survey+" and event_id = "+self.activeHaul+" and partition = '"+
                        self.activePartition+"' AND event_parameter = 'CodendStatus'")
        if query.first():

            currentCodendState=query.value(0).toString()
            for btn in self.codendstate.btns:
                if btn.text()==currentCodendState:
                    btn.setChecked(True)
            codendstatus=self.codendstate.state_value
            self.codendstate.exec_()
            codendstatus=self.codendstate.state_value
            query = QtSql.QSqlQuery("UPDATE event_data SET parameter_value='"+codendstatus+"' WHERE ship = "+self.ship+
                            " and survey = "+self.survey+" and event_id = "+self.activeHaul+" and partition = '"+
                            self.activePartition+"' AND event_parameter = 'CodendStatus'")

    def getHaul(self):

        #  set the button blue to indicate the active form
        self.haulBtn.setPalette(self.blue)

        #  display the haul selection dialog
        haulWindow = CLAMShaul.CLAMSHaul(self)
        ok = haulWindow.exec_()

# 1/25/22 - RHT - Commented this code out as we have changed how
#                 the partitions combo box is populated. This is
#                 now done in the init. This code here was adding
#                 duplicate entries for Codend.
#
#        #  check if it was completed
#        if ok:
#            #  the form was completed - allow them to move on
#            self.partitionBox.addItem('Codend')
#            self.partitions.append('Codend')
#
#        else:
#            #  the form was not completed - we don't enable the catch button
#            #  since we can't move forward until the haul form is complete
#            pass

        #  set the button back to black
        self.haulBtn.setPalette(self.black)


    def getCatch(self):

        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                                    self.firstName + ", you need to select a partition for" +
                                    " this haul first!", 'info')
            self.message.exec_()
            return


        self.catchBtn.setPalette(self.blue)
        catchWindow = CLAMScatch.CLAMSCatch(self)
        self.lengthBtn.setEnabled(True)
        self.specBtn.setEnabled(True)
        catchWindow.exec_()
        self.catchBtn.setPalette(self.black)


    def getLength(self):
        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                                    self.firstName + ", you need to select a partition for" +
                                    " this haul first!", 'info')
            self.message.exec_()
            return

        self.lengthBtn.setPalette(self.blue)
        lengthWindow = CLAMSlength.CLAMSLength(self)
        lengthWindow.exec_()
        self.lengthBtn.setPalette(self.black)

    def getSpecimen(self):
        #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                                    self.firstName + ", you need to select a partition for" +
                                    " this haul first!", 'info')
            self.message.exec_()
            return
        self.specBtn.setPalette(self.blue)
        specimenWindow = CLAMSspecimen.CLAMSSpecimen(self)
        specimenWindow.exec_()
        self.specBtn.setPalette(self.black)

    def goFixSpecies(self):
                #  make sure there is an active partition
        if (self.activePartition == None):
            #  no partition selected - issue error
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                                    self.firstName + ", you need to select a partition for" +
                                    " this haul first!", 'info')
            self.message.exec_()
            return
        #  display the standard haul selection dialog
        spcFixWindow = CLAMSSpeciesFix.CLAMSSpeciesFix(self)
        if not spcFixWindow.exec_():
            return

    def goExit(self):

        #  called when the fi
        self.close()

    def closeEvent(self, event=None):

        #  set the status for this workstation to closed
        query = QtSql.QSqlQuery("UPDATE workstations SET status='closed' WHERE workstation_ID=" + self.workStation)

        #  check if we're the last station to close - THIS CODE IS PROBLEMATIC
        #  It is possible to close a station, then open it and move to the next
        #  event. As the other stations close, the last one on the previous event
        #  will not know it is the last for that event and this code is never run
        #  for that event. The event ID needs to be added to this check so a station
        #  knows it is the last of a certain event to close.
        query = QtSql.QSqlQuery("SELECT status FROM workstations WHERE status='open'")
        if not query.next():
            self.totalHaulWeight() # populate the total partition weights into the event_data table
            # this is the last station to close - reset the active haul
            query = QtSql.QSqlQuery("UPDATE application_configuration SET parameter_value = 0" +
                                    " WHERE parameter = 'ActiveHaul'")
            if not self.methotFlag and not self.testing:
                #  do some basic checks on the data we just collected to make sure
                #  we didn't miss anything big.
                self.sampleValidation1()

                if self.returnFlag:
                    #  user chose to fix the problem so we don't exit
                    event.ignore()
                    return

        #  update the CATCH_SUMMARY table for this event
        ok, error_txt = self.updateCatchSummary()
        if not ok:
            #  let the user know there was a problem
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], error_txt, 'info')
            self.message.exec_()

        # shut down serial monitor
        try:
            self.serMonitor.stopMonitoring()
        except:
            #  we don't care if we can't close the serial ports becuase
            #  we probably couldn't open them in the first place.
            pass

        event.accept()


    def totalHaulWeight(self):
        basket_weights = []
        for partition in self.partitions:
            query1 = QtSql.QSqlQuery("select parameter_value from event_data where ship = "+self.ship+
                    " and survey = "+self.survey+" and event_id = "+self.activeHaul+" and partition = '"+
                    partition+"' and event_parameter = 'PartitionWeight' ")
            query1.first()
            if query1.value(0) == "TBD":
                sample_sum = []
                total_weight = []
                sample_id = []
                query2 = QtSql.QSqlQuery("select sample_id from samples where ship = "+self.ship+
                        " and survey = "+self.survey+" and event_id = "+self.activeHaul+" and partition = '"+
                        partition+"' and sample_type = 'WholeHaul'")
                query2.first()
                parent_id_qt = query2.value(0).toInt()
                parent_id = parent_id_qt[0]
                query3 = QtSql.QSqlQuery("select sample_id from samples where ship = "+self.ship+
                        " and survey = "+self.survey+" and event_id = "+self.activeHaul+" and parent_sample  = " +
                        str(parent_id) )
                while query3.next():
                    sample_id_qt = query3.value(0).toInt()
                    sample_id.append(sample_id_qt[0])
                for samples in sample_id:
                    query4 = QtSql.QSqlQuery("select weight from baskets where ship = "+self.ship+
                            " and survey = "+self.survey+" and event_id = "+self.activeHaul+
                            " and sample_id ="+str(samples)+ " ")
                    while query4.next():
                        basket_weight = query4.value(0).toFloat()
                        basket_weights.append(basket_weight[0])
                        #print basket_weights#
                    basket_sum = sum(basket_weights)
                    sample_sum.append(basket_sum)
                    basket_weights = []
                    basket_sum = []

                total_weight = sum(sample_sum)
                query5 = QtSql.QSqlQuery("update event_data set parameter_value ="+str(round(total_weight,3))+
                        " where  ship = "+self.ship+" and survey = "+self.survey+" and event_id = "+self.activeHaul+
                        " and partition = '"+partition+"' and event_parameter = 'PartitionWeight' ")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') +
                                                         "," + query5.lastQuery())


    def updateCatchSummary(self):
        '''
        updateCatchSummary updates the catch_summary table with data from this event. Data in catch_summary 
        are generated outside the database and loaded into the table. These data need to be updated
        whenever the underlying data change. This method does this.
        
        This is awkward because new code we have written use our dbConnection library that sorta pythonifies
        the QtSql interface. CLAMS predates dbQuery and uses "raw" QtSql. Because of this, we're going
        to just create a new dbConnection connection to the database.
        '''
               
        event_id = self.activeHaul
        
        #  set the initial return state
        ok = True
        error_msg = ''

#        try:
        #  open a connection to the db using dbConnection
        dbQueryObj = dbConnection.dbConnection(self.parent().dbName, self.parent().dbUser,
                self.parent().dbPassword)
        dbQueryObj.dbOpen()
        
        #  create an instance of clamsbase functions
        clamsFunctions = Clamsbase2Functions.Clamsbase2Functions(dbQueryObj, self.ship,
                self.survey)

        #  delete existing data for this event
        sql = ("DELETE FROM catch_summary WHERE ship=" + self.ship + " AND survey=" + self.survey +
                " AND event_id=" + event_id)
        dbQueryObj.dbExec(sql)

        #  find all the unique species samples
        sql = ("SELECT sample_id, parent_sample, partition, species_code, subcategory FROM samples " +
                "WHERE ship=" + self.ship + " AND survey=" + self.survey + " AND event_id=" + event_id +
                " AND sample_type='Species'")
        sampleQuery = dbQueryObj.dbQuery(sql)
        
        for sample_id, parent_sample, partition, species_code, subcategory in sampleQuery:
            #  call the computeCatchSummary method of clamsFunctions to, er compute the
            #  catch summary data.
            [status, vals]=clamsFunctions.computeCatchSummary(event_id, partition, species_code, subcategory)

            #  check if we successfully computed the summary data
            if status:
                #  since status is OK, discard the empty error strings that can be returned in
                #  vals. vals[0] is a list containing the following data:
                #    vals = [sample id, species code, subcategory, sample id, WeightInHaul,SampledWeight,
                #            NumberInHaul,SampledNumer,FrequencyExpansion,InMix,WholeHauled]
                vals = vals[0]
                
                #  get species name
                sql = ("SELECT scientific_name, common_name FROM species WHERE species_code=" + species_code)
                sppQuery = dbQueryObj.dbQuery(sql)
                sci_name, common_name = sppQuery.first()

                #  then insert results into catch summary table
                sql = ("INSERT INTO catch_summary (ship,survey,event_id,partition,sample_id,parent_sample," +
                        "scientific_name,species_code,common_name,subcategory,weight_in_haul,sampled_weight," +
                        "number_in_haul,sampled_number,frequency_expansion,in_mix,whole_hauled) VALUES(" +
                        self.ship + "," + self.survey + "," + event_id + ",'" + partition + "'," + sample_id + "," +
                        parent_sample + ",'" + sci_name + "'," + species_code + ",'" + common_name +
                        "','" + subcategory + "'," + str(vals[4]) + "," + str(vals[5]) + "," +
                        str(vals[6]) + ","+str(vals[7]) + "," + str(vals[8]) + "," + str(vals[9]) +
                        "," + str(vals[10]) + ")")
                dbQueryObj.dbExec(sql)
            else:
                #  check to make sure there is an actionable error - computeCatchSummary can return false if there
                #  is a sample with no measurements which we silently ignore here as it isn't necessarily an error
                if (len(vals) > 0):
                    error_msg = ("Error computing catch summary data for event " +
                            event_id + ". Error text:" + vals[2]  + vals[1])
                    ok = False
                    break
                        
#        except Exception, e:
#            error_msg = ("Unknown error computing catch summary data for event " +
#                                event_id )
#            ok = False
            
        return (ok, error_msg)


    def sampleValidation1(self):
        '''
        sampleValidation1 performs some basic checks to make sure there aren't any obvious
        errors made during sampling.
        '''
        
        self.returnFlag = False
        #  loop thru the partitions doing common validations on the catch
        for partition in self.partitions:
            # loop though samples in this partition
            query = QtSql.QSqlQuery("SELECT species.common_name, samples.sample_id, samples.species_code, samples.subcategory" +
                                    " FROM species, samples WHERE species.species_code = samples.species_code" +
                                    " AND samples.event_id=" + self.activeHaul + " AND samples.ship=" + self.ship +
                                    " AND samples.survey=" + self.survey + " AND samples.partition='" +
                                    partition + "' and samples.sample_type = 'Species'")


            while query.next():
                species = query.value(0).toString()
                code = query.value(2).toString()
                key = query.value(1).toString()
                subcategory=query.value(3).toString()

                # validation #1 - species samples without weights
                query1 = QtSql.QSqlQuery("SELECT * FROM baskets WHERE sample_id=" + key+" AND event_id=" +
                                                    self.activeHaul + " AND ship=" + self.ship +
                                                    " AND survey=" + self.survey)

                if not query1.first():
                    # this sample has no basket weights
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                            "You haven't weighed any baskets for " + species + " in the " +
                                            partition + ". Do you want to return to sampling?", 'choice')
                    if self.message.exec_():
                        #  return to sampling to fix problem
                        self.returnFlag = True
                        return
                    else:
                        #  delete the sample that doesn't have a weight
                        query2 = QtSql.QSqlQuery("DELETE FROM samples WHERE samples.sample_id = " + key+
                                " AND samples.event_id=" + self.activeHaul + " AND samples.ship=" + self.ship +
                                " AND samples.survey=" + self.survey )
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+"," +
                                             query2.lastQuery())


                # validation #2 - are there samples of type measure lacking specimen (or length) data
                query2 = QtSql.QSqlQuery("SELECT sum(weight) FROM baskets WHERE basket_type = 'Measure'" +
                                         " AND sample_id=" + key+" AND baskets.event_id=" +
                                        self.activeHaul + " AND baskets.ship=" + self.ship +
                                        " AND baskets.survey=" + self.survey)
                query2.first()
                if not query2.value(0).toString() =='0':
                    # there are "measure" baskets - check if there are specimens
                    query3 = QtSql.QSqlQuery("SELECT * FROM specimen WHERE specimen.sample_id = " + key+
                            " AND specimen.event_id=" + self.activeHaul + " AND specimen.ship=" + self.ship +
                            " AND specimen.survey=" + self.survey, self.db)
                    if query3.first():
                        # there are also specimens
                        #validation #3 - verify that there is an appropriate sample weight for the number of specimens...
                        query=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code="+
                                code+" AND subcategory='"+subcategory+"' AND lower(species_parameter)='a_param'")
                        if query.first():
                            self.aParm=float(query.value(0).toString())
                        else:
                            self.aParm=None
                        query=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code="+
                                code+" AND subcategory='"+subcategory+"' AND lower(species_parameter)='b_param'")
                        if query.first():
                            self.bParm=float(query.value(0).toString())
                        else:
                            self.bParm=None

                        #  first check if there are length/weight parameters for this species
                        if self.aParm and self.bParm:
                            # there are LW parameters for this species
                            #  get the lengths
                            query5 = QtSql.QSqlQuery("SELECT measurements.measurement_value FROM " +
                                    " measurements WHERE AND measurements.sample_id=" + key +
                                    "  AND measurements.event_id=" + self.activeHaul + " AND measurements.ship=" +
                                    self.ship +" AND measurements.survey=" + self.survey+
                                    " AND measurements.measurement_type='length'",  self.db)

                            #  sum up the theoretical weights for the sampled lengths
                            calcWeight = 0
                            while query5.next():
                                length = float(query5.value(0).toString())
                                calcWeight += (length ** self.aParm) * self.bParm

                            #  get the sample weight and compare with the theoretical weight
                            subsampleWeight = float(query2.value(0).toString())
                            if calcWeight==0:
                                continue
                            deviation = (calcWeight - subsampleWeight) / calcWeight

                            #  check that the two weights are within the allowed threshold
                            if abs(deviation) > float(self.settings[QString('SubSampleCheckThreshold')]):
                                # The sample deviates too much from the theoretical weight
                                self.message.setMessage(self.errorIcons[1], self.errorSounds[1],"The weight of" +
                                                        " the measured sample is " + str(round(1+deviation, 0)) +
                                                        "% different from the estimated weight for " + species +
                                                        " in the " + partition + " using length weight regression" +
                                                        " of measured fish. You might have misclassified a Basket." +
                                                        " Do you want to return to the sampling?", 'choice')
                                if self.message.exec_():
                                    #  return to fix the problem
                                    self.returnFlag = True
                                    return
                                else:
                                    #  Ignore the problem - insert into override table
                                    self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                                            "You're in big trouble, " + self.firstName +
                                                            "!", 'info')
                                    self.message.exec_()

                                    #  insert into overrides table
                                    query6 = QtSql.QSqlQuery("INSERT INTO overrides (ship,survey,event_id,record_id,table_name," +
                                            "scientist,description) VALUES (" + self.ship + ", " + self.survey +
                                            "," + self.activeHaul + "," + key + ",'baskets','" +
                                            self.scientist + "','Bad subsample weight.'", self.db)
                                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+
                                            ","+query6.lastQuery())

                                    self.returnFlag = False

                    else:
                        # ask whether to return and samle stuff
                        self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "You have some basket" +
                                                " weights of type 'Measure' for " + species + " in the " +
                                                partition + " but no measurements!  Are you able to live with" +
                                                " yourself?", 'choice')
                        if not self.message.exec_():
                            self.returnFlag=True
                            return






