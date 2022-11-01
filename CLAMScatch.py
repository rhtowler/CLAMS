
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_CLAMSCatch
import addcatchspcdlg_multimix
import numpad
import typeseldialog
import basketeditdlg
import keypad
import transferdlg
import messagedlg
import QZebraPrinter
import addspecdlg

class CLAMSCatch(QDialog, ui_CLAMSCatch.Ui_clamsCatch):

    def __init__(self, parent=None):
        super(CLAMSCatch, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.db=parent.db
        self.serMonitor=parent.serMonitor
        if not self.db.isOpen():
            self.db.open()
        self.workStation=parent.workStation
        self.activeHaul=parent.activeHaul
        self.survey=parent.survey
        self.ship=parent.ship
        self.settings=parent.settings
        self.activePartition=parent.activePartition
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.backLogger=parent.backLogger
        self.scientist=parent.scientist
        self.sciLabel.setText(self.scientist)
        self.activeSampleKey=None
        p=self.scientist.split(' ')
        self.firstName=p[0]
        self.message=messagedlg.MessageDlg(self)

        # get sample types
        query=QtSql.QSqlQuery("SELECT gear_options.basket_type FROM gear_options INNER JOIN " +
                "events ON gear_options.gear=events.gear WHERE events.ship="+self.ship+
                " AND events.survey="+self.survey+" AND events.event_id="+self.activeHaul+
                " AND gear_options.basket_type is not NULL ORDER BY gear_options.basket_type")
        self.basketTypes=[]
        while query.next(): # populate types list
            self.basketTypes.append(query.value(0).toString())

        #get special plankton treatment
        query=QtSql.QSqlQuery("SELECT GEAR.GEAR_TYPE FROM events, GEAR WHERE (events.GEAR = "+
                "GEAR.GEAR ) and  ((events.SHIP = "+self.ship+" ) AND (events.SURVEY = "+
                self.survey+" ) AND (events.event_id = "+self.activeHaul+") )")
        query.first() # populate types list
        self.planktonFlag=False
        if query.value(0).toString()=='PlanktonNet':
            self.planktonFlag=True

        # set up tables for data display
        font=QFont('helvetica', 14, -1, False)
        self.basketView.setFont(font)
        self.basketModel = QtSql.QSqlQueryModel()
        self.basketView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.basketView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.basketView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.basketView.setModel(self.basketModel)
        self.selModel=QItemSelectionModel(self.basketModel, self.basketView)
        self.basketView.setSelectionModel(self.selModel)
        self.basketView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.basketView.show()

        # set up dialog windows
        self.numpad = numpad.NumPad(self)

        self.addspec=addspecdlg.addspecedlg(self)
        self.addspec_flag = True
        self.typeDlg=typeseldialog.TypeSelDialog(self)

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
            self.printBtn.setEnabled(False)

        query=QtSql.QSqlQuery("select a.parameter_value " +
                                            "from device_configuration a, devices b " +
                                            "where a.device_id=b.device_id " +
                                            "and b.device_name='Label_Printer' "+
                                            "and a.device_parameter='SoundFile'")
        if query.first():
            self.printSound=QSound(self.settings[QString('SoundsDir')] + '/' + query.value(0).toString() +'.wav')
        else:
            self.printSound = None

        # initialize variables
        self.activeSpcName=None
        self.activeSpcCode=None
        self.comment=''
        self.validList=[1, 1, 1]# sets valid sample type choices
        self.freeze=False
        self.whHaulFlag=False
        self.devices=[]
        self.manualDevice='0'
        self.parentSamples={}
        self.mixtureNames={'100000':'WholeHaul', '100001':'SortingTable', '100002':'Mix1', '100003':'SubMix1', '100004':'Mix2'}
        # set up window position
        screen=QDesktopWidget().screenGeometry()
        window=self.geometry()
        self.setGeometry((screen.width()-window.width())/2,parent.windowAnchor[0]+(parent.windowAnchor[1]-window.height()), window.width(), window.height())
        self.setMinimumSize(window.width(), window.height())
        self.setMaximumSize(window.width(), window.height())
        # set up tables
        self.sumTable.setColumnWidth(0, 100)
        self.sumTable.setColumnWidth(1, 100)

        # setup parent sample
        self.wholeHaulKey=None
        # if not present, create whole catch sample - top level sample with no parent
        query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship="+self.ship+" AND survey="+
                self.survey+" AND event_id="+self.activeHaul+" AND partition ='"+self.activePartition+
                "' AND species_code=100001")
        if not query.first():
            query =QtSql.QSqlQuery("INSERT INTO samples (ship, survey, event_id, partition, " +
                    "sample_type,species_code, scientist) VALUES("+self.ship+","+self.survey+","+self.activeHaul+
                    ",'"+self.activePartition+"','SortingTable',100001,'"+self.scientist+"')")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # retrieve newly created sample key from database
            query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                    " AND partition ='"+self.activePartition+"' AND species_code=100001")
            query.first()

        self.sortingTableKey=query.value(0).toString()
        # is this a splitter?  if so create whole haul parent key
        query=QtSql.QSqlQuery("SELECT event_data.PARAMETER_VALUE FROM event_data  WHERE " +
                "(event_data.SHIP="+self.ship+") AND (event_data.SURVEY="+self.survey+
                ") AND (event_data.event_id="+self.activeHaul+") AND "+
                "(event_data.PARTITION='"+self.activePartition+"') AND "+
                "(event_data.event_parameter='PartitionWeightType')")
        if query.first():
            if not query.value(0).toString()=='not_subsampled':
                # create whole haul sample - top level sample if needed
                query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship="+self.ship+
                        " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                        " AND partition ='"+self.activePartition+"' AND species_code=100000")
                if not query.first():# we dont already have this sample id- first time in
                    query =QtSql.QSqlQuery("INSERT INTO samples (ship, survey, event_id, partition, " +
                            " sample_type, species_code,scientist) VALUES("+self.ship+","+self.survey+
                            ","+self.activeHaul+",'"+self.activePartition+"'"+
                            ",'WholeHaul',100000, '"+self.scientist+"')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                    # retrieve newly created sample key from database
                    query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship="+self.ship+
                            " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                            " AND partition ='"+self.activePartition+"' AND species_code=100000")

                    query.first()
                self.wholeHaulKey=query.value(0).toString()
                # update parent key for 'sorting table' sample
                query=QtSql.QSqlQuery("UPDATE samples SET parent_sample="+self.wholeHaulKey+" WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                    " AND partition ='"+self.activePartition+"' AND species_code=100001")
                self.whHaulFlag=True
            else:
                self.whHaulFlag=False
        else:
            self.whHaulFlag=False

        # the slots
        self.connect(self.addspcBtn, SIGNAL("clicked()"), self.getSpecies)
        self.connect(self.manualBtn, SIGNAL("clicked()"), self.getManual)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)
        self.connect(self.delBtn, SIGNAL("clicked()"), self.goDelete)
        self.connect(self.printBtn, SIGNAL("clicked()"), self.printLabel)
        self.connect(self.editBtn, SIGNAL("clicked()"), self.editTable)
        self.connect(self.speciesList, SIGNAL("itemSelectionChanged()"), self.getActiveSpc)
        self.connect(self.speciesList, SIGNAL("itemActivated()"), self.getSpeciesFocus)
        self.connect(self.selModel, SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.getBasketRow)
        self.connect(self.serMonitor, SIGNAL("SerialDataReceived"), self.getAuto)
        self.connect(self.transBtn, SIGNAL("clicked()"), self.transferSample)
        self.connect(self.commentBtn, SIGNAL("clicked()"), self.getComment)
        
        # set up serial connections
        self.openSerial()
        self.reloadSpeciesList()
        self.spcDlg = addcatchspcdlg_multimix.AddCatchSpcDlg(self)
        self.connect(self.spcDlg, SIGNAL("changed"), self.addSpecies)

        self.updateParentKeys()
        
        checkHaulTimer = QTimer(self)
        checkHaulTimer.setSingleShot(True)
        self.connect(checkHaulTimer, SIGNAL("timeout()"), self.checkHaulIsDone)
        checkHaulTimer.start(1)


    def checkHaulIsDone(self):
            # check to see if haul form has been checked for codend partition
        if self.activePartition=='Codend':
            query=QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeHaul+
                " AND partition='Codend' AND event_parameter='PartitionWeightType'")
            if not query.first():# haul form has not been entered yet!!
                self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                        "You need to visit haul form before you can enter codend catch.",'info')
                self.message.exec_()
                self.close()
                return


    def getSpecies(self):
        self.freeze=True
        self.spcDlg.exec_()
        self.freeze=False


    def addSpecies(self):
        self.addspec_flag = False
        code=str(self.spcDlg.activeSpcCode)
        spcName=str(self.spcDlg.activeSpcName)
        subCat=str(self.spcDlg.activeSpcSubcat)
        # parent sample
        parentKey  = self.parentSamples[self.spcDlg.parentSample]
        self.createSample(code, spcName, subCat,  self.spcDlg.nameType,  parentKey)
        #
        self.updateParentKeys()
        # are we creating a mix sample? Need the parent key for species in mix...

        # make this new addition the active one...
        self.reloadSpeciesList()
        #self.setActiveSpecies(spcName, subCat)
        self.addspec_flag = True


    def updateParentKeys(self):
        for code in ['100002', '100003', '100004']:# these are the mix codes
            query=QtSql.QSqlQuery("SELECT species.common_name, samples.sample_id  " +
                "  FROM samples, species WHERE species.species_code=samples.species_code " +
                " AND samples.species_code ="+code+" AND samples.ship=" + self.ship + " AND samples.survey=" + self.survey + " AND samples.event_id = " +
                self.activeHaul + " AND samples.partition='" + self.activePartition + "'")
            if query.first():# we have a mix
                spcName=query.value(0).toString()
                parentKey=query.value(1).toString()
                if not parentKey in self.parentSamples:
                    self.parentSamples.update({spcName:parentKey})
        if not self.wholeHaulKey in self.parentSamples:
            self.parentSamples.update({QString('WholeHaul'):self.wholeHaulKey})
        if not self.sortingTableKey in self.parentSamples:
            self.parentSamples.update({QString('SortingTable'):self.sortingTableKey})


    def createSample(self,  code, name, subCat,  nameType,   parentSample):
        # check whether is already in list
        if subCat<>'None':
            if self.speciesList.findItems(name+"-"+subCat, Qt.MatchExactly):
                return
        else:
            if self.speciesList.findItems(name, Qt.MatchExactly):
                return
        if code in ('100002', '100003', '100004'):
            sampleType=self.mixtureNames[code]
        else:
            sampleType='Species'
        query =QtSql.QSqlQuery("INSERT INTO samples (ship, survey, event_id, partition, sample_type, species_code, subcategory, parent_sample, scientist) VALUES("+self.ship+","+self.survey+","+
                                    self.activeHaul+",'"+self.activePartition+"','"+sampleType+"',"+code+",'"+subCat+"',"+parentSample+",'"+self.scientist+"')")
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
        query =QtSql.QSqlQuery("SELECT max(sample_id) FROM samples WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+
                                              self.activeHaul+" AND partition ='"+self.activePartition+"'")
        query.first()
        query1 =QtSql.QSqlQuery("INSERT INTO sample_data (ship, survey, event_id, sample_id, sample_parameter, parameter_value) VALUES("+self.ship+","+self.survey+","+
                                    self.activeHaul+","+query.value(0).toString()+",'sample_name','"+nameType+"')")
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query1.lastQuery())


    def setActiveSpecies(self, spc_name, subcat):
        # this is for programattically setting active species
        
        if subcat=='None':
            spc_tag=spc_name
        else:
            spc_tag=spc_name+"_"+subcat

        self.speciesList.setCurrentItem(spc_tag, Qt.MatchExactly)
        self.activeSpcSubcat=subcat
        self.activeSpcName=spc_name
        self.activeSampleKey=self.speciesList.verticalHeaderItem(self.speciesList.currentRow()).text()
        self.activeSpcCode=self.speciesDict[str(self.activeSpcName)]
        # look for previous data on species
        self.updateTables()
        self.focus='speciesList'
        # set up picture
        if self.activeSpcSubcat<>'None':
            imgName=self.activeSpcCode+"_"+self.activeSpcSubcat
        else:
            imgName=self.activeSpcCode
        pic=QImage()
        if pic.load(self.settings[QString('ImageDir')]+'\\fishPics\\'+imgName+".jpg"):
            pic=pic.scaled(self.picLabel.size(),Qt.KeepAspectRatio)#,  Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(pic))
            self.picLabel.setAlignment(Qt.AlignHCenter)
            self.picLabel.setAlignment(Qt.AlignVCenter)
        else:
             self.picLabel.clear()
        if self.speciesList.item(self.speciesList.currentRow(), 1).text()=='mix1':
            self.inMixFlag=True
        else:
            self.inMixFlag=False
        query=QtSql.QSqlQuery("SELECT comments FROM samples WHERE (ship = "+self.ship+" and survey = "+self.survey+" and event_id = "+self.activeHaul+" and sample_id = "+self.activeSampleKey+")")
        if query.first():
            self.comment=query.value(0).toString()


    def checkSampleExists(self,  sampID):
        '''
        checkSampleExists checks if the sample ID is still present in the database. Returns
        True if so, and False if not.
        '''
        query =QtSql.QSqlQuery("SELECT sample_id from samples WHERE ship = "+self.ship+
                " AND survey = "+self.survey+" AND event_id = "+self.activeHaul+
                " AND sample_id = "+sampID)
        if query.first():
            return True
        else:
            return False


    def getActiveSpc(self):
        self.basketView.setEnabled(True)
        self.sumTable.setEnabled(True)
        
        # default setting for a species is no whole haul
        if self.speciesList.currentRow()<0:# no species left, for deleting purposes
            return
        text=str(self.speciesList.item(self.speciesList.currentRow(), 0).text())
        
        #  check to make sure this sample still exists - stations can get out of sync with the samples
        #  list if someone deletes a sample at a different station after someone opens this form.
        sampID = self.speciesList.verticalHeaderItem(self.speciesList.currentRow()).text()
        ok = self.checkSampleExists(sampID)
        if not ok:
            #  this sample has been deleted - inform the user and remove from the list
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                        "The sample you selected has been deleted by someone else. " + 
                        "You must re-add it using the Catch module if you need it.",'info')
            self.message.exec_()
            #  refresh the species list
            self.reloadSpeciesList()
            return

        # New dialog for confirming active species
        if self.addspec_flag == True:
            self.freeze=True
            self.addspec.setMessage(self.errorIcons[1], self.errorSounds[2],
                    "Changing the Active Species to: \n \n"+ text ,'info')
            self.addspec.exec_()
            self.freeze=False
        text1=text.split('-')
        if len(text1)>1:# this species has subcategory
            self.activeSpcSubcat=text1[-1]
            self.activeSpcName='-'.join(text1[0:-1])
        else:
            self.activeSpcSubcat='None'
            self.activeSpcName=text1[0]
        self.activeSampleKey=self.speciesList.verticalHeaderItem(self.speciesList.currentRow()).text()
        self.activeSpcCode=self.speciesDict[str(self.activeSpcName)]
        
        # look for previous data on species
        self.updateTables()
        self.focus='speciesList'
        # set up picture
        if self.activeSpcSubcat<>'None':
            imgName=self.activeSpcCode+"_"+self.activeSpcSubcat
        else:
            imgName=self.activeSpcCode
        pic=QImage()
        if pic.load(self.settings[QString('ImageDir')]+'\\fishPics\\'+imgName+".jpg"):
            pic=pic.scaled(self.picLabel.size(),Qt.KeepAspectRatio)#,  Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(pic))
            self.picLabel.setAlignment(Qt.AlignHCenter)
            self.picLabel.setAlignment(Qt.AlignVCenter)
        else:
             self.picLabel.clear()
        if self.speciesList.item(self.speciesList.currentRow(), 1).text()=='mix1':
            self.inMixFlag=True
        else:
            self.inMixFlag=False
        query=QtSql.QSqlQuery("SELECT comments FROM samples WHERE (ship = "+self.ship+" and survey = "+self.survey+" and event_id = "+self.activeHaul+" and sample_id = "+self.activeSampleKey+")")
        if query.first():
            self.comment=query.value(0).toString()

    def getManual(self):
                # is a species selected
        if self.activeSpcName==None:
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2], self.firstName +
                    ", please select a species.",'info')
            self.message.exec_()
            return

        self.numpad.msgLabel.setText("Punch in the Weight")
        if not self.numpad.exec_():
            return

        #  check that we didn't get a 0 weight
        if (self.numpad.value == 0):
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2], "You have entered 0 (zero) "
                    "for the basket weight which is not allowed. If your sample is too small to register " +
                    "on the scale, you should enter 0.001", 'info')
            self.message.exec_()
            return

        self.currentBasketWt=self.numpad.value
        self.manualFlag=True
        self.device=self.manualDevice # manual input key
        self.updateBasket()


    def getAuto(self, device, val):
        # check if we're working on a previous weight
        if self.freeze:
            return
        if not device in self.devices:
            return
        # check if a species is selected
        if self.activeSpcName==None:
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2],self.firstName+", please select a species.",'info')
            self.message.exec_()
            return

        #  check that we didn't get a 0 weight
        if (val <= 0):
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2], "The scale sent a weight of 0 (zero) "
                    "which is not allowed. If your sample is too small to register " +
                    "on the scale, you should manually enter 0.001", 'info')
            self.message.exec_()
            return

        self.manualFlag = False
        self.currentBasketWt = val
        self.device = device
        self.sounds[self.devices.index(self.device)].play()
        self.updateBasket()


    def getWeightValidation(self):
        self.valFlag=True
        self.freeze=True
        # CHECK BASKET WEIGHT AGAINST MAXIMUM
        if float(self.currentBasketWt)>float(self.settings[QString('MaxBasketWt')]):
            self.message.setMessage(self.errorIcons[1],self.errorSounds[1], self.firstName+", this Basket exceeds the maximum basket weight of "+self.settings[QString('MaxBasketWt')]+".  Does this bother you?", 'choice')
            if self.message.exec_():
                self.valFlag=False
                return


        #  check for mix subsample weight and stuff
        if self.inMixFlag: #there's mix
            (mixSubWeight, mixSpeciesWeight)=self.mixValidation()

            # validation for mix sub weight - can't have more weight in sub part of mix than in mix subsample
            if mixSubWeight*(1+float(self.settings[QString('MaxMixDev')])/100)<(mixSpeciesWeight+float(self.currentBasketWt)):
                    self.message.setMessage(self.errorIcons[0],self.errorSounds[0],self.firstName+", it appears that the total weight of species in the mix exceeds the mix subsample by more than "+
                    self.settings[QString('MaxMixDev')]+" % - i.e. not good.  Do you want to fix this now?",'info')
                    if self.message.exec_():
                        self.valFlag=False
                        return


    def getBasketType(self):
        if self.activeSpcCode in ['100002', '100003', '100004']:# turn off count sample type for mixes
            self.validList[self.basketTypes.index('Count')]=0
        else:
            self.validList[self.basketTypes.index('Count')]=1

        self.typeDlg.buttonSetup(self.validList)
        if self.typeDlg.exec_():
            self.basketType=self.typeDlg.basketType
            self.count=self.typeDlg.count
        else:
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2],"You didn't choose a Basket type, you bugger",'info')
            self.message.exec_()
            self.basketType=None

    def updateBasket(self):

        #  set the "freeze" flag so we ignore input from the scale while we're finishing this basket
        self.freeze = True
        #  ensure that we have a connection to the db
        #  THIS CHECK SHOULDN'T BE HERE -
        if not self.db.isOpen():
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2],"Database is not connected - restart clams",'info')
            self.message.exec_()
            self.freeze = False
            return
        #  run the weight validation
        self.getWeightValidation()
        if not self.valFlag:
            #  this weight is not valid
            self.freeze = False
            return
        #  get the sample type
        self.getBasketType()
        if (self.basketType == None):
            #  user cancelled sample type selection
            self.freeze = False
            return
        #  insert data into db
        if self.count==None:
            query =QtSql.QSqlQuery("INSERT INTO baskets (ship, survey, event_id, sample_id, basket_type,  weight, device_id) VALUES ("+
                        self.ship+", "+self.survey+","+self.activeHaul+","+self.activeSampleKey+",'"+self.basketType+"',"+self.currentBasketWt+","+self.device+")")
        else:# write basket record
            query =QtSql.QSqlQuery("INSERT INTO baskets (ship, survey, event_id, sample_id, basket_type, count, weight, device_id) VALUES ("+
                        self.ship+", "+self.survey+","+self.activeHaul+","+self.activeSampleKey+",'"+self.basketType+"',"+self.count+","+self.currentBasketWt+","+self.device+")")

        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
        # update the GUI
        self.updateTables()
        #  we're done with this basket - unfreeze
        self.freeze = False

    def updateTables(self):
        self.basketModel.setQuery("SELECT basket_id, weight, count, basket_type FROM baskets WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND sample_id ="+
                                  self.activeSampleKey+" ORDER BY basket_id", self.db)
        self.basketModel.reset()
        self.basketView.scrollToBottom()
        self.basketView.resizeColumnsToContents()
        self.updateSumTable()

    def updateSumTable(self):
        self.sumTable.clearContents()
        self.sumTable.setRowCount(0)
        for i in range(3):
            self.sumTable.setVerticalHeaderItem(i, QTableWidgetItem(""))
        # get counts per basket type
        query=QtSql.QSqlQuery("SELECT sum(WEIGHT), count(weight), basket_type FROM BASKETS "+
        " WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND sample_id="+self.activeSampleKey+" GROUP BY basket_type")
        cnt=0
        totWt=0
        totCnt=0
        while query.next():
            self.sumTable.insertRow(cnt)
            self.sumTable.setVerticalHeaderItem(cnt,QTableWidgetItem(query.value(2).toString()))
            self.sumTable.setItem(cnt, 0, QTableWidgetItem(query.value(0).toString()))
            self.sumTable.setItem(cnt, 1, QTableWidgetItem(query.value(1).toString()))
            cnt+=1
            totWt=totWt+float(query.value(0).toString())
            totCnt=totCnt+float(query.value(1).toString())
        # get total
        self.sumTable.insertRow(cnt)
        self.sumTable.setVerticalHeaderItem(cnt,QTableWidgetItem('Total'))
        self.sumTable.setItem(cnt, 0, QTableWidgetItem(str(totWt)))
        self.sumTable.setItem(cnt, 1, QTableWidgetItem(str(totCnt)))
        self.sumTable.resizeColumnsToContents()


    def getSpeciesFocus(self):
        self.focus='speciesList'


    def getBasketRow(self):
        self.focus='basketList'
        self.selRecord=[]
        selObj=self.basketView.currentIndex()
        for i in range(4):
            index= self.basketModel.index(selObj.row(), i, QModelIndex())
            self.selRecord.append(self.basketModel.data(index, Qt.DisplayRole).toString())


    def deleteSpecimen(self):
        """
        deleteSpecimen is called when the user wants to delete a basket or sample and
        specimen exist in the database.
        """

        #  double check that they want to delete the specimen
        self.message.setMessage(self.errorIcons[3],self.errorSounds[1],
                "Are you REALLY sure you want to delete these specimen?", 'choice')
        if self.message.exec_():
            #  they want to do it - delete the measurements
            query=QtSql.QSqlQuery("DELETE FROM measurements WHERE ship=" + self.ship +
                    " AND survey = " + self.survey + " AND event_id=" + self.activeHaul +
                    " AND sample_id ="+ self.activeSampleKey)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            #  delete the specimen records
            query=QtSql.QSqlQuery("DELETE FROM specimen WHERE ship=" + self.ship +
                    " AND survey = " +self.survey + " AND event_id=" + self.activeHaul +
                    " AND sample_id ="+self.activeSampleKey)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            #  try to delete from the catch summary and length histogram tables - these will be
            #  populated at this point if a user has come back into CLAMS to edit a past haul
            query=QtSql.QSqlQuery("DELETE FROM catch_summary WHERE ship=" + self.ship +
                    " AND survey = " +self.survey + " AND event_id=" + self.activeHaul +
                    " AND sample_id ="+self.activeSampleKey)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            query=QtSql.QSqlQuery("DELETE FROM length_histogram WHERE ship=" + self.ship +
                    " AND survey = " +self.survey + " AND event_id=" + self.activeHaul +
                    " AND sample_id ="+self.activeSampleKey)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            #  set the return value to true since we deleted the specimen
            deleted = True

        else:
            #  user changed their mind
            deleted = False

        return deleted


    def goDelete(self):
        """
        goDelete  deletes either baskets or a sample depending on what widget has focus
        (basket list or sample list)
        """

        if self.activeSampleKey==None:
            return

        hasSpecimen=False
        nOther = 0
        nMeasure = 0

        #  first check if we have specimen - this process a bit more complicated with specimen
        query=QtSql.QSqlQuery("SELECT specimen_id FROM specimen WHERE ship="+self.ship+" AND survey="+
                self.survey+" AND event_id="+self.activeHaul+" AND sample_id ="+self.activeSampleKey)
        if query.first():
            # the active species has specimen data
            hasSpecimen=True

        #  determine type and count of baskets for this sample. We need to know this because if
        #  the user is trying to delete the last "measure" basket and there are samples, the
        #  samples have to be deleted too.
        query=QtSql.QSqlQuery("SELECT basket_type FROM baskets WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND sample_id = "
                +self.activeSampleKey)
        while query.next():
            if query.value(0).toString() == 'Measure':
                #  this is a measure basket
                nMeasure = nMeasure + 1
            else:
                #  this is a count, preserve, or toss basket
                nOther = nOther + 1

        #  now move ahead based on where the focus is in the GUI. If a basket is selected, we
        #  attempt to delete that single basket. If a sample is selected, we attempt to delete the
        #  whole sample.

        #  if the focus is on the basket list, delete the selected basket
        if self.focus=='basketList':

            #  if there is only 1 measure basket left and there are specimen, check if the selected
            #  basket is that lone measure basket
            if nMeasure == 1 and hasSpecimen:
                query=QtSql.QSqlQuery("SELECT basket_type FROM baskets WHERE ship="+self.ship+
                        " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND basket_id="+
                        self.selRecord[0])
                if query.value(0).toString() == 'Measure':
                    #  this is the last measure basket and specimen exist
                    self.message.setMessage(self.errorIcons[1],self.errorSounds[1],
                            "This is the last basket of type 'Measure' for this species and specimen " +
                            "exist for this species. If you delete this basket, the specimen will be " +
                            "deleted as well. Are you SURE you want to permanently delete this basket " +
                            "AND all of the specimen collected for this species, "+
                            self.firstName+"?", 'choice')
                    if self.message.exec_():
                        #  user chose to delete the specimen (we'll ask one more time)
                        ok = self.deleteSpecimen()

                        if not ok:
                            #  user changed their mind when we asked if they're sure - we're done here
                            return
                    else:
                        #  user changed their mind - we're done here
                        return

                #  Either this basket wasn't a measure type or it was and we deleted all of the
                #  associated specimen. Now we delete the basket
                query =QtSql.QSqlQuery("DELETE FROM baskets WHERE ship="+self.ship+" AND survey="+
                            self.survey+" AND event_id="+self.activeHaul+" AND basket_id="+
                            self.selRecord[0], self.db)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+
                        query.lastQuery())

            else:
                #  this is not the last measure basket so we just delete the basket regardless of
                #  type and assume the user knows what they are doing

                self.message.setMessage(self.errorIcons[3],self.errorSounds[1], "Are you sure you want " +
                        "to permanently delete this basket, "+self.firstName+"?", 'choice')
                if self.message.exec_():
                    #  user chose to delete
                    query =QtSql.QSqlQuery("DELETE FROM baskets WHERE ship="+self.ship+" AND survey="+
                            self.survey+" AND event_id="+self.activeHaul+" AND basket_id="+
                            self.selRecord[0], self.db)
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+
                            query.lastQuery())

        #  if the focus is on the sample list so we're going to delete the entire sample
        elif self.focus=='speciesList':

            #  make sure the user really wants to do the
            if hasSpecimen:
                #  if there are specimen associated with this sample, we present a different dialog
                #  and then have to first delete the specimen
                self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "There are "+
                        str(nMeasure+nOther)+" basket weights for this species AND you have " +
                        "collected specimen data too. Are SURE you want permanatly delete this "
                        "species and ALL of these baskets and ALL of your specimen data?",'choice')
                if self.message.exec_():
                    #  user chose to delete the everything from this sample so first delete the specimen
                    ok = self.deleteSpecimen()

                    if not ok:
                        #  user changed their mind when we asked if they're sure - we're done here
                        return
            else:
                #  no specimen yet so we present a differently worded dialog. Only present a dialog
                #  if there are baskets though. Otherwise we just delete the sample.
                if nMeasure+nOther > 0:
                    self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "There are "+
                            str(nMeasure+nOther)+" basket weights for this species. " +
                            "Are sure you want to permanantly delete ALL of them?", 'choice')
                    if not self.message.exec_():
                        #  user changed their mind
                        return

                    # kill the baskets
                    query =QtSql.QSqlQuery("DELETE FROM baskets WHERE ship="+self.ship+" AND survey="+
                            self.survey+" AND event_id="+self.activeHaul+" AND sample_id = "+
                            self.activeSampleKey, self.db)
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+
                            query.lastQuery())

                #  try to delete from the catch summary and length histogram tables - these will be
                #  populated at this point if a user has come back into CLAMS to edit a past haul
                #  (depending on the execution path this might have already been done but it doesn't
                #  hurt to try again here.)
                query=QtSql.QSqlQuery("DELETE FROM catch_summary WHERE ship=" + self.ship +
                        " AND survey = " +self.survey + " AND event_id=" + self.activeHaul +
                        " AND sample_id ="+self.activeSampleKey)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                query=QtSql.QSqlQuery("DELETE FROM length_histogram WHERE ship=" + self.ship +
                        " AND survey = " +self.survey + " AND event_id=" + self.activeHaul +
                        " AND sample_id ="+self.activeSampleKey)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

                # delete the sample_data
                query =QtSql.QSqlQuery("DELETE FROM sample_data WHERE ship="+self.ship+" AND survey="+
                        self.survey+" AND event_id="+self.activeHaul+" AND sample_id = "+
                        self.activeSampleKey, self.db)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+
                        query.lastQuery())

                #  and then delete the sample
                query =QtSql.QSqlQuery("DELETE FROM samples WHERE ship="+self.ship+" AND survey="+
                        self.survey+" AND event_id="+self.activeHaul+" AND sample_id = "+
                        self.activeSampleKey, self.db)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+
                        ","+query.lastQuery())

            #  refresh the species list
            self.reloadSpeciesList()

        #  update the tables
        self.updateTables()


    def transferSample(self):
        self.freeze=True
        transDlg = transferdlg.TransferDlg(self)
        if not transDlg.exec_():# user cancelled action
            self.freeze=False
            return
        # write basket record
        if transDlg.fromType=='Count':
            count=str(-transDlg.transCount)
        else:
            count='NULL'
        query =QtSql.QSqlQuery("INSERT INTO baskets (ship, survey, event_id, sample_id, basket_type, count, weight, device_id) VALUES ("+
                    self.ship+", "+self.survey+","+self.activeHaul+","+transDlg.fromSampleKey+",'"+transDlg.fromType+"',"+count+","+str(-transDlg.transWeight)+","+
                    transDlg.transDevice+")",  self.db)

        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
        if transDlg.toType=='Count':
            count=str(transDlg.transCount)
        else:
            count='NULL'

        query =QtSql.QSqlQuery("INSERT INTO baskets (ship, survey, event_id, sample_id, basket_type, count, weight, device_id) VALUES ("+
                self.ship+", "+self.survey+","+self.activeHaul+","+transDlg.toSampleKey+",'"+transDlg.toType+"',"+count+","+str(transDlg.transWeight)+","+
                transDlg.transDevice+")",  self.db)
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
        self.activeSampleKey=transDlg.toSampleKey
        # update basket table
        self.updateTables()
        self.freeze=False

    def editTable(self):
        pass
        self.freeze=True
        if self.activeSpcName=='mix1':# turn off count sample type for mixes
            self.validList[self.basketTypes.index('Count')]=0
        else:
            self.validList[self.basketTypes.index('Count')]=1

        self.typeDlg.buttonSetup(self.validList)

        columns=self.basketModel.columnCount(QModelIndex())
        row=self.basketView.currentIndex().row()
        if (row == -1):
            self.message.setMessage(self.errorIcons[2], self.errorSounds[1], "Please select a basket to edit " + self.firstName,'info')
            self.message.exec_()
            self.freeze = False
            return
        self.getBasketRow()
        header=['BASKET_ID','WEIGHT', 'COUNT', 'SAMPLE_TYPE' ]
        items=self.selRecord

        editDlg = basketeditdlg.BasketEditDlg(header,  items,  self)
        editDlg.exec_()
        if not editDlg.okFlag:# user cancelled action
            return
        # update database
        if editDlg.count=='-':
            editDlg.count='NULL'
        # update basket table
        query =QtSql.QSqlQuery("UPDATE baskets SET basket_type='"+editDlg.basketType+"', count = "+
                editDlg.count+", weight = "+editDlg.weight+"  WHERE ship="+self.ship+" AND survey="+self.survey+
                " AND event_id="+self.activeHaul+" AND sample_id = "+self.activeSampleKey+" AND basket_id = "+
                self.selRecord[0], self.db)
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

        self.freeze=False
        self.updateTables()


    def exitValidation(self):
        self.returnFlag=False
        for mixcode in ['100002', '100003', '100004']:
            query=QtSql.QSqlQuery("SELECT * FROM samples WHERE ship="+self.ship+" AND survey="+
                    self.survey+" AND event_id = "+self.activeHaul+" AND partition='"+
                    self.activePartition+"' AND species_code="+mixcode)
            if query.first():# there been a mix collected
                # mix validation
                (mixSubWeight, mixSpeciesWeight)=self.mixValidation(mixcode)
                if mixSubWeight==0:
                    self.message.setMessage(self.errorIcons[1],self.errorSounds[1], self.firstName+
                            ", there's no mix basket subsample weight for "+self.mixtureNames[mixcode]+" in the system.  Go do it now.", 'info')
                    self.message.exec_()
                    self.returnFlag=True
                    return

                #  check the mix parts more or less make up the weight of the total
                dev = (mixSubWeight - mixSpeciesWeight) / mixSubWeight * 100.
                #  check that the deviation is below the allowed value
                if (abs(dev) > float(self.settings[QString('MaxMixDev')])):
                    #  it is not, issue a warning and ask user what they want to do
                    self.message.setMessage(self.errorIcons[2], self.errorSounds[1], self.firstName+
                            ", the weight of the mix components is more or less than "+ str(dev) +
                            " % of the mix subsample weight for  "+self.mixtureNames[mixcode]+". Does this bother you? ", 'choice')
                    if self.message.exec_():
                        #  user is bothered by this - set the failed validation flag
                        self.returnFlag=True
                    else:
                        if mixcode in self.parentSamples:
                            #  user doesn't care, make note of this and move on
                            QtSql.QSqlQuery("INSERT INTO override (scientist, record_id, " +
                                    "table_name,description) VALUES ('" + self.scientist + "'," +
                                    self.parentSamples[mixcode] + ",'sample', 'mix components are "+str(dev)+
                                    " % less than the mix subsample weight')")

        # closing  validation - get species in list

        query=QtSql.QSqlQuery("SELECT species.common_name, samples.sample_id, samples.species_code, " +
                "samples.subcategory  FROM samples, species WHERE species.species_code=samples.species_code " +
                " AND samples.sample_type in ('Mix1','SubMix1','Mix2','Species') AND samples.ship=" + self.ship + " AND samples.survey=" + self.survey + " AND samples.event_id = " +
                self.activeHaul + " AND samples.partition='" + self.activePartition + "'")
        while query.next():
            query1 = QtSql.QSqlQuery("SELECT * FROM baskets WHERE ship="+self.ship+" AND survey="+
                    self.survey+" AND event_id = "+self.activeHaul+" AND sample_id = "+
                    query.value(1).toString())

            if not query1.next(): # no baskets for this species
                if query.value(3).toString()<>'None':
                    spcName=query.value(0).toString()+" "+query.value(3).toString()
                else:
                    spcName=query.value(0).toString()
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1], "My dear "+self.firstName+
                        ", There are are no basket weights for "+spcName+". Does this bother you?", 'choice')
                if self.message.exec_():
                        self.returnFlag=True
                        return
                # we're commenting this out because its caousing problems with multi catch input
