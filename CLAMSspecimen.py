
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_CLAMSSpecimen_collections
from conditionals import *
from validations import *

import listseldialog
import numpad
import keypad
import messagedlg
import collectionsdlg
import QZebraPrinter


class CLAMSSpecimen(QDialog, ui_CLAMSSpecimen_collections.Ui_clamsSpecimen):

    def __init__(self, parent=None):
        # initialize the super class and GUI
        super(CLAMSSpecimen, self).__init__(parent)
        self.setupUi(self)

        # general settings
        self.setAttribute(Qt.WA_DeleteOnClose)

        # pass variables from parent window
        self.db=parent.db
        self.workStation=parent.workStation
        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeHaul
        self.activePartition=parent.activePartition
        self.settings=parent.settings
        self.serMonitor=parent.serMonitor
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.backLogger=parent.backLogger
        self.blue = parent.blue
        self.black = parent.black
        self.gray="QPushButton { background-color: rgb(100,100,100)}"
        self.scientist=parent.scientist
        self.sqlLengthIndex = None
        self.freeze=False

        #  set the serial I/O temporal filter interval (in ms)
        #    Identical measurements from the same device will be ignored for this
        #    period of time filtering out accidental double scans/measurements
        #    from devices.
        self.__serialIOTimerInterval = 3000

        # check database connection
        if not self.db.isOpen():
            self.db.open()

        #  set the scientist labels
        self.sciLabel.setText(self.scientist)
        self.firstName = self.scientist.split(' ')[0]

        # figure out if this is administrative station
        actions = str(self.settings[QString('MainActions')])
        actions = actions.split(',')
        if 'Administration' in actions:
            self.admin = True
        else:
            self.admin = False

        # initialize variables
        self.activeSpcName = None
        self.activeSpcCode = None
        self.comment = ''
        self.value = None
        self.manualFlag = False
        self.serialValue = None
        self.specimenKey = None
        self.editFieldFlag = False
        self.editStateFlag = False
        self.incomplete = False
        self.protocol = None
        self.buttons = [self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        self.lastSerialValue = [None,None]
        self.devices = []
        self.sqlString = None
        self.activeCollections=[]
        self.collectionMeasurementTypes=[]# also temporary for now
        self.collectionDevices=[]# also temporary for now

        #setup reoccuring dlgs
        self.numpad = numpad.NumPad(self)
        self.message = messagedlg.MessageDlg(self)

        #  Check if we have a label printer attached at this workstation
        query=QtSql.QSqlQuery("SELECT MEASUREMENT_SETUP.DEVICE_ID, DEVICES.DEVICE_NAME " +
                             "FROM MEASUREMENT_SETUP INNER JOIN DEVICES ON " +
                             "MEASUREMENT_SETUP.DEVICE_ID = DEVICES.DEVICE_ID WHERE " +
                             "MEASUREMENT_SETUP.WORKSTATION_ID = " +  self.workStation +
                             " AND DEVICES.DEVICE_NAME = 'Label_Printer'" +
                             " GROUP BY MEASUREMENT_SETUP.DEVICE_ID, DEVICES.DEVICE_NAME")
        if query.first():
            #  initialize the Label Printer
            self.printer = QZebraPrinter.QZebraPrinter(self.serMonitor, str(query.value(0).toString()))
        else:
            #  no printer configured
            self.printer = None
            #self.printBtn.setEnabled(False)

        query=QtSql.QSqlQuery("select a.parameter_value " +
                            "from device_configuration a, devices b " +
                            "where a.device_id=b.device_id " +
                            "and b.device_name='Label_Printer' "+
                            "and a.device_parameter='SoundFile'")
        if query.first():
            self.printSound=QSound(self.settings[QString('SoundsDir')] + '/' + query.value(0).toString() +'.wav')
        else:
            self.printSound = None

        # set up button colors
        self.red="QPushButton { background-color: rgb(223,77,77)}"
        self.green="QPushButton { background-color: rgb(77,223,77)}"
        self.yellow="QPushButton { background-color: rgb(209,223,77)}"

        # set up window position
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.setGeometry((screen.width()-window.width())/2,parent.windowAnchor[0]+(parent.windowAnchor[1]-window.height()), window.width(), window.height())
        self.setMinimumSize(window.width(), window.height())
        self.setMaximumSize(window.width(), window.height())

        # set default sampling Method
        query = QtSql.QSqlQuery("SELECT sampling_method FROM sampling_methods")
        while query.next():
            self.samplingMethodBox.addItem(query.value(0).toString())
        self.samplingMethodBox.setCurrentIndex(self.samplingMethodBox.findText('random'))

        # set up our QTableView
        font = QFont('helvetica', 12, -1, False)
        self.measureView.setFont(font)
        self.measureModel = QtSql.QSqlQueryModel()
        self.measureView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.measureView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.measureView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.measureView.setModel(self.measureModel)
        self.selModel = QItemSelectionModel(self.measureModel, self.measureView)
        self.measureView.setSelectionModel(self.selModel)
        self.measureView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)

        #  Connect general slots
        self.connect(self.printBtn, SIGNAL("clicked()"), self.printLabel)
        self.connect(self.addspcBtn, SIGNAL("clicked()"), self.getSpecies)
        self.connect(self.cycleBtn, SIGNAL("clicked()"), self.getNext)
        self.connect(self.deleteBtn, SIGNAL("clicked()"), self.goDelete)
        self.connect(self.collectBtn, SIGNAL("clicked()"), self.getCollections)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)
        self.connect(self.protoBtn, SIGNAL("clicked()"), self.getProtocol)
        self.connect(self.selModel, SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.getEditSel)
        self.connect(self.serMonitor, SIGNAL("SerialDataReceived"), self.serialInput)
        self.connect(self.commentBtn, SIGNAL("clicked()"), self.getComment)
        self.connect(self.samplingMethodBox, SIGNAL("activated(int)"), self.editSamplingMethod)
        self.connect(self.lengthTypeBox, SIGNAL("activated(int)"), self.lengthTypeChanged)

        #  Connect up slots for protocol buttons
        for btn in self.buttons:
            self.connect(btn, SIGNAL("clicked()"), self.btnInput)

        #  initialize the timer for the serial I/O "temporal filter"
        self.__serialIOTimer = QTimer(self)
        self.__serialIOTimer.setSingleShot(True)
        self.__serialIOTimerOK = True
        self.connect(self.__serialIOTimer, SIGNAL("timeout()"), self.__serialIOFilter)

        #  set up an init timer
        initTimer = QTimer(self)
        initTimer.setSingleShot(True)
        self.connect(initTimer, SIGNAL("timeout()"), self.applicationInit)
        initTimer.start(0)


    def applicationInit(self):

        # get the first species
        self.initializing = True
        self.getSpecies()


    def __serialIOFilter(self):
        '''
        __serialIOFilter is an internal method that simply resets the __serialIOTimerOK
        property after a specific amount of time. When __serialIOTimerOK is false, serialInput
        will filter (ignore) values matching the last received value from a serial device.
        This helps eliminate accidental 2nd scans of bar codes, for example.
        '''
        self.__serialIOTimerOK = True


    def lengthTypeChanged(self):
        '''
        lengthTypeChanged is called when the length type combo box changes. It simply calls
        updateMeasureView to update the view to show the current length type.
        '''
        lengthType=self.lengthTypeBox.currentText()
        self.updateMeasureView()
        # Provide user with the length type that should be measured.
        # Use this to re-inforce the new length type policy
        QMessageBox.information(self, "Length Measurement Type", "<font size = 12>You should now measure " +lengthType)

    def getSpecies(self):

        #  check if we've been collecting data - if so, make sure we're done with this specimen
        if self.activeSpcCode and self.specimenKey:
            #  We've taken some specimens, call getNext() to make sure we're
            #  not in the middle of a specimen
            self.getNext()
            if self.incomplete:
                #  current specimen is incomplete - exit
                return

        # get valid species from catch
        species = []
        samples = []
        subCats=[]
        self.speciesDict = {}
        query=QtSql.QSqlQuery("SELECT species.common_name, species.scientific_name, samples.species_code, samples.sample_id, samples.subcategory FROM" +
                              " species, samples, baskets WHERE species.species_code = samples.species_code" +
                              " AND samples.ship=baskets.ship AND samples.survey=baskets.survey AND samples.event_id=baskets.event_id AND samples.sample_id=baskets.sample_id AND samples.ship=" + self.ship +
                              " AND samples.survey=" + self.survey + " AND samples.event_id=" + self.activeHaul +
                              " AND samples.partition='" + self.activePartition + "' AND baskets.basket_type=" +
                              " 'Measure' AND samples.species_code <> 0 GROUP BY species.common_name," +
                              " samples.species_code, species.scientific_name, samples.sample_id, samples.subcategory",  self.db)
        while query.next():
            subcat=query.value(4).toString()
            query0=QtSql.QSqlQuery("SELECT PARAMETER_VALUE FROM sample_data WHERE sample_parameter='sample_name' AND ship="+
            self.ship+" AND survey="+self.survey+" AND event_id="+self.activeHaul+ " AND sample_id="+query.value(3).toString())
            if query0.first():
                if (query0.value(0).toString() == 'scientific'):
                    spc = query.value(1).toString()
                else:
                    spc = query.value(0).toString()
            else:
                spc = query.value(0).toString()
            if subcat<>'None':
                name=spc+'-'+subcat
            else:
                name=spc
            species.append(name)
            samples.append(query.value(3).toString())
            subCats.append(subcat)
            self.speciesDict.update({str(name):str(query.value(2).toString())})

        #  Populate the list dialog with our species and present to user
        listDialog = listseldialog.ListSelDialog(species, 'Short', self)
        listDialog.label.setText('Pick a species to sample...')
        #listDialog.okBtn.setText('Sample')
        if not listDialog.exec_():
            #  user cancelled action
            return

        #  user selected a species - set some properties based on selection
        text=str(listDialog.itemList.currentItem().text())
        text1=text.split('-')
        self.activeSpcName = text1[0]
        if len(text1)>1:
            self.activeSpcSubcat = text1[1]
        else:
            self.activeSpcSubcat = 'None'
        self.activeSample = samples[species.index(text)]
        self.speciesLabel.setText(text)
        self.activeSpcCode = self.speciesDict[text]

        #  determine the length type
        self.lengthTypeBox.clear()
        self.lengthTypes = []
        params = ['primary_length_type',  'secondary_length_type']
        nParms = len(params)
        vals = [None] * nParms
        for i in range(nParms):
            query = QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code=" +
                    self.activeSpcCode+" AND subcategory='" + self.activeSpcSubcat +
                    "' AND lower(species_parameter)='" + params[i] + "'", self.db)
            if query.first():
                vals[i] = query.value(0).toString()

        # add primary length type
        if vals[0] <> None:
            self.lengthTypeBox.addItem(vals[0])
            self.lengthTypes.append(vals[0])
        else:
            #  if no primary length type is specified for this species+subcategory
            #  default to fork_length
            self.lengthTypeBox.addItem('fork_length')
            self.lengthTypes.append('fork_length')

        #  set the length type combo box to the primary measurement
        self.lengthTypeBox.setCurrentIndex(0)

        # add alternative (secondary) length type
        if vals[1] <> None:
            self.lengthTypeBox.addItem(vals[1])
            self.lengthTypes.append(vals[1])

        #  determine the maturity table
        query=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code="+self.activeSpcCode+
                " AND subcategory='"+self.activeSpcSubcat+"' AND lower(species_parameter)='maturity_table'", self.db)
        if query.first():
             self.maturityTable =  query.value(0).toString()
        else:
            self.maturityTable = ''

        #  have the user select the protocol
        ok = self.getProtocol()
        if not ok:
            if self.initializing:
                #  user cancelled and we're still setting up - close out
                self.close()
                return
            else:
                #  user cancelled action
                return
        self.initializing = False

        #get picture
        if self.activeSpcSubcat<>'None':
            imgName=self.activeSpcCode # +"_"+self.activeSpcSubcat
        else:
            imgName=self.activeSpcCode
        pic=QImage()
        if pic.load(self.settings[QString('ImageDir')]+'\\fishPics\\'+imgName+".jpg"):
            pic = pic.scaled(self.picLabel.size(),Qt.KeepAspectRatio)#,  Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(pic))
        else:
             self.picLabel.clear()

        #check for existing records
        self.updateMeasureView()
        self.cycleBtn.setEnabled(True)


    def getProtocol(self):
        '''
        getProtocol prompts the user to select a protocol for the currently active species.
        '''

        #  build a list of the active protocols for this species
        self.protocols=[]
        nProtocols = 0
        query=QtSql.QSqlQuery("SELECT protocol_name FROM protocol_map WHERE species_code = " +
                              self.activeSpcCode + " AND subcategory= '"+self.activeSpcSubcat +"' AND active=1")
        while query.next():
            nProtocols = nProtocols + 1
            self.protocols.append(query.value(0).toString())

        if nProtocols == 0:
            QMessageBox.information(self, "Huh...", "<font size = 12>There are no protocols defined " +
                    "for this species. If you want to sample this species you must link it to some " +
                    "protocols in the protocol_map table.")
            return False

        #  present the list to the user
        listDialog = listseldialog.ListSelDialog(self.protocols,'Short', self)
        listDialog.label.setText('Pick a sampling protocol...')
        listDialog.okBtn.setText('Sample')
        if listDialog.exec_():
            #  user selected a protocol - set some props and return true
            self.protocol = listDialog.itemList.currentItem().text()
            self.protoLabel.setText(self.protocol)
            self.setup()
            self.updateMeasureView()
            return True
        else:
            #  user cancelled selection - return false
            return False


    def serialInput(self, device, val):

        #  ignore empty inputs
        if (val == None) or (val == ''):
            return
        if self.freeze:
            return

        # figure out code direction for value
        self.manualFlag = False
        try:
            #  get an index into our devices list for this device
            ind = self.devices.index(device)
        except:
            #  somehow we have received data from a device we didn't configure?
            print("ERROR: CLAMSspecimen.serialInput: received data from unknown device? How can that be?")
            return

        #  Check if we have a duplicate serial value within the filter timer period
        if (self.__serialIOTimerOK == False):
            if (ind == self.lastSerialValue[0]) and (val == self.lastSerialValue[1]):
                #  This measurement is the same as the last and we're within our filter period - ignore
                return

        #  set the serial value variables
        self.lastSerialValue = [ind, val]
        self.serialValue = val

        #  set the timer OK value to false and start the filter timer
        self.__serialIOTimerOK = False
        self.__serialIOTimer.start(self.__serialIOTimerInterval)

        #  Check if this measurement is "in order" or out of order.
        if (self.forceOrder[ind] == '1'):
            #  this is an in order measurement - determine if this device
            #  provides multiple measurements
            if (self.devices.count(device) == 1):
                # only one measurement using this device
                self.cycle(ind)
            else:
                # this device can provide multiple measurements - find next empty value
                for i in self.iterator:
                    if (self.devices[i] == device) and (self.values[i] == None):
                        self.cycle(i)
                        break
        else:
            #  this measurement is an out of order measurement
            self.outCycle(ind)


    def btnInput(self):
        '''
        btnInput is called when a protocol button is pressed. The protocol buttons can be
        pressed to manually enter or edit a value.
        '''

        #  determine what button was pressed
        ind = self.buttons.index(self.sender())

        #  set the manual flag
        self.manualFlag = True

        #  Check if this measurement is "in order" or out of order.
        if (self.forceOrder[ind] == '1'):
            #  measurement is in order
            self.cycle(ind)
        else:
            #  this measurement is an out of order measurement
            self.outCycle(ind)


    def cycle(self, i):
        '''
            cycle is called each time a measurement is taken. It performs the validations before
            passing measurement on to writeMeasurement.
        '''

        #  check if this measurement has been disabled
        if (not self.buttons[i].isEnabled()):
            # this measurement is disabled - skip on to the next measurement
            self.moveOn(i)
            return

        # check for existing measurement
        self.editFieldFlag = False
        if (not self.values[i] == None):
            self.freeze=True
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2], 'You already measured the ' +
                                    self.label[i] + '. Do you want to overwrite it?', 'choice')
            if self.message.exec_():
                # overwrite the measurement
                self.editFieldFlag = True
                self.freeze=False
            else:
                # redo the measurement
                self.freeze=False
                return

        #check the order
        if not self.editStateFlag:
            self.checkOrder(i)
            if self.orderCheckFlag:
                return

        #  Get the measurement value
        if (self.interface[i] == 'Software'):
            #  The measurement value comes from a custom dialog box (for example sex selection)

            #  setup and display the dialog
            self.i = i
            self.dialogs[i].setup(self)
            self.dialogs[i].exec_()

            #  process the result
            result = self.dialogs[i].result
            if result[0]:
                #  user slected a value
                val = result[1]
            else:
                #  user cancelled action
                return
        else:
            #  The measurement value can come from a device or it could come from
            #  a dialog if the user has pushed the measurement button in the GUI

            #  check if this is a manually entered value or from a device
            if (self.manualFlag):
                #  this value is entered manually - display the number pad
                self.numpad.msgLabel.setText("Enter " + self.label[i])
                if not self.numpad.exec_():
                    #  user cancelled action
                    return
                #  get the number from the numpad and unset manualFlag value
                val = self.numpad.value
                #  check that we didn't get a 0 weight
                if (val == '0'):
                    self.message.setMessage(self.errorIcons[2],self.errorSounds[2], "You have entered 0 (zero) "
                        "for the basket weight which is not allowed. If your sample is too small to register " +
                        "on the scale, you should enter 0.001", 'info')
                    self.message.exec_()
                    return
                self.manualFlag = False

            elif not (self.serialValue == None):
                # value coming from serial device
                val = self.serialValue
                self.serialValue = None
            else:
                return

        # play the sound
        self.sounds[i].play()

        # do the validations
        for valObj in self.validations[i]:
            result = valObj.validate(val, self.measureType, self.values)
            if not result[0] and not result[0] ==None:
                # validation failed - ask if user wants to redo or override
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1], result[1], 'choice')
                if self.message.exec_():
                    # redo the measurement
                    return
                else:
                    # user has overridden the validation error
                    if not self.specimenKey == None:
                        self.message.setMessage(self.errorIcons[2],self.errorSounds[2],
                                                "You're in big trouble, " + self.firstName, 'info')
                        #  insert event into overrides table
                        query = QtSql.QSqlQuery("INSERT INTO overrides (ship,survey,event_id,record_id,table_name," +
                                "scientist,description) VALUES (" + self.ship + ", " + self.survey +
                                "," + self.activeHaul + "," + self.specimenKey + ",'measurements','" +
                                self.scientist + "','Specimen weight is outside valid range.'", self.db)
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+
                                ","+query.lastQuery())

        self.values[i]=val
        self.writeMeasurement(i, True)


    def outCycle(self, i):
        '''
            OutCycle is called each time an out of order serial measurement is taken. It performs the validations before
            passing measurement on to writeMeasurement.
        '''

        #  check if this measurement has been disabled
        if (not self.buttons[i].isEnabled()):
            return

        # check for existing measurement
        self.editFieldFlag = False
        if (not self.values[i] == None):
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2], 'You already measured the ' +
                                    self.label[i] + '. Do you want to overwrite it?', 'choice')
            if self.message.exec_():
                # overwrite the measurement
                self.editFieldFlag = True
            else:
                # redo the measurement
                return

        # get the value
        if self.interface[i]=='Software':
            result = [None]

