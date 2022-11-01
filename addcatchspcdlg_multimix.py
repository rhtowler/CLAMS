
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import  ui_AddCatchSpcDlg_alt3
import listseldialog


class AddCatchSpcDlg(QDialog, ui_AddCatchSpcDlg_alt3.Ui_addcatchspcDlg):
    def __init__(self, parent=None):
        super(AddCatchSpcDlg, self).__init__(parent)

        self.setupUi(self)
        self.mixCreateFlag=False
        self.mixAddFlag=False
        self.ship = parent.ship
        self.survey = parent.survey
        self.activeHaul=parent.activeHaul
        self.activePartition=parent.activePartition
        self.message=parent.message
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.whHaulFlag=parent.whHaulFlag
        self.previous = None
        self.listOrigin = None
        self.chars=''
        self.updatingDigit = False
        self.settings=parent.settings

        #  put the keyboard buttons into a list to easily reference them
        self.digitBtns=[self.A_Btn,self.B_Btn,self.C_Btn,self.D_Btn,self.E_Btn,self.F_Btn,
                        self.G_Btn,self.H_Btn,self.I_Btn,self.J_Btn,self.K_Btn,self.L_Btn,
                        self.M_Btn,self.N_Btn,self.O_Btn,self.P_Btn,self.Q_Btn,self.R_Btn,
                        self.S_Btn,self.T_Btn,self.U_Btn,self.V_Btn,self.W_Btn,self.X_Btn,
                        self.Y_Btn,self.Z_Btn]

        #  connect signals
        for btn in self.digitBtns:
            self.connect(btn, SIGNAL("clicked()"),self.getDigit)

        self.connect(self.fullspcCList, SIGNAL("itemClicked (QListWidgetItem *)"), self.getSpcSel)
        self.connect(self.fullspcSList, SIGNAL("itemClicked (QListWidgetItem *)"), self.getSpcSel)
        self.connect(self.backBtn, SIGNAL("clicked()"), self.clearOneChar)
        self.connect(self.clearBtn, SIGNAL("clicked()"), self.clearAllChar)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)
        self.connect(self.addBtn, SIGNAL("clicked()"), self.sendSel)
        self.connect(self.radio10, SIGNAL("toggled(bool)"), self.getSpcHistory)
        self.connect(self.radioFull, SIGNAL("toggled(bool)"), self.clearAllChar)

        # parent sample buttons
        self.buttons=[self.wholeHaulBtn, self.sortTableBtn, self.mix1Btn,
                self.subMix1Btn, self.mix2Btn]

        #  connect the sample button clicked signal to a method that manages their exclusivity
        #  it seems autoexclusive buttons in a container cannot all be unchecked. Once one is
        #  checked, you can't uncheck it (at least by calling setChecked()
        for btn in self.buttons:
            self.connect(btn, SIGNAL("clicked()"), self.handleSampleBtnEx)

        # position the window
        screen=QDesktopWidget().screenGeometry()
        window=self.geometry()
        self.setGeometry(round(screen.width()*.28, 0), round(screen.height()*.05, 0),
                window.width(), window.height())

        # set default tab, get past haul species
        query=QtSql.QSqlQuery("SELECT event_id FROM events WHERE survey = "+self.survey+
                " AND event_id <= "+self.activeHaul+"")
        self.hauls=[]
        while query.next():
            self.hauls.append(int(query.value(0).toString()))
        self.hauls.reverse()
        self.history=10
        self.getSpcHistory()
        self.radio10.setChecked(True)

        #  set up the sample buttons
        self.setSampleBtnEnable()


    def handleSampleBtnEx(self):
        '''
        handleSampleBtnEx manages the exclusivity of the parent sample buttons
        This
        '''
        #  uncheck all buttons
        for btn in self.buttons:
            btn.setChecked(False)
        #  and check the button pressed
        self.sender().setChecked(True)


    def setSampleBtnEnable(self):
        '''
        setSampleBtnEnable enables/disables the parent sample buttons based on
        the
        '''

        #  set all buttons enabled
        for btn in self.buttons:
            btn.setEnabled(True)

        #  uncheck all buttons
        for btn in self.buttons:
            btn.setChecked(False)

        # set default values
        if not self.whHaulFlag:
            self.wholeHaulBtn.setEnabled(False)

        # find out if we have a mix1
        query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship = "+self.ship+" AND survey = "+
                self.survey+ " AND event_id = "+self.activeHaul+" AND partition ='"+self.activePartition+
                "' AND species_code=100002")
        if not query.first():
            # no mix 1 in the system
            self.mix1Btn.setEnabled(False)
            self.subMix1Btn.setEnabled(False)
        else:
            # we have a mix 1 - check if we have a submix for mix 1
            query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship = "+self.ship+" AND survey = "+
                    self.survey+ " AND event_id = "+self.activeHaul+" AND partition ='"+self.activePartition+
                    "' AND species_code=100003")
            if not query.first():
                # no submix1
                self.subMix1Btn.setEnabled(False)

        #  check if there is a mix2
        query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship = "+self.ship+" AND survey = "+
                self.survey+ " AND event_id = "+self.activeHaul+" AND partition ='"+self.activePartition+
                "' AND species_code=100004")
        if not query.first():
            #  there is no mix2
            self.mix2Btn.setEnabled(False)


    def getDigit(self):

        self.updatingDigit=True
        self.chars=self.chars+self.sender().text()
        self.lineEdit.setText(self.chars)

        self.radioFull.setChecked(True)
        self.fullspcCList.clear()
        self.fullspcSList.clear()

        self.getList()
        self.updatingDigit=False


    def clearOneChar(self):
        self.chars=self.chars[:-1]
        self.lineEdit.setText(self.chars)
        self.getList()


    def clearAllChar(self):
        if not self.updatingDigit:
            self.chars=''
            self.spcLabel.setText('')
            self.picLabel.clear()
            self.lineEdit.setText(self.chars)
            self.fullspcCList.clear()
            self.fullspcSList.clear()
            self.getList()



    def getList(self):

        if self.chars=='':
            commonQuery = "SELECT species.common_name FROM species ORDER BY species.common_name"
            sciQuery = "SELECT species.scientific_name FROM species WHERE species_code<999900 ORDER BY species.scientific_name"
        else:
            like_exp = "'"+self.chars+"%'"
            commonQuery = ("SELECT species.common_name FROM species WHERE upper(species.common_name)" +
                " LIKE upper(" + like_exp + ") AND species_code<999900 ORDER BY species.common_name")
            sciQuery = ("SELECT species.scientific_name FROM species WHERE upper(species.scientific_name) "+
                " LIKE upper(" + like_exp + ") AND species_code<999900 ORDER BY species.scientific_name")

        query=QtSql.QSqlQuery(commonQuery)
        trunc=[]
        while query.next():
            trunc.append(query.value(0).toString())
        self.fullspcCList.addItems(QStringList(trunc))

        query=QtSql.QSqlQuery(sciQuery)
        trunc1=[]
        while query.next():
            trunc1.append(query.value(0).toString())
        self.fullspcSList.addItems(QStringList(trunc1))

        if len(trunc)<2 and self.nameTab.currentIndex==0:
            self.fullspcCList.setCurrentRow(1)
        elif len(trunc1)<2 and self.nameTab.currentIndex==1:
            self.fullspcSList.setCurrentRow(1)

        self.picLabel.clear()


    def getSpcSel(self):

        # image code
        self.listOrigin=self.sender()
        self.activeSpcName=self.listOrigin.currentItem().text()
        if self.nameTab.currentIndex()==0:
            self.nameType='common'
            query=QtSql.QSqlQuery("SELECT species.species_code  "+
                    "FROM species WHERE species.common_name='"+
                    self.listOrigin.currentItem().text()+"'")
        else:
            self.nameType='scientific'
            query=QtSql.QSqlQuery("SELECT species.species_code  "+
                    "FROM species WHERE species.scientific_name='"+
                    self.listOrigin.currentItem().text()+"'")
        query.first()
        self.activeSpcCode=query.value(0).toString()
        imgName=None

        # check for multiple subcategories
        query=QtSql.QSqlQuery("SELECT subcategory FROM species_associations WHERE species_code="+
                self.activeSpcCode)
        subcats=[]
        while query.next():
            subcats.append(query.value(0).toString())
        if len(subcats)>1:
            # species has multiple subclasses in species associations
            #  display the subcat selection dialog
            self.listDialog = listseldialog.ListSelDialog(subcats, 'Short',  self)
            self.listDialog.label.setText('Choose Size Class')
            if self.listDialog.exec_():
                if (self.listDialog.itemList.currentRow() < 0):
                    #  no name selected
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                            'Please select a Size Class or "All Sizes".', 'info')
                    self.message.exec_()
                else:
                    self.activeSpcSubcat = self.listDialog.itemList.currentItem().text()
                    imgName=self.activeSpcCode #+"_"+self.activeSpcSubcat
                    labelText=self.activeSpcName+"-"+self.activeSpcSubcat
            else:
                return

        elif len(subcats)>1:
            self.activeSpcSubcat=subcats[0]# species has one listing in species associations
            imgName=self.activeSpcCode
            labelText=self.activeSpcName
        else:
            self.activeSpcSubcat='None' # species not listed in species associations
            imgName=self.activeSpcCode
            labelText=self.activeSpcName
        # find out previous occurence
        self.previous=1
        if int(self.activeSpcCode)<99999:# not a mix
            query=QtSql.QSqlQuery("SELECT parameter_value  "+ "FROM species_data WHERE species_code="+
                    self.activeSpcCode+" AND subcategory='"+self.activeSpcSubcat+
                    "' AND lower(species_parameter)='previous_occurrence'")
            if query.first():
                self.previous=int(query.value(0).toString())

        # load label
        self.spcLabel.setText(labelText)
        # set image
        pic=QImage()
        if imgName:
            if pic.load(self.settings[QString('ImageDir')]+'\\fishPics\\'+imgName+".jpg"):
               pic=pic.scaled(self.picLabel.size(),Qt.KeepAspectRatio,  Qt.SmoothTransformation)
               self.picLabel.setPixmap(QPixmap.fromImage(pic))
            else:
                self.picLabel.clear()
        # submix check
        if self.activeSpcCode=='100003':
            # find out if we have some mixes
            query=QtSql.QSqlQuery("SELECT sample_id FROM samples WHERE ship = "+self.ship+" AND survey = "+self.survey+
                    " AND event_id = "+self.activeHaul+" AND partition ='"+self.activePartition+"' AND species_code=100002")
            if not query.first():  # no mix 1 in the system

                self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                            "There's no Mix1 sample for this partition.  you need to create it before using the SubMix1", 'info')
                self.message.exec_()
            else:# you can only choose Mix1!!
                for btn in self.buttons:
                    btn.setEnabled(False)
                self.mix1Btn.setEnabled(True)
                self.mix1Btn.setChecked(True)


    def sendSel(self):

        #  get the selected parent sample
        self.parentSample=None
        for btn in self.buttons:
            if btn.isChecked():
                self.parentSample = btn.text()
                break
        if self.parentSample==None:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],
                    "You need to select a parent sample! ", 'info')
            self.message.exec_()
            return

        if self.listOrigin == None:
            return

        if self.previous==0:
            #  ask if we want to add this exotic species we've never encountered
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "We've never seen a "+
                    self.listOrigin.currentItem().text()+". Are you sure that's right? ", 'choice')
            if not self.message.exec_():
                return

        #  emit the changed signal to update parent
        self.emit(SIGNAL("changed"))

        self.setSampleBtnEnable()

        #  only clear the text box and list if this isn't a history pick
        if not self.radio10.isChecked():
            self.clearAllChar()


    def getSpcHistory(self):
        '''
        Create a "short list" of the most common species from the last
        few hauls.
        '''

        #  clear the short list
        self.fullspcCList.clear()
        self.fullspcSList.clear()

        spcList=[]

        if (len(self.hauls) < 2):
            return

        hauls = str(self.hauls[0])
        if len(self.hauls)<self.history:
            count=len(self.hauls)
        else:
            count=self.history
        for i in range(count-1):
            hauls=(hauls+","+str(self.hauls[i+1]))
        query=QtSql.QSqlQuery("SELECT species.common_name, species.species_code FROM species INNER " +
                "JOIN samples ON species.species_code=samples.species_code WHERE (samples.event_id in("+
                hauls+") AND (samples.survey = "+self.survey+") AND species.species_code not in (100000, 100001) AND species.species_code<900000) " +
                "GROUP BY species.common_name, species.species_code")
        wghtList=[]
        while query.next():
            spcList.append(query.value(0).toString())
            query1=QtSql.QSqlQuery("SELECT sum(BASKETS.WEIGHT ) FROM BASKETS, SAMPLES  WHERE " +
                    "(( SAMPLES.SAMPLE_ID = BASKETS.SAMPLE_ID ) and (SAMPLES.SPECIES_CODE = "+
                    query.value(1).toString()+") AND  (SAMPLES.SURVEY = "+self.survey+
                    ") AND  (SAMPLES.event_id in("+hauls+")))" )
            query1.first()
            wghtList.append(query1.value(0).toFloat()[0])

        #  if we have a history - create the "short list"
        if wghtList:
            wghtList, spcList = (list(x) for x in zip(*sorted(zip(wghtList, spcList))))
            spcList.reverse()
            self.fullspcCList.addItems(QStringList(spcList))


    def getMethotSpecies(self):
        spcList=[]
        query=QtSql.QSqlQuery("SELECT species.common_name FROM species WHERE plankton_species=1 ORDER BY species.common_name");
        while query.next():
            spcList.append(query.value(0).toString())
        self.planktonList.addItems(QStringList(spcList))


    def getRadioSel(self):

        self.history=10
        self.getSpcHistory()


    def goExit(self):
        self.accept()



