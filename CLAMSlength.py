
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import  ui_CLAMSLength
import numpad
import keypad
import messagedlg
import histogramplot
import addspecdlg

class CLAMSLength(QDialog, ui_CLAMSLength.Ui_clamsLength):

    def __init__(self, parent=None):
        super(CLAMSLength, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.db=parent.db
        self.serMonitor=parent.serMonitor
        if not self.db.isOpen():
            self.db.open()
        self.workStation=parent.workStation
        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeHaul
        self.activePartition=parent.activePartition
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.backLogger=parent.backLogger
        self.blue = parent.blue
        self.black = parent.black
        self.scientist=parent.scientist
        self.sciLabel.setText(self.scientist)
        p=self.scientist.split(' ')
        self.firstName=p[0]
        #setup reoccuring dlgs
        self.numDialog = numpad.NumPad(self)
        self.message=messagedlg.MessageDlg(self)
        self.addspec = addspecdlg.addspecedlg(self)

        # figure out if this is administrative station
        actions = str(self.settings[QString('MainActions')] )
        actions = actions.split(',')
        if 'Administration' in actions:
            self.admin=True
        else:
            self.admin=False
        # initialize variables
        self.activeSpcName=None
        self.comment=''
        self.value=''
        self.tempval=''
        self.valFlag=1
        self.sex=None
        self.editFlag=False
        self.plotFreshCount=0
        self.malesPlot=[]
        self.femalesPlot=[]
        self.unsexPlot=[]
        self.selRecord=[None, None, None]
        self.freeze=False
        self.specimenKey = None
        # set up some table bits
        self.sumTable.horizontalHeader().setVisible(False)
        self.sumTable.setColumnCount(1)
        # set default sampling Method
        query=QtSql.QSqlQuery("SELECT sampling_method FROM sampling_methods")
        while query.next():
            self.samplingMethodBox.addItem(query.value(0).toString())
        self.samplingMethodBox.setCurrentIndex(self.samplingMethodBox.findText('random'))
        
        # populate species window
        self.updateSpecies()
        
        # set up tables for data display
        font=QFont('helvetica', 14, -1, False)
        self.measureView.setFont(font)
        self.measureModel = QtSql.QSqlQueryModel()
        self.measureView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.measureView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.measureView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.measureView.setModel(self.measureModel)
        self.selModel=QItemSelectionModel(self.measureModel, self.measureView)
        self.measureView.setSelectionModel(self.selModel)
        self.measureView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)

        self.measureView.show()
        # set up lf plot
        self.lfPlotScene=histogramplot.HistogramPlot(self)
        self.lfPlot.setScene(self.lfPlotScene)
        self.lfPlot.scale(4, 4)
        self.lfPlot.show()

        # set up window position
        screen=QDesktopWidget().screenGeometry()
        window=self.geometry()
        self.setGeometry((screen.width()-window.width())/2,parent.windowAnchor[0]+(parent.windowAnchor[1]-window.height()), window.width(), window.height())
        self.setMinimumSize(window.width(), window.height())
        self.setMaximumSize(window.width(), window.height())
        # general slots
        self.connect(self.deleteBtn, SIGNAL("clicked()"), self.goDelete)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)
        self.connect(self.manualBtn, SIGNAL("clicked()"), self.getManual)
        self.connect(self.speciesList, SIGNAL("itemSelectionChanged()"), self.getSpecies)
        self.connect(self.selModel, SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.getMeasureRow)
        self.connect(self.maleBtn, SIGNAL("clicked()"), self.getSex)
        self.connect(self.femaleBtn, SIGNAL("clicked()"), self.getSex)
        self.connect(self.unsexBtn, SIGNAL("clicked()"), self.getSex)
        self.connect(self.serMonitor, SIGNAL("SerialDataReceived"), self.getAuto)
        self.connect(self.commentBtn, SIGNAL("clicked()"), self.getComment)
        self.connect(self.lengthTypeBox, SIGNAL("activated(int)"), self.lengthTypeChanged)
        
        # connect to serial devices
        self.openSerial()



    def updateSpecies(self):
        
        # populate species window
        query=QtSql.QSqlQuery("SELECT species.common_name, species.scientific_name, samples.species_code, samples.sample_id, samples.subcategory FROM species, samples, baskets "+
                "WHERE species.species_code = samples.species_code AND samples.ship=baskets.ship AND samples.survey=baskets.survey AND samples.event_id=baskets.event_id AND "+
                "samples.sample_id=baskets.sample_id AND samples.ship="+self.ship+" AND samples.survey="+
                self.survey+" AND samples.event_id="+self.activeHaul+
                " AND samples.partition='"+self.activePartition+"' AND baskets.basket_type='Measure' AND "+
                "samples.sample_type='Species' GROUP BY species.common_name, samples.species_code, species.scientific_name, samples.sample_id, samples.subcategory",  self.db)
        self.sampleKeys=[]
        self.speciesCodes=[]
        self.subCats=[]
        while query.next():
            #get the namespace
            query0=QtSql.QSqlQuery("SELECT PARAMETER_VALUE FROM sample_data WHERE sample_parameter='sample_name' AND ship="+
                    self.ship+" AND survey="+self.survey+" AND event_id="+self.activeHaul+ " AND sample_id="+query.value(3).toString())
            subcat=query.value(4).toString()
            if query0.first():
                if query0.value(0).toString()=='scientific':
                    species=query.value(1).toString()
                else:
                    species=query.value(0).toString()
            else:
                species=query.value(0).toString()
            if subcat<>'None':
                name=species+'-'+subcat
            else:
                name=species
            self.speciesList.addItem(name)
            self.speciesCodes.append(query.value(2).toString())
            self.subCats.append(subcat)
            self.sampleKeys.append(query.value(3).toString())


    def getSpecies(self):
        
        # set active species and inform the user
        self.activeSpcName = self.speciesList.currentItem().text()
        
        self.freeze=True
        self.addspec.setMessage(self.errorIcons[1], self.errorSounds[2],
                "Changing the Active Species to: \n \n"+ self.activeSpcName ,'info')
        self.addspec.exec_()
        self.freeze=False
        
        #  reset the GUI
        self.lengthTypeBox.clear()
        self.sumTable.setEnabled(True)
        self.groupSexBox.setEnabled(True)
        self.otherBox.setEnabled(True)

        # get species code and sample key
        self.activeSpcCode=self.speciesCodes[self.speciesList.currentRow()]
        self.activeSpcSubcat=self.subCats[self.speciesList.currentRow()]
        self.sampleKey=self.sampleKeys[self.speciesList.currentRow()]

        # get species_data prameters
        params = ['min_length', 'max_length', 'primary_length_type',
                'secondary_length_type']
        nParms = len(params)
        vals = [None] * nParms
        for i in range(nParms):
            query = QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code=" +
                    self.activeSpcCode+" AND subcategory='" + self.activeSpcSubcat +
                    "' AND lower(species_parameter)='" + params[i] + "'", self.db)
            if query.first():
                vals[i] = query.value(0).toString()

        #  set the min and max lengths
        if vals[0] <> None:
            self.minLength = float(vals[0])
        else:
            self.minLength = 0.
        if vals[1] <> None:
            self.maxLength = float(vals[1])
        else:
            self.maxLength = 999.

        #  set primary length type and initialize the lengthTypes measurement_types
        #  query constraint string
        if vals[2] <> None:
            self.lengthTypeBox.addItem(vals[2])
            self.lenthTypes = "'" + vals[2] + "'"
        else:
            #  by default we add fork_length if no primary is specified
            self.lengthTypeBox.addItem('fork_length')
            self.lenthTypes = "'fork_length'"

        #  set the length_type combo box to primary
        self.lengthTypeBox.setCurrentIndex(0)

        #  add alternative (secondary) length type
        if vals[3] <> None:
            self.lengthTypeBox.addItem(vals[3])
            self.lenthTypes = self.lenthTypes + ",'" + vals[3] + "'"
            
        # get picture
        if self.activeSpcSubcat <> 'None':
            imgName = self.activeSpcCode+"_"+self.activeSpcSubcat
        else:
            imgName = self.activeSpcCode

        pic = QImage()
        if pic.load(self.settings[QString('ImageDir')]+'\\fishPics\\'+imgName+".jpg"):