#            try:
            #  try to execute the software measurement dialog
            self.dialogs[i].setup(self)
            self.dialogs[i].exec_()
            result=self.dialogs[i].result
#            except:
#                #  this dialog doesn't exist or it has an internal error
#                result = [None]
#                return

            #  check if we got a value from the dialog
            if result[0]:
                val=result[1]
            else:
                return
        else:
            #  check if this is a manually entered value or from a device
            if self.manualFlag:
                #  this value is entered manually
                self.numpad.msgLabel.setText("Enter " + self.label[i])
                if not self.numpad.exec_():
                    return
                val = self.numpad.value
                #  check that we didn't get a 0 weight
                if (val == '0'):
                    self.message.setMessage(self.errorIcons[2],self.errorSounds[2], "You have entered 0 (zero) "
                        "for the basket weight which is not allowed. If your sample is too small to register " +
                        "on the scale, you should enter 0.001", 'info')
                    self.message.exec_()
                    return
                self.manualFlag = False

            elif not self.serialValue==None:
                # value coming from serial device
                val = self.serialValue
                self.serialValue = None
            else:
                return

        # play the sound
        self.sounds[i].play()

        # do the validations
        for valObj in self.validations[i]:
            result = valObj.validate(val, self.measureType, self.values)
            if not result[0] and not result[0] ==None:
                # validation failed - ask if user wants to redo or override
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1], result[1], 'choice')
                if self.message.exec_():
                    # redo the measurement
                    return
                else:
                    # user has overridden the validation error
                    if not self.specimenKey == None:
                        self.message.setMessage(self.errorIcons[2],self.errorSounds[2],
                                "You're in big trouble, " + self.firstName, 'info')
                        #  insert event into overrides table
                        query = QtSql.QSqlQuery("INSERT INTO overrides (ship,survey,event_id,record_id,table_name," +
                                "scientist,description) VALUES (" + self.ship + ", " + self.survey +
                                "," + self.activeHaul + "," + self.specimenKey + ",'measurements','" +
                                self.scientist + "','Specimen weight is outside valid range.'", self.db)
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+
                                ","+query.lastQuery())

        self.values[i]=val
        self.writeMeasurement(i, False)


    def writeMeasurement(self, i, keepGoing):
        '''
            writeMeasurement is called each time a measurement is taken. It inserts or updates data in the db
            for that measurement type and also logs the SQL to a text file.
        '''

        #  check if this is the first measurement for this specimen
        if (self.specimenKey == None):
            # first measurement - get a specimen key
            self.getNewSpecimen()

        #  disable the protocol change button - only can change protocols
        #  when you're not in the middle of processing a specimen
        self.protoBtn.setEnabled(False)
        #  change the button text to green
        self.buttons[i].setStyleSheet(self.green)
        if self.measureType[i]=='length':
            measure_type=self.lengthTypeBox.currentText()
        else:
            measure_type=self.measureType[i]

        #  check if we're editing (overwriting) a record or inserting a new one
        if self.editFieldFlag:
            # overwrite record - UPDATE
            query =QtSql.QSqlQuery("UPDATE measurements SET measurement_value ='" +
                                   self.values[i] + "' WHERE  ship="+self.ship+" AND survey="+self.survey+" AND event_id="+self.activeHaul+
                                   " AND sample_id="+self.activeSample+" AND specimen_id = " +self.specimenKey + " AND measurement_type = '" +
                                   measure_type+"'")
            #  insert the last SQL statement into the local log file
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + "," + query.lastQuery())
            # update table
            self.updateMeasureView()
            self.checkConditionals()

        else:
            #  this is a new record - INSERT
            query = QtSql.QSqlQuery("INSERT INTO measurements (ship, survey, event_id, sample_id, specimen_id, measurement_type, device_id, " +
                                    "measurement_value) VALUES (" +self.ship+","+self.survey+","+self.activeHaul+ ","+self.activeSample+","+ self.specimenKey + ",'" +
                                    measure_type + "'," + self.devices[i] + ",'" +
                                    self.values[i] + "')")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            # update table
            self.updateMeasureView()
            # check conditionals
            self.checkConditionals()
            if keepGoing:
                self.moveOn(i)


    def moveOn(self, i):
        #  check if this is the last measurement
        while i < len(self.values)-1:
            # this is not the last available measurement - check if the next measurement is forced

            if self.forcing[i+1]=='1' and self.values[i+1]==None and self.buttons[i+1].isEnabled():
                # next measurement is forced - check if it is from a serial device
                if self.interface[i+1]=='Software':# next input is software, fire it away

                    self.cycle(i+1)
                    break
                else:
                    # next measurement is serial, just wait for it
                    break

            else:
                i=i+1

        # this is the last measurement
        if i == len(self.values)-1:
            if self.autoCheck.isChecked():
                self.protoBtn.setEnabled(True)
                self.getNext()


    def checkConditionals(self):
            self.buttonEnable=[]
            for i in self.iterator:
                self.buttonEnable.append(True)
            for condObj in self.conditionals:
                self.buttonEnable=condObj.evaluate(self.measureType,  self.values, self.buttonEnable)
            for i in self.iterator:
                btn=self.buttons[i]
                btn.setEnabled(self.buttonEnable[i])
                if not self.buttonEnable[i]:
                    btn.setStyleSheet(self.gray)