#                    else:
#                        # remove stray sample record
#                        query =QtSql.QSqlQuery("DELETE FROM samples WHERE ship="+self.ship+" AND survey="+
#                                        self.survey+" AND event_id = "+self.activeHaul+" AND sample_id = "+query.value(1).toString(),  self.db)
#                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())


    def mixValidation(self,  mixcode):
        # validation #2 mix sub weight vs species in it
        mixSubWeight=0
        #get mix sample key
        query = QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE samples.species_code="+mixcode+" AND ship="+self.ship+" AND survey="+
                                        self.survey+" AND event_id = "+self.activeHaul+" AND partition='"+self.activePartition+"'")
        if query.first():# there is a mix on this tow
            mixKey=query.value(0).toString()
            query1 = QtSql.QSqlQuery("SELECT Sum(weight) FROM baskets WHERE ship="+self.ship+" AND survey="+
                                        self.survey+" AND event_id = "+self.activeHaul+" AND sample_id="+mixKey+
            " AND basket_type = 'Measure'")
            # check for a mix subsample weight
            query1.first()
            mixSubWeight=(float(query1.value(0).toString()))
        else: #there's no mix
            return

        mixSpeciesWeight=0
        query = QtSql.QSqlQuery("SELECT Sum(baskets.weight) FROM samples, baskets WHERE samples.sample_id = "+
        "baskets.sample_id AND samples.ship=baskets.ship AND samples.survey=baskets.survey AND samples.event_id=baskets.event_id AND samples.ship="+self.ship+" AND samples.survey="+
        self.survey+" AND samples.event_id="+self.activeHaul+" AND samples.partition='"+self.activePartition+"' AND samples.parent_sample="+mixKey)# check for a mix subsample weight
        if query.first():
            mixSpeciesWeight=(float(query.value(0).toString()))

        return mixSubWeight, mixSpeciesWeight



    def reloadSpeciesList(self):

        #  disconnect the selection changed signal so we don't trigger it when the list is
        #  cleared.
        self.disconnect(self.speciesList, SIGNAL("itemSelectionChanged()"), self.getActiveSpc)

        # add just species
        self.speciesList.clearContents()
        self.speciesList.setRowCount(0)
        self.speciesDict={}

        # get species involved
        query=QtSql.QSqlQuery("SELECT samples.sample_id, species.common_name, species.scientific_name," +
                "species.species_code, samples.parent_sample, samples.subcategory"+
                " FROM samples, species WHERE samples.species_code=species.species_code AND " +
                "samples.ship="+self.ship+" AND samples.survey="+
        self.survey+" AND samples.event_id="+self.activeHaul+" AND samples.partition='"+
                self.activePartition+"' AND samples.species_code not in (100000,100001) ORDER BY samples.sample_id ASC")
        cnt=0
        while query.next():
            #get the namespace
            query0=QtSql.QSqlQuery("SELECT PARAMETER_VALUE FROM sample_data WHERE sample_parameter=" +
                    "'sample_name' AND  sample_id="+ query.value(0).toString())
            if query0.first():
                if query0.value(0).toString()=='scientific':
                    species=query.value(2).toString()
                else:
                    species=query.value(1).toString()
            else:
                species=query.value(1).toString()
            subcat=query.value(5).toString()
            if subcat<>'None':
                name=species+'-'+subcat
            else:
                name=species
            # what's the parent sample Name

            query1=QtSql.QSqlQuery("SELECT b.common_name FROM samples a JOIN species b ON a.species_code=b.species_code WHERE a.ship="+self.ship+" AND a.survey="+
                    self.survey+" AND a.event_id = "+self.activeHaul+" AND a.sample_id="+query.value(4).toString() + "")
            if query1.first():
                myParent=query1.value(0).toString()
            else:
                myParent=''
            self.speciesList.insertRow(cnt)
            self.speciesList.setVerticalHeaderItem(cnt,QTableWidgetItem(query.value(0).toString()))
            self.speciesList.setItem(cnt, 0, QTableWidgetItem(name))
            self.speciesList.setItem(cnt, 1, QTableWidgetItem(myParent))
            cnt=cnt+1
            self.speciesDict.update({str(species):str(query.value(3).toString())})
        self.speciesList.resizeColumnsToContents()
        self.picLabel.clear()

        #  reconnect the selection changed signal now that we're done changing the list
        self.connect(self.speciesList, SIGNAL("itemSelectionChanged()"), self.getActiveSpc)
        self.speciesList.scrollToBottom()

    def openSerial(self):
        query = QtSql.QSqlQuery("SELECT measurement_setup.device_id, device_configuration.parameter_value FROM " +
                                "device_configuration INNER JOIN measurement_setup ON device_configuration.device_id " +
                                "= measurement_setup.device_id WHERE measurement_setup.workstation_id=" +
                                self.workStation+" AND measurement_setup.gui_module='Catch' AND " +
                                "device_configuration.device_parameter = 'SoundFile'")
        self.devices = []
        self.sounds = []
        while query.next():
            self.devices.append(query.value(0).toString())
            self.sounds.append(QSound(self.settings[QString('SoundsDir')] +
                    '\\'+ query.value(1).toString() + '.wav'))


    def printLabel(self):
        '''
            printLabel prints a label for whole fish samples
        '''

        #  ensure that a species is selcted
        if (self.activeSpcName == None):
            #  no species selected - show error dialog
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2], "Hey " + self.firstName +
                                    " pick a species. Duh, even I know that.", 'info')
            self.message.exec_()
            return
        else:

            # get species code from db
            speciesCode = self.activeSpcCode=self.speciesDict[str(self.activeSpcName)]

            #get eq_time
            query=QtSql.QSqlQuery("SELECT event_data.PARAMETER_VALUE FROM event_data  WHERE " +
                "(event_data.SHIP="+self.ship+") AND (event_data.SURVEY="+self.survey+
                ") AND (event_data.event_id="+self.activeHaul+") AND "+
                "(event_data.PARTITION='"+self.activePartition+"') AND "+
                "(event_data.event_parameter='EQ')")
            if query.first():
                EQDateTime = query.value(0).toString()
                EQDate = EQDateTime.split(' ')[0]
            else:
                EQDate = ''


            #  ask how many fish are being frozen
            self.numpad.msgLabel.setText("How many " + self.activeSpcName + " are you freezing?")
            if not self.numpad.exec_():
                return
            number = self.numpad.value

            data={'title':'NOAA/AFSC/RACE/MACE',
                  'ship':self.ship,
                  'survey':self.survey,
                  'haul':self.activeHaul,
                  'species_code':speciesCode,
                  'common_name':self.activeSpcName,
                  'date':EQDate,
                  'sample_type':'whole fish',
                  'count':number,
                  'scientist':self.scientist
                 }

            #  print the label
            self.printer.printSpecialSampleLabel2(data)

            # print sound
            if self.printSound:
                self.printSound.play()


    def getComment(self):
        keyDialog = keypad.KeyPad(self.comment,  self)
        keyDialog.exec_()
        if keyDialog.okFlag:
            string=keyDialog.dispEdit.toPlainText()
            self.comment=keyDialog.dispEdit.toPlainText()
            string=string.split('\n')
            p=''
            for s in string:
                p=p+s+' '

            # insert comment into sample
            QtSql.QSqlQuery("UPDATE samples SET comments='" + p + "' WHERE ship="+self.ship +
                    " AND survey=" + self.survey + " AND event_id = " + self.activeHaul +
                    " AND sample_id = "+self.activeSampleKey)


    def goExit(self):
        self.close()

    def closeEvent(self, event):
        self.exitValidation()
        #self.refreshTimer.stop()
        if self.returnFlag:
            event.ignore()
        else:
            event.accept()