#            pic=pic.scaled(self.picLabel.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(pic))
        else:
             self.picLabel.clear()

        #check for existing records going through length type changed
        self.lengthTypeChanged()

        # reset sex buttons
        if self.maleBtn.isChecked():
            self.maleBtn.setChecked(False)
            self.maleBtn.setPalette(self.black)
        if self.femaleBtn.isChecked():
            self.femaleBtn.setChecked(False)
            self.femaleBtn.setPalette(self.black)
        if self.unsexBtn.isChecked():
            self.unsexBtn.setChecked(False)
            self.unsexBtn.setPalette(self.black)
        self.sex=None


    def getManual(self):
        self.manualFlag=True
        self.overrideFlag=False
        if self.activeSpcName==None:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    "Please select a species!", 'info')
            self.message.exec_()
            return
        if self.sex==None:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    "Please select a sex!",'info')
            self.message.exec_()
            return
        while self.valFlag:
            self.numDialog.msgLabel.setText("Enter Length in cm")
            self.numDialog.exec_()
            self.value=self.numDialog.value
            # validation
            if float(self.value)>self.minLength and float(self.value)<self.maxLength:# measurement within specs
                self.writeTable()
                self.valFlag=False
            else:
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1], self.firstName +
                        ", The length is out of range for this. Do you want to reenter length?", 'choice')
                if self.message.exec_():
                    self.valFlag=True
                else:
                    self.message.setMessage(self.errorIcons[2],self.errorSounds[2], "You're in big trouble, "
                            +self.firstName, 'info')
                    self.message.exec_()
                    self.overrideFlag=False
                    # write into override table
                    self.writeTable()

                    self.valFlag=False
        self.valFlag=True


    def getAuto(self, device, val):
        try:
            float(val)
        except:
            return
        if self.freeze:# we're working on a previous length, dont interrupt with new measurement
            return
        self.manualFlag=False
        self.overrideFlag=False
        if self.activeSpcName==None:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    "Please select a species!", 'info')
            self.message.exec_()
            return
        if self.sex==None:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    "Please select a sex!",'info')
            self.message.exec_()
            return
        self.value=val
        if float(self.value)>self.minLength and float(self.value)<self.maxLength:# measurement within specs
            self.writeTable()
            self.sounds[self.devices.index(device)].play()
        else:
            self.freeze=True
            self.message.setMessage(self.errorIcons[1],self.errorSounds[1], self.firstName +
                    ", The length is out of range for this. Do you want to reenter length?", 'choice')
            if self.message.exec_():
                self.valFlag=True
            else:
                self.message.setMessage(self.errorIcons[2],self.errorSounds[2],
                        "You're in big trouble, "+self.firstName, 'info')
                self.message.exec_()
                self.overrideFlag=True
                self.writeTable()
            self.freeze=False


    def getSex(self):
        button=self.sender().text()
        if button =='Male':
            self.maleBtn.setPalette(self.blue)
            self.femaleBtn.setChecked(False)
            self.femaleBtn.setPalette(self.black)
            self.unsexBtn.setChecked(False)
            self.unsexBtn.setPalette(self.black)
            self.sex='Male'
        elif button =='Female':
            self.femaleBtn.setPalette(self.blue)
            self.maleBtn.setChecked(False)
            self.maleBtn.setPalette(self.black)
            self.unsexBtn.setChecked(False)
            self.unsexBtn.setPalette(self.black)
            self.sex='Female'
        elif button =='Unsexed':
            self.unsexBtn.setPalette(self.blue)
            self.maleBtn.setChecked(False)
            self.maleBtn.setPalette(self.black)
            self.femaleBtn.setChecked(False)
            self.femaleBtn.setPalette(self.black)
            self.sex='Unsexed'
        if not self.maleBtn.isChecked and not self.femaleBtn.isChecked and not self.unsexBtn.isChecked:
            self.sex=None


    def lengthTypeChanged(self):
        #check for existing records
        self.len_type=self.lengthTypeBox.currentText()
        QMessageBox.information(self, "Length Measurement Type", "<font size = 12>You should now measure " +self.len_type)
        self.reloadTable()
        self.reloadLFPlot()

    def reloadTable(self):
        # Fix 10-30-2017 NEL: remove query of 'length' in measurements table to specific length type- whatever is selected in the combo box
        if self.admin:
            sql=("SELECT a.specimen_id, a.length, b.sex "+
                    " FROM "+
                    " (SELECT measurements.ship, "+
                     "  measurements.survey, "+
                      " measurements.event_id, "+
                      " measurements.specimen_id, "+
                      " measurements.measurement_value as length "+
                    " FROM  measurements JOIN specimen ON "+
                      "  (measurements.ship = specimen.ship "+
                      " AND measurements.survey = specimen.survey "+
                      " AND measurements.event_id = specimen.event_id "+
                      " AND measurements.specimen_id = specimen.specimen_id) "+
                    " WHERE measurement_type = '" + self.len_type + "' and  "+
                    " measurements.ship="+self.ship+" and  "+
                    " measurements.survey="+self.survey+" and  "+
                    " measurements.event_id="+self.activeHaul+" and  "+
                    " measurements.sample_id="+self.sampleKey+" and "+
                    " specimen.protocol_name ='Length_Sex') a "+
                  " LEFT OUTER JOIN "+
                    " (SELECT ship, survey, event_id, specimen_id, measurement_value as sex "+
                    " FROM measurements "+
                    " WHERE measurement_type = 'sex') b     "+
                  " ON (b.ship = a.ship "+
                  " AND b.survey = a.survey "+
                  " AND b.event_id = a.event_id "+
                  " AND b.specimen_id = a.specimen_id) ORDER BY  a.specimen_id")
        else:
            sql=("SELECT a.specimen_id, a.length, b.sex "+
                    " FROM "+
                    " (SELECT measurements.ship, "+
                     "  measurements.survey, "+
                      " measurements.event_id, "+
                      " measurements.specimen_id, "+
                      " measurements.measurement_value as length "+
                    " FROM  measurements JOIN specimen ON "+
                      "  (measurements.ship = specimen.ship "+
                      " AND measurements.survey = specimen.survey "+
                      " AND measurements.event_id = specimen.event_id "+
                      " AND measurements.specimen_id = specimen.specimen_id) "+
                    " WHERE measurement_type in '" + self.len_type + "' and  "+
                    " measurements.ship="+self.ship+" and  "+
                    " measurements.survey="+self.survey+" and  "+
                    " measurements.event_id="+self.activeHaul+" and  "+
                    " measurements.sample_id="+self.sampleKey+" and "+
                    " specimen.protocol_name ='Length_Sex' and "+
                    " specimen.workstation_id = "+self.workStation+") a "+
                  " LEFT OUTER JOIN "+
                    " (SELECT ship, survey, event_id, specimen_id, measurement_value as sex "+
                    " FROM measurements "+
                    " WHERE measurement_type = 'sex') b     "+
                  " ON (b.ship = a.ship "+
                  " AND b.survey = a.survey "+
                  " AND b.event_id = a.event_id "+
                  " AND b.specimen_id = a.specimen_id) ORDER BY a.specimen_id")

        self.measureModel.setQuery(sql)
        self.measureModel.setHeaderData(0, Qt.Horizontal, 'SPEC. ID')
        self.measureModel.reset()
        self.measureView.scrollToBottom()
        self.updateSumTable()


    def reloadLFPlot(self):
        self.lfPlotScene.clearPlot()
        self.lmax=[]
        for i in range(80):
            self.lmax.append(0.)

        # Fix 10-30-2017 NEL: remove query of 'length' in measurements table to specific length type- whatever is selected in the combo box
        if self.admin:
            sql=("SELECT a.length, b.sex "+
                    " FROM  "+
                    " (SELECT measurements.ship, "+
                     "  measurements.survey, "+
                      " measurements.event_id, "+
                      " measurements.specimen_id, "+
                      " measurements.measurement_value as length "+
                    " FROM  measurements JOIN specimen ON "+
                      "  (measurements.ship = specimen.ship "+
                      " AND measurements.survey = specimen.survey "+
                      " AND measurements.event_id = specimen.event_id "+
                      " AND measurements.specimen_id = specimen.specimen_id) "+
                    " WHERE measurement_type in '" + self.len_type + "' and  "+
                    " measurements.ship="+self.ship+" and  "+
                    " measurements.survey="+self.survey+" and  "+
                    " measurements.event_id="+self.activeHaul+" and  "+
                    " measurements.sample_id="+self.sampleKey+" and "+
                    " specimen.protocol_name ='Length_Sex') a "+
                  " LEFT OUTER JOIN "+
                    " (SELECT ship, survey, event_id, specimen_id, measurement_value as sex "+
                    " FROM measurements "+
                    " WHERE measurement_type = 'sex') b "+
                  " ON (b.ship = a.ship "+
                  " AND b.survey = a.survey "+
                  " AND b.event_id = a.event_id "+
                  " AND b.specimen_id = a.specimen_id)")
        else:
            sql=("SELECT a.length, b.sex "+
                    " FROM  "+
                    " (SELECT measurements.ship, "+
                     "  measurements.survey, "+
                      " measurements.event_id, "+
                      " measurements.specimen_id, "+
                      " measurements.measurement_value as length "+
                    " FROM  measurements JOIN specimen ON "+
                      "  (measurements.ship = specimen.ship "+
                      " AND measurements.survey = specimen.survey "+
                      " AND measurements.event_id = specimen.event_id "+
                      " AND measurements.specimen_id = specimen.specimen_id) "+
                    " WHERE measurement_type in '" + self.len_type + "' and  "+
                    " measurements.ship="+self.ship+" and  "+
                    " measurements.survey="+self.survey+" and  "+
                    " measurements.event_id="+self.activeHaul+" and  "+
                    " measurements.sample_id="+self.sampleKey+" and "+
                    " specimen.protocol_name ='Length_Sex' and "+
                    " specimen.workstation_id = "+self.workStation+") a "+
                  " LEFT OUTER JOIN "+
                    " (SELECT ship, survey, event_id, specimen_id, measurement_value as sex "+
                    " FROM measurements "+
                    " WHERE measurement_type = 'sex') b "+
                  " ON (b.ship = a.ship "+
                  " AND b.survey = a.survey "+
                  " AND b.event_id = a.event_id "+
                  " AND b.specimen_id = a.specimen_id)")

        query=QtSql.QSqlQuery(sql)
        self.scale=1.
        while query.next():
            l=int(round(float(query.value(0).toString())))
            self.lfPlotScene.update(l, query.value(1).toString())
            self.lmax[l]+=self.scale
            if max(self.lmax)>20.:
                self.lfPlotScene.rescale(0.8)
                self.scale=self.scale*0.8
                for i in range(80):
                    self.lmax[i]=self.lmax[i]*.8

        self.lfPlot.repaint()


    def writeTable(self):

        self.specimenKey = None

        #  check if this is a randon or non-random sample
        samplingMethod = self.samplingMethodBox.currentText()

        #  check if the database is open
        if not self.db.isOpen():
            self.message.setMessage(self.errorIcons[2],self.errorSounds[2],
                    "Database is not connected - restart clams",'info')
            self.message.exec_()
            return

        # write specimen table
        query = QtSql.QSqlQuery("INSERT INTO specimen (ship,survey,event_id,sample_id,workstation_id," +
                "scientist,sampling_method,protocol_name,comments) VALUES ("+self.ship+","+self.survey+
                ","+self.activeHaul+ ","+self.sampleKey+","+self.workStation+",'"+self.scientist+"','"+
                samplingMethod+"','Length_Sex','"+self.comment+"')", self.db)
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

        #  get the key for the specimen record we just created
        query = QtSql.QSqlQuery("SELECT max(specimen_id) FROM specimen WHERE workstation_id = "+
                self.workStation+" AND ship="+self.ship+ " AND survey="+self.survey+
                " AND event_id="+self.activeHaul, self.db)
        while query.next():
            self.specimenKey = query.value(0).toString()

        #  set the device ID based on manual or electronic entry
        if self.manualFlag:
            deviceId = '0'
        else:
            deviceId = self.devices[0]

        # get length_type
        len_type = self.lengthTypeBox.currentText()

        #  make sure we have a specimen key
        if (not self.specimenKey == None):
            #  Insert the length type that is selected in the lengthTypeBox combo 'len_type', now skip insert of 'length' type
            query = QtSql.QSqlQuery("INSERT INTO measurements (ship, survey,event_id,sample_id,specimen_id," +
                    "measurement_type,device_id,measurement_value) VALUES ("+self.ship+","+self.survey+","+
                    self.activeHaul+ ","+self.sampleKey+","+self.specimenKey+",'"+len_type+"',"+deviceId+
                    ",'"+self.value+"')")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # write sex
            query = QtSql.QSqlQuery("INSERT INTO measurements (ship,survey,event_id,sample_id,specimen_id," +
                    "measurement_type,  device_id,measurement_value) VALUES ("+self.ship+","+self.survey+","+
                    self.activeHaul+ ","+self.sampleKey+","+self.specimenKey+",'sex',0,'"+self.sex+"')")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            if self.overrideFlag:
                query = QtSql.QSqlQuery("INSERT INTO override (scientist, record_id, crime, table_name) VALUES ('"+
                        self.scientist+"',"+self.specimenKey+", 'length range','measurement')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            self.reloadTable()

            # update plot
            self.lfPlotScene.update(int(round(float(self.value))), self.sex)
            self.lmax[int(round(float(self.value)))]+=self.scale
            if max(self.lmax)>20.:
                self.lfPlotScene.rescale(0.8)
                self.scale=self.scale*0.8
                for i in range(80):
                    self.lmax[i]=self.lmax[i]*.8

            self.comment= ''

    def getMeasureRow(self):
        self.selRecord=[]
        selObj=self.measureView.currentIndex()
        for i in range(3):
            index= self.measureModel.index(selObj.row(), i, QModelIndex())
            self.selRecord.append(self.measureModel.data(index, Qt.DisplayRole).toString())
        self.specimenKey=self.selRecord[0]
        query=QtSql.QSqlQuery("SELECT comments FROM specimen WHERE specimen_id = "+self.specimenKey+" AND ship="+self.ship+
        " AND survey="+self.survey+" AND event_id="+self.activeHaul)
        if query.first():
            self.comment=query.value(0).toString()


    def goDelete(self):
        if not self.selRecord[0]==None:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "Are you sure you want to permanently delete this record, "+self.firstName+"?", 'choice')
            if self.message.exec_():
                query = QtSql.QSqlQuery("DELETE FROM measurements WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND specimen_id = "+self.selRecord[0]) # delete away
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                query = QtSql.QSqlQuery("DELETE FROM specimen WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND specimen_id = "+self.selRecord[0]) # delete away
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                self.comment = ''
                self.reloadTable()


    def updateSumTable(self):
        if self.admin:
            query=QtSql.QSqlQuery("SELECT count(specimen_id), SEX "+
                " FROM V_SPECIMEN_MEASUREMENTS  WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND haul="+self.activeHaul+" AND SAMPLE_ID = "+self.sampleKey+
                "AND PROTOCOL_NAME='Length_Sex' GROUP BY SEX ")
        else:
            query=QtSql.QSqlQuery("SELECT count(specimen_id), SEX "+
                " FROM V_SPECIMEN_MEASUREMENTS  WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND haul="+self.activeHaul+" AND SAMPLE_ID = "+self.sampleKey+"  AND "+
                " WORKSTATION_ID = "+self.workStation+" AND PROTOCOL_NAME='Length_Sex'  GROUP BY SEX ")
        counts=[]
        self.sumTable.setItem(0, 0,QTableWidgetItem('0'))
        self.sumTable.setItem(1, 0,QTableWidgetItem('0'))
        self.sumTable.setItem(2, 0,QTableWidgetItem('0'))
        while query.next():# there's gents
            if query.value(1).toString()=='Male':
                self.sumTable.setItem(0, 0,QTableWidgetItem(query.value(0).toString()))
            elif query.value(1).toString()=='Female':
                self.sumTable.setItem(1, 0,QTableWidgetItem(query.value(0).toString()))
            elif query.value(1).toString()=='Unsexed':
                self.sumTable.setItem(2, 0,QTableWidgetItem(query.value(0).toString()))
            counts.append(int(query.value(0).toString()))
        self.sumTable.setItem(3, 0,QTableWidgetItem(str(sum(counts))))


    def openSerial(self):
        query = QtSql.QSqlQuery("SELECT measurement_setup.measurement_type, measurement_setup.device_id, device_configuration.parameter_value FROM " +
                                "device_configuration INNER JOIN measurement_setup ON device_configuration.device_id " +
                                "= measurement_setup.device_id WHERE measurement_setup.workstation_id=" +
                                self.workStation+" AND measurement_setup.gui_module='Length' AND " +
                                "device_configuration.device_parameter = 'SoundFile'")
        self.measurements = []
        self.devices = []
        self.sounds = []
        while query.next():
            self.measurements.append(query.value(0).toString())
            self.devices.append(query.value(1).toString())
            self.sounds.append(QSound(self.settings[QString('SoundsDir')] +'\\'+ query.value(2).toString() + '.wav'))


    def getComment(self):

        if (self.specimenKey == None):
            return

        keyDialog = keypad.KeyPad(self.comment, self)
        keyDialog.exec_()

        if keyDialog.okFlag:
            string = keyDialog.dispEdit.toPlainText()
            self.comment = keyDialog.dispEdit.toPlainText()
            string = string.split('\n')
            p=''
            for s in string:
                p=p+s+' '

            # insert comment into sample
            QtSql.QSqlQuery("UPDATE specimen SET comments='"+p+ "' WHERE  ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeHaul+" AND specimen_id = "+self.specimenKey)


    def goExit(self):
        self.close()


    def closeEvent(self, event):
        event.accept()