#########################################################################################

    def getNext(self, skipChecks=False):
        '''
        getNext checks that all required measurements have been collected for a sample
        and then resets the system for the next sample. The skipChecks keyword can be set
        to True to bypass the checks when you are deleting a sample.
        '''

        if (not skipChecks) and (not self.specimenKey == None):
            # check specimen and make sure all required measurements have been collected
            for i in self.iterator:
                self.incomplete = False
                btn = self.buttons[i]
                if (self.values[i] == None) and (self.forcing[i] == '1') and (btn.isEnabled()):
                    #  a measurement is missing - ask the user what they want to do
                    self.message.setMessage(self.errorIcons[0], self.errorSounds[0], "You still need a " +
                                            self.measureType[i] + " measurement. Does this bother you, " +
                                            self.firstName + "?", 'choice')
                    if self.message.exec_():
                        #  user doesn't want to skip the measurement - return to sampling
                        self.incomplete = True
                        return
                    else:
                        #  user wants to skip this measurement - log it
                        self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                                "You're in big trouble, " + self.firstName, 'info')
                        self.message.exec_()
                        #  insert event into overrides table
                        query = QtSql.QSqlQuery("INSERT INTO overrides (ship,survey,event_id,record_id,table_name," +
                                "scientist,description) VALUES (" + self.ship + ", " + self.survey +
                                "," + self.activeHaul + "," + self.specimenKey + ",'measurements','" +
                                self.scientist + "','User skipped required protocol measurement.'", self.db)
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+
                                ","+query.lastQuery())

        #  R. Levine - added qsound to make noise when hit next
        QSound(self.settings[QString('SoundsDir')]+'\\snapjaw.wav').play()
        # re-show all the buttons
        for i in self.iterator:
            self.values[i] = None
            self.buttons[i].setEnabled(True)
        #  reset the specimen key
        self.specimenKey = None
        self.specimenLabel.setText('')
        #  reset the button colors
        self.resetColors()
        #  clear the comment
        self.comment=''
        #  reset the editing state
        self.editStateFlag = False
        #  enable the change protocol button - only enabled when you're not processing a specimen
        self.protoBtn.setEnabled(True)


    def getNewSpecimen(self):
        '''
        getNewSpecimen inserts the initial data into the specimen table and then queries
        the table for the newly generated specimen id. Specimen Id's are generated by a
        sequence in the database.
        '''

        #  get the current sampling method
        samplingMethod = self.samplingMethodBox.currentText()

        #  check that we're connected to the db
        if not self.db.isOpen():
            #  we're not connected
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2], "Database is not connected" +
                                    " - restart clams", 'info')
            self.message.exec_()
            return

        #  insert the initial data into specimen
        query = QtSql.QSqlQuery("INSERT INTO specimen (ship, survey, event_id, sample_id, workstation_id, scientist, " +
                                " sampling_method, protocol_name, comments) VALUES (" +self.ship+","+self.survey+","+self.activeHaul+ ","+self.activeSample+","+
                                self.workStation + ",'" + self.scientist + "','" + samplingMethod + "','" + self.protocol + "','" + self.comment + "')")
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + "," + query.lastQuery())

        # get the newly created specimen key
        query = QtSql.QSqlQuery("SELECT max(specimen_id) FROM specimen WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+self.activeHaul+
                                   " AND sample_id="+self.activeSample+" AND workstation_id=" + self.workStation)
        query.first()
        self.specimenKey = query.value(0).toString()
        self.specimenLabel.setText(self.specimenKey)


    def updateMeasureView(self):
        '''
        updateMeasureView updates the GUI table that presents the specimen measurements to the user.
        This method is called every time the specimen data changes. We take a very conservative approach
        where we requery the specimen data on every update to convince the user that the data are
        being recorded.
        '''

        #  if we have "length" as a measurement in the protocol - switch
        #  the generic length with the specific length type currently being used
        #  If there is no "length" as a measurement, we want all specimens from that sample and protocol,
        #  without length type is not null attached to the end of the sql query
        if (self.sqlLengthIndex != None):
            #  create the SQL string based on the current length type
            length_type = str(self.lengthTypeBox.currentText())
            sqlStringEnd=' AND '+length_type+' IS NOT NULL '
            #  insert the current length type
            self.sqlString[self.sqlLengthIndex] = length_type
        else:
            # For this case, the sqlString will already be formatted correctly because the length types were established in the protocol
            # And we want all of the specimens for that sample and protocol, so no ending sql string is needed- set it to one space string
            sqlStringEnd=' '

        #  create the string
        sqlString = ','.join(self.sqlString)

        #  set the model view SQL
        if self.admin:
            #  admin mode shows all measurements
            self.measureModel.setQuery("SELECT SPECIMEN_ID, "+ sqlString +" FROM V_SPECIMEN_MEASUREMENTS WHERE " +
                                      "ship="+self.ship+" AND survey="+self.survey+" AND haul="+self.activeHaul+
                                      " AND sample_id="+self.activeSample+"  AND " +
                                      "PROTOCOL_NAME = '" + self.protocol +"'" + sqlStringEnd +
                                      "ORDER BY SPECIMEN_ID")
        else:
            #  regular mode shows only measurements at that station
            sql = ("SELECT SPECIMEN_ID, "+ sqlString +" FROM V_SPECIMEN_MEASUREMENTS WHERE " +
                  "ship="+self.ship+" AND survey="+self.survey+" AND haul="+self.activeHaul+
                  " AND sample_id="+self.activeSample+"  AND " +
                  "PROTOCOL_NAME = '" + self.protocol + "' AND WORKSTATION_ID = " +
                  self.workStation + sqlStringEnd + "ORDER BY SPECIMEN_ID")
            self.measureModel.setQuery(sql)

        # set up table labels
        self.measureModel.setHeaderData(0, Qt.Horizontal, "Spec. ID")
        for i in self.iterator:
            self.measureModel.setHeaderData(i + 1, Qt.Horizontal, self.label[i])
        self.measureModel.reset()
        self.measureView.scrollToBottom()


    def setup(self):

        # hide all of the measurement buttons
        for btn in self.buttons:
            btn.hide()

        #  initialize the various lists that store operational details
        self.measureType=[]
        self.devices=[]
        self.forcing=[]
        self.forceOrder=[]
        self.label=[]
        self.sounds=[]
        self.dialogs=[]
        self.interface=[]
        self.validations=[]
        self.values=[]
        self.sqlString=[]
        self.sqlLengthIndex = None
        nMeasurements = 0

        # get the measurements for this species
        query=QtSql.QSqlQuery("SELECT PROTOCOL_DEFINITIONS.MEASUREMENT_TYPE, MEASUREMENT_SETUP.DEVICE_ID, MEASUREMENT_SETUP.DEVICE_INTERFACE,  "+
                              "PROTOCOL_DEFINITIONS.FORCE_MEASUREMENT, PROTOCOL_DEFINITIONS.FORCE_ORDER, PROTOCOL_DEFINITIONS.LABEL "+
                              " FROM PROTOCOL_DEFINITIONS, MEASUREMENT_SETUP WHERE ( MEASUREMENT_SETUP.MEASUREMENT_TYPE = "+
                              "PROTOCOL_DEFINITIONS.MEASUREMENT_TYPE ) and ( ( PROTOCOL_DEFINITIONS.PROTOCOL_NAME = '"+self.protocol+"' ) AND "+
                              "( MEASUREMENT_SETUP.WORKSTATION_ID = "+self.workStation+" ) AND ( MEASUREMENT_SETUP.GUI_MODULE = 'Specimen' ) ) "+
                              " ORDER BY PROTOCOL_DEFINITIONS.MEASUREMENT_ORDER ASC")


        #  Initialize length type combo box to disabled until you encounter a 'length' in the protocol
        self.lengthTypeBox.setEnabled(False)
        #  loop through the measurements we have found and extract the deets
        while query.next():
            measure_type=query.value(0).toString()
            self.measureType.append(measure_type)
            self.devices.append(query.value(1).toString())
            self.interface.append(query.value(2).toString())
            self.forcing.append(query.value(3).toString())
            self.forceOrder.append(query.value(4).toString())
            self.label.append(query.value(5).toString())

            # get the sounds for the device
            query1=QtSql.QSqlQuery("SELECT device_configuration.PARAMETER_VALUE FROM device_configuration WHERE " +
                    "(device_configuration.DEVICE_ID = "+ query.value(1).toString()+") AND (" +
                    "device_configuration.DEVICE_PARAMETER = 'SoundFile' )")
            if query1.first():
                self.sounds.append(QSound(self.settings[QString('SoundsDir')]+'\\'+query1.value(0).toString()+'.wav'))
            else:
                self.sounds.append(QSound(self.settings[QString('SoundsDir')]+'\\softwareSound.wav'))

           # for software inputs, get the dialog to be used
            if query.value(2).toString()=='Software':
                query1=QtSql.QSqlQuery("SELECT device_configuration.PARAMETER_VALUE FROM device_configuration WHERE " +
                        "(device_configuration.DEVICE_ID = " + query.value(1).toString() + " ) AND (" +
                        "device_configuration.DEVICE_PARAMETER = 'Module' )")
                if query1.first():
                    #  module name found - import and instantiate an instance of it
                    dlg = query1.value(0).toString()
                    updlg = dlg
                    try:
                        exec(str('from measurementDialogs import '+dlg.toLower()))
                        exec(str('dlgObj='+dlg.toLower()+'.'+updlg+'(self)'))
                        self.dialogs.append(dlgObj)
                    except Exception as e:
                        #  there was a problem importing or instantiating the measurement dialog
                        self.dialogs.append(None)
                        self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                            "Error importing or instantiating the " + dlg.toLower() +
                            " measurement dialog.\nError text: '" + str(e) + "'\n"
                            "This measurement will not be available until the issue is fixed.", 'info')
                        self.message.exec_()
                else:
                    #  we were unable to find a Module entry in device_configuration for this device ID
                    self.dialogs.append(None)

                    #  get the device name for the error dialog
                    query1 = QtSql.QSqlQuery("SELECT device_name FROM devices WHERE device_id=" +
                            query.value(1).toString())
                    if query1.first():
                        deviceName = query1.value(0).toString()
                    else:
                        deviceName = "Unknown (device ID " + query.value(1).toString() + ")"

                    #  present the error dialog
                    self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                        "No module definition found in the device_configuration table for " +
                        "software device " + deviceName + ". The measurement associated with " +
                        "this device will not function." , 'info')
                    self.message.exec_()
            else:
                #  this measurement does not have a dialog (aka hardware measurement)
                self.dialogs.append(None)

            # get validations
            query1=QtSql.QSqlQuery("SELECT VALIDATION FROM VALIDATIONS WHERE ( "+
                    "PROTOCOL_NAME = '"+self.protocol+"' ) AND ( "+
                    "MEASUREMENT_TYPE = '"+query.value(0).toString()+"') "+
                    "ORDER BY VALIDATION_ORDER ASC ", self.db)
            vals=[]

            #  create an instance of the validation object and add to our list of validations
            while query1.next():
                val=query1.value(0).toString()
                exec(str('valObj='+val+'.'+val+'(self.db,self.activeSpcCode, self.activeSpcSubcat)'))
                vals.append(valObj)
            self.validations.append(vals)

            #  build the measureView SQL list - this is a list of the measurements that
            #  we join with a comma to generate a string right before using it in the
            #  updateMeasureView method. We store the items as a list so we can easily
            #  swap out the length type if the user changes it.

            #  First we check if this is a length measurement. Lengths are treated special
            #  since we are allowing the generic measurement "length" to map to multiple
            #  real measurement types. This breaks the rules and is not ideal, but this
            #  change was implemented years after CLAMS was initially written and it is
            #  too late at this point to change everything.
            #  Enable lengthType combo box if there is 'length' type- otherwise it will be disabled
            if (measure_type == 'length'):
                #  store the index of "length" in the SQL string so we can swap it out
                #  when the user changes the length_type
                self.sqlLengthIndex = nMeasurements
                self.lengthTypeBox.setEnabled(True)
                # Provide user with the length type that should be measured.
                # Use this to re-inforce the new length type policy
                lengthType=self.lengthTypeBox.currentText()
                QMessageBox.information(self, "Length Measurement Type", "<font size = 12>You should now measure " +lengthType)


            #  append this measurement onto our sqlString list
            self.sqlString.append(str(measure_type))

            #  increment the measurements counter
            nMeasurements = nMeasurements + 1

            # initialize the value vector
            self.values.append(None)

        #  set up the measurement buttons
        for i in range(len(self.label)):
            # show button
            self.buttons[i].show()
            self.buttons[i].setText(self.label[i])
        # if there are optional items, cant use autocycle
        if '0' in self.forcing:
            self.autoCheck.setEnabled(False)
        else:
            self.autoCheck.setEnabled(True)
        # default is always random
        self.samplingMethodBox.setCurrentIndex(self.samplingMethodBox.findText('random'))

        # get conditionals
        query=QtSql.QSqlQuery("SELECT CONDITIONALS.CONDITIONAL FROM CONDITIONALS WHERE ( "+
                                            "CONDITIONALS.PROTOCOL_NAME = '"+self.protocol+"')", self.db)
        self.conditionals=[]
        while query.next():
            cond=query.value(0).toString()
            upcond=cond
            exec(str('condObj='+cond.toLower()+'.'+upcond+'(self.db)'))
            self.conditionals.append(condObj)

        self.iterator=range(len(self.measureType))
        # collections - this will be done though DB in the future
        self.activeCollections=['Stomach', 'Ovary']
        self.collectionMeasurementTypes=['stomach_taken', 'ovary_taken']# also temporary for now
        self.collectionDevices=['5', '7']# also temporary for now


        self.resetColors()
        self.editStateFlag=False

        #  check to make sure we set up at least one measurement
        if len(self.values) == 0:
            #  we don't even have one measurement :(
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                "Either this protocol is not set up correctly or your workstation does not have any measurements " +
                "configured in measurement_setup. Please select a different protocol or configure your " +
                "workstation correctly.", 'info')
            self.message.exec_()
        else:
            self.cycle(0)


    def goDelete(self):

        #  ensure that a specimen is selected
        if (self.specimenKey == None):
            #  no specimen is currently selected
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                    "Please select a specimen to delete.", 'info')
            self.message.exec_()
            return

        #  verify that the user wants to delete the specimen
        self.message.setMessage(self.errorIcons[0], self.errorSounds[0], "Are you sure you want to delete" +
                                " specimen " + self.specimenKey + ", " + self.firstName + "? ", 'choice')
        if self.message.exec_():
            #  yes - delete the specimen
            query = QtSql.QSqlQuery("DELETE FROM measurements WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND specimen_id = " + self.specimenKey, self.db)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + ", " +
                                 query.lastQuery())
            query=QtSql.QSqlQuery("DELETE FROM specimen WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND specimen_id = "+self.specimenKey, self.db)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + ", " +
                                 query.lastQuery())

            #  update the view
            self.updateMeasureView()
            self.specimenLabel.setText('')
            #  reset for the next sample - skip the checks since we're deleting this sample
            self.getNext(skipChecks=True)


    def resetColors(self):
        '''
        resetColors resets the button colors after a specimen has been taken, deleted, or is being edited
        '''

        #  loop thru the buttons
        for i in self.iterator:
            btn = self.buttons[i]

            #  check if we're editing this specimen
            if self.editStateFlag:
                #  we're editing - check if there is a value for this measurement
                if self.values[i]:
                    # already measured - set the button green
                    btn.setStyleSheet(self.green)
                else:
                    #  we haven't taken this measurement - check if it's required or optional
                    if (self.forcing[i] == '1'):
                        #  this measurement is required - set the button red
                        btn.setStyleSheet(self.red)
                    else:
                        #  this measurement is optional - set yellow
                        btn.setStyleSheet(self.yellow)
            else:
                #  we're not editing so we don't check for any existing values\
                #  just check for required vs optional measurements
                if (self.forcing[i] == '1'):
                    #  this measurement is required - set the button red
                    btn.setStyleSheet(self.red)
                else:
                    #  this measurement is optional - set yellow
                    btn.setStyleSheet(self.yellow)

        #  check if we're editing
        if self.editStateFlag:
            #  we're editing so we need to check the conditionals
            self.checkConditionals()


    def getEditSel(self):

        # this prevents method from firing on DE-selection
        if self.selModel.selection().count()==0:
            return

        #  get the specimen id for the selected row
        selObj = self.measureView.currentIndex()
        index = self.measureModel.index(selObj.row(), 0, QModelIndex())
        thisSpecimenKey = self.measureModel.data(index, Qt.DisplayRole).toString()

        #  check if the selected row is the most current specimen
        if (thisSpecimenKey == self.specimenKey):
            #  The selected row is the current specimen - nothing else to do here
            return

        #  The selected row is not the most current specimen
        #  check that the current specimen is complete before editing an old specimen
        content = False
        for i in self.values:
            if i <> None:
                content = True
        if content:
            #  there are missing measurements throw up a dialog
            for i in range(len(self.measureType)):
                btn = self.buttons[i]
                if (self.values[i] == None) and (self.forcing[i] == '1') and (btn.isEnabled()):
                    self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "Dear "+self.firstName+", "+
                                        "Please finish up your current specimen before editing.",'info' )
                    self.message.exec_()
                    self.selModel.clearSelection()
                    return

        #  set the specimen_id and update it on the GUI
        self.specimenKey = thisSpecimenKey
        self.specimenLabel.setText(thisSpecimenKey)

        # re-initialize measurement array
        self.values = [None] * len(self.measureType)

        #  query the measurements for this specimen
        query = QtSql.QSqlQuery("SELECT measurement_type, measurement_value FROM measurements WHERE ship=" +
                self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND specimen_id = " +
                self.specimenKey, self.db)
        while query.next():

            #  now try to get the index into our measurements array for this
            #  measurement type. This will work for every measurement *except*
            #  the specific length types since lengths break the rule of
            try:
                ind = self.measureType.index(query.value(0).toString())
            except:

                #  since we failed finding this measurement, this should be one of
                #  the specific length measurements for this species+subcode
                if (query.value(0).toString() in self.lengthTypes):
                    ind = self.measureType.index('length')
                else:
                    #  huh. This shouldn't happen....
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                            "Measurement '" + query.value(0).toString() + "' found when reloading " +
                            "the specimen for edit. This measurement is not in the current protocol." +
                            " This can only happen if the protocol was changed after data was already " +
                            "collected which is generally considered bad form. You will not be able to" +
                            " alter this measurement using CLAMS.", 'info')
                    self.message.exec_()
                    continue

            #  Now that we did all that work to get the index, set the measurement value
            self.values[ind] = query.value(1).toString()

        # set the random flag and get the comments
        query=QtSql.QSqlQuery("SELECT sampling_method, comments FROM specimen WHERE ship="+
                self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                " AND specimen_id = "+self.specimenKey, self.db)
        query.first()
        self.samplingMethodBox.setCurrentIndex(self.samplingMethodBox.findText(query.value(0).toString()))
        self.comment = query.value(1).toString()
        self.editStateFlag = True
        self.resetColors()


    def checkOrder(self, i):
        '''
        checkOrder enforces the protocol order.
        '''
        # this is not a validation but an internal check that the protocol order is being followed
        self.orderCheckFlag = False
        self.outOfOrder=False
        if (self.forceOrder[i] == '1'):
            for j in range(i):
                if (self.values[j]==None) and (self.forceOrder[j]=='1') and (self.buttons[j].isEnabled()) and (self.forcing[j]=='1'):
                    # a measurement below this one in order has not been made and the order for this is forced
                    self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "Dear " +
                                            self.firstName + ", you screwed up the order. Measure the " +
                                            self.measureType[j]+" first, please.",'info' )
                    self.message.exec_()
                    self.values[i] = None
                    self.orderCheckFlag = True
                    break
        else:
            self.outOfOrder=True


    def getCollections(self):
        if self.specimenKey == None:
            return
        # fire up dialog
        collectionDialog = collectionsdlg.CollectionsDlg(self.activeCollections, self)
        #listDialog.okBtn.setText('Sample')
        if collectionDialog.exec_():# we want to print stuff and we made collections
            # iterate though boxes and get checked ones - non-visible boxes default to uncecked
            for i, box in enumerate(collectionDialog.checkboxes):
                if box.isChecked():
                    # insert measurement
                    sql=("INSERT INTO measurements (ship,survey,event_id,sample_id,specimen_id," +
                            "measurement_type,device_id,measurement_value) VALUES ("+self.ship+","+
                            self.survey+","+self.activeHaul+ ","+self.activeSample+","+ self.specimenKey + ",'" +
                            self.collectionMeasurementTypes[i] + "'," + self.collectionDevices[i] + ",'Yes')")
                    QtSql.QSqlQuery(sql)
                    self.printLabel()



    def printLabel(self):
        '''
        printLabel is called when the "Print Label" button is pressed. Labels are usually
        printed for special specimen collection projects and they contain information that
        allows the person processing the sample to link it back to the specimen in CLAMSBASE.
        '''

        #  make sure that a specimen has been selected
        if (self.specimenKey == None):
            self.message.setMessage(self.errorIcons[0], self.errorSounds[0], "Please Select a "+
                    "specimen to print a label for.")
            self.message.exec_()
            return

        #  check that all requried measurements have been obtained
        for i in self.iterator:
            btn = self.buttons[i]
            if (self.values[i] == None) and (self.forcing[i] == '1') and (btn.isEnabled()):
                #  a measurement is missing - ask the user what they want to do
                self.message.setMessage(self.errorIcons[0], self.errorSounds[0], "You still need a " +
                                        self.measureType[i] + " measurement. Does this bother you, " +
                                        self.firstName + "?", 'choice')
                if self.message.exec_():
                    #  user doesn't want to print label - return to sampling
                    self.incomplete = True
                    return
                else:
                    #  user wants to print a label anyways
                    break

        #  get data from db - query everything *BUT* length
        query = QtSql.QSqlQuery("SELECT ship, survey, haul, specimen_id, species_code, common_name, "+
                "organism_weight, sex, maturity, scientist, barcode FROM v_specimen_measurements WHERE "+
                "survey=" + self.survey +" AND ship="+self.ship+" AND specimen_id="+self.specimenKey)

        query.first()
        vessel = query.value(0).toString()
        survey = query.value(1).toString()
        haul = query.value(2).toString()
        spec_id = query.value(3).toString()
        code = query.value(4).toString()
        name = query.value(5).toString()
        weight = query.value(6).toString()
        sex = query.value(7).toString()
        maturity = query.value(8).toString()
        scientist = query.value(9).toString()
        barcode =  query.value(10).toString()

        #  with the latest version of the CLAMS schema, we have a "is_length" column in the
        #  measurements table that is set to 1 for "length" measurements which allows us
        #  to query all of the length measurements regardless of their name. First we build
        #  a list of all length types.
        len_list=[]
        query = QtSql.QSqlQuery("SELECT measurement_type FROM measurement_types WHERE " +
                "is_length=1")
        while query.next():
            len_list.append(str(query.value(0).toString()))

        # When the length type is changed in the combo box, only the specimens with that
        # length type are shown in the table, therefore, the only option for length type
        #  selected is the one currently active in the combo box- query using that type
        if self.lengthTypeBox.isEnabled():
            lengthType=str(self.lengthTypeBox.currentText())
            query = QtSql.QSqlQuery("SELECT lower(measurement_type), measurement_value from measurements WHERE " +
                "measurement_type = '"+lengthType+"' AND survey=" + self.survey +
                " AND ship="+self.ship+" AND specimen_id="+self.specimenKey)
            query.first()
            length=query.value(1).toString()
            #  now build the length string to print
            if lengthType in len_list:
                ind=lengthType.find('_')+1
                if ind!=0:
                    lt=lengthType[0].upper()+lengthType[ind].upper()
                else:
                    # This case is for length types without an underscore, which doesn't happen now but might in the future
                    lt=lengthType[0].upper()+lengthType[1].upper()
        else:
            # Just stick the first length type (from protocol) value on the label in the length section, if it exists (if not, NaN)
            length='NaN'
            for lengthType in self.measureType:
                if lengthType in len_list:
                    lengthType=str(lengthType)
                    query = QtSql.QSqlQuery("SELECT lower(measurement_type), measurement_value from measurements WHERE " +
                        "measurement_type = '"+lengthType+"' AND survey=" + self.survey +
                        " AND ship="+self.ship+" AND specimen_id="+self.specimenKey)
                    query.first()
                    length=query.value(1).toString()
                    ind=lengthType.find('_')+1
                    if ind!=0:
                        lt=lengthType[0].upper()+lengthType[ind].upper()
                    else:
                        # This case is for length types without an underscore, which doesn't happen now but might in the future
                        # Just take first two letter of length type word
                        lt=lengthType[0].upper()+lengthType[1].upper()
                    break


        length = length + ' ' + lt

        #create dictionary
        data={'title':'NOAA/AFSC/RACE/MACE',
              'ship':vessel,
              'survey':survey,
              'haul':haul,
              'specimen_id':spec_id,
              'species_code':code,
              'common_name':name,
              'length':length,
              'weight':weight,
              'sex':sex,
              'maturity_table':self.maturityTable,
              'maturity_key':maturity,
              'scientist':scientist,
              'otolith':barcode
              }

        #  print the label
        self.printer.printSpecialSampleLabel1(data)

        # print sound
        if self.printSound:
            self.printSound.play()


    def getComment(self):
        '''
        getComment displays the comment dialog then "cleans" the comment string and inserts
        it into the database.
        '''

        keyDialog = keypad.KeyPad(self.comment, self)
        keyDialog.exec_()
        if keyDialog.okFlag:
            #  get the comment string
            commentString = keyDialog.dispEdit.toPlainText()
            self.comment = commentString

            #  clean string by removing newline chars and replacing with a space
            commentString = commentString.split('\n')
            newString = ''
            for c in commentString:
                newString = newString + c + ' '

            # insert comment into sample
            query =QtSql.QSqlQuery("UPDATE specimen SET comments='" + newString +
                    "' WHERE ship="+self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                    " AND specimen_id = " + self.specimenKey)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + ", " +
                                 query.lastQuery())


    def editSamplingMethod(self):
        # user toggles in sample flag - have to update data
        if self.editStateFlag:
            query = QtSql.QSqlQuery("UPDATE specimen SET sampling_method =" + self.samplingMethodBox.currentText() +
                    " WHERE ship="+self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                    " AND specimen_id = "+self.specimenKey)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + ", " +
                                 query.lastQuery())


    def goExit(self):
        self.close()


    def closeEvent(self, event):
        if self.activeSpcCode and self.specimenKey: # there's already some collections made
            self.getNext()
            if self.incomplete:
                event.ignore()
                return

        event.accept()




