'''

'''


#  import
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_CLAMSHaul
import haulwtseldlg
import numpad
import keypad
from math import *
import messagedlg

class CLAMSHaul(QDialog, ui_CLAMSHaul.Ui_clamsHaul):
    '''
        The CLAMS Haul dialog class. This form ....
    '''

    def __init__(self,  parent=None):
        '''
            The CLAMS Haul dialog initialization method. Gets basic information
            and sets up the haul form
        '''

        #  call superclass init methods and GUI form setup method
        super(CLAMSHaul, self).__init__(parent)
        self.setupUi(self)

        #  check if our database connection is open
        self.db = parent.db
        if not self.db.isOpen():
            self.db.open()

        #  copy some info from parent for convienience
        self.workStation=parent.workStation
        self.activeHaul=parent.activeHaul
        self.survey=parent.survey
        self.ship=parent.ship
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.serMonitor=parent.serMonitor
        self.backLogger=parent.backLogger
        self.blue = parent.blue
        self.black = parent.black
        self.scientist=parent.scientist
        self.sciLabel.setText(self.scientist)
        p=self.scientist.split(' ')
        self.firstName=p[0]
        self.haulInfoBtns=[[self.haulInfoBtn1_1, self.haulInfoBtn1_2, self.haulInfoBtn1_3, self.haulInfoBtn1_4],
                           [self.haulInfoBtn2_1, self.haulInfoBtn2_2, self.haulInfoBtn2_3, self.haulInfoBtn2_4],
                           [self.haulInfoBtn3_1, self.haulInfoBtn3_2, self.haulInfoBtn3_3, self.haulInfoBtn3_4]]
        self.partitionLabels=[self.partitionLabel1,self.partitionLabel2,self.partitionLabel3, self.partitionLabel4]
        self.haulInfoGroups=[self.groupBox1, self.groupBox2, self.groupBox3]

        #  define default variable values
        self.comment = ""
        self.incomplete = False
        self.perfBoxFlag = False
        self.reloadFlag=False
        self.forceExit = False

        #  load the error icon
        self.errorIcon = QPixmap()
        self.errorIcon.load(self.settings[QString('IconDir')] + "\\error.bmp")

        #  connect button signals...
        self.connect(self.commentBtn, SIGNAL("clicked()"), self.getComment)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)
        self.connect(self.perfBox, SIGNAL("activated(int)"), self.setFlag)
        self.connect(self.perfCheckBox, SIGNAL("stateChanged(int)"), self.getFullPerfList)

        #  set up window position/size and min/max constraints
        screen=QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.setGeometry((screen.width()-window.width())/2,parent.windowAnchor[0]+(parent.windowAnchor[1]-window.height()), window.width(), window.height())
        self.setMinimumSize(window.width(), window.height())
        self.setMaximumSize(window.width(), window.height())

        #  setup reoccuring dialogs
        self.numpad = numpad.NumPad(self)
        self.message = messagedlg.MessageDlg(self)

        #  create a single-shot timer that runs the application initialization code
        #  this allows the application to complete the main window init method before
        #  the rest of the initialization code runs. We do this because we can't
        #  close the main window (as we would if there was an initialization error)
        #  from the window's init method.
        initTimer = QTimer(self)
        initTimer.setSingleShot(True)
        self.connect(initTimer, SIGNAL("timeout()"), self.formInit)
        initTimer.start(0)


    def formInit(self):

        # set up Haul Info business -
        query = QtSql.QSqlQuery("SELECT gear FROM events WHERE SHIP = " + self.ship + "  AND SURVEY = " +
                self.survey + " AND event_id=" + self.activeHaul)
        query.first()
        self.gear=query.value(0).toString()

        #  load and display the gear image (if available)
        pic = QImage()
        if pic.load(self.settings[QString('ImageDir')] + '\\gearPics\\'+self.gear + ".jpg"):
             pic=pic.scaled(self.picLabel.size(),Qt.KeepAspectRatio,  Qt.SmoothTransformation)
             self.picLabel.setPixmap(QPixmap.fromImage(pic))
        else:
            self.picLabel.clear()

        #  populate gear performance combo box
        query = QtSql.QSqlQuery("SELECT event_performance.performance_code, event_performance.description " +
                                "FROM event_performance INNER JOIN gear_options ON " +
                                "event_performance.performance_code = gear_options.performance_code WHERE " +
                                "(((gear_options.gear)='" + self.gear + "')) ORDER BY gear_options.perf_gui_order")
        self.perfBox.setEnabled(True)
        self.perfCode=[]
        self.perfBox.clear()
        while query.next():
            self.perfBox.addItem(query.value(1).toString())
            self.perfCode.append(query.value(0).toString())

        # get from short list, otherwise, get full list
        queryOld=QtSql.QSqlQuery("SELECT gear, event_type, performance_code, scientist, comments "+
                    "FROM events WHERE ship=" + self.ship+ " AND survey=" + self.survey
                    + " AND event_id=" + self.activeHaul)
        # get values
        queryOld.first()
        if queryOld.value(2).toString() in self.perfCode:
            ind=self.perfCode.index(queryOld.value(2).toString())
        else:
            self.perfCheckBox.setCheckState(Qt.Checked)
            self.getFullPerfList()
            ind=self.perfCode.index(queryOld.value(2).toString())
        self.perfBox.setCurrentIndex(ind)

        #  determine what gear we're working with and set up the details
        query = QtSql.QSqlQuery("SELECT gear_type FROM gear WHERE gear='" + self.gear + "'")
        query.first()
        self.gearType=query.value(0).toString()
        self.haulInfo=[]
        self.completeTest=[]
        if self.gearType == 'SingleCodendTrawl':
            self.singleCodendTrawl()
        elif self.gearType == 'PlanktonNet':
            self.planktonNet()
        elif self.gearType == 'MultiCodendTrawl':
            self.multiCodendTrawl()

        #  update the comment from the trawl event
        self.comment=queryOld.value(4).toString()

        #  check if data already exists
        self.reloadData()


    def singleCodendTrawl(self):
        for i in range(1):
            self.connect(self.haulInfoBtns[0][i], SIGNAL("clicked()"), self.getWeight)
        for j in range(4):
                self.haulInfoBtns[2][j].hide()
        for i in range(1, 4):
            self.partitionLabels[i].hide()
            for j in range(2):
                self.haulInfoBtns[j][i].hide()
        self.groupBox1.setTitle('Haul Weight Type')
        self.groupBox2.setTitle('Haul Weight')
        self.partitionLabels[0].setText('Codend')
        self.partitions=['Codend']
        self.parameters=['PartitionWeightType', 'PartitionWeight']


    def getWeight(self):
        ind=self.haulInfoBtns[0].index(self.sender())
        wtDlg = haulwtseldlg.HaulWtSelDlg(self)
        wtDlg.exec_()
        if wtDlg.ok:
            self.haulInfoBtns[0][ind].setText(wtDlg.weightType)
            self.haulInfoBtns[1][ind].setText(wtDlg.weight)


    def multiCodendTrawl(self):
        for i in range(4):
            self.connect(self.haulInfoBtns[0][i], SIGNAL("clicked()"), self.getWeight)
        for j in range(4):
                self.haulInfoBtns[2][j].hide()
        self.partitionLabels[3].hide()
        for j in range(2):
            self.haulInfoBtns[j][3].hide()
        self.groupBox1.setTitle('Haul Weight Type')
        self.groupBox2.setTitle('Haul Weight')
        self.partitionLabels[0].setText('Codend 1')
        query=QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE ship=" + self.ship+ " AND survey=" + self.survey+
        " AND event_id=" + self.activeHaul+ " AND partition='Codend_2' AND event_parameter='EQ'")
        if query.first():
            self.partitionLabels[1].setText('Codend 2')
        else:
            self.haulInfoBtn1_2.setEnabled(False)
        query=QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE ship=" + self.ship+ " AND survey=" + self.survey+
        " AND event_id=" + self.activeHaul+ " AND partition='Codend_3' AND event_parameter='EQ'")
        if query.first():
            self.partitionLabels[2].setText('Codend 3')
        else:
            self.haulInfoBtn1_3.setEnabled(False)

        self.partitions=['Codend_1', 'Codend_2', 'Codend_3']
        self.parameters=['PartitionWeightType', 'PartitionWeight']


    def planktonNet(self):
        #  HIDE ALL OF THE BUTTONS AND THEN SHOW THEM WHEN YOU'RE CONNECTING SIGNALS
        if self.gear == 'Bongo':
            self.partitionLabels[0].setText('Codend_1')
            self.partitionLabels[1].setText('Codend_2')
            for i in range(0,2):
                self.connect(self.haulInfoBtns[i][0], SIGNAL("clicked()"), self.getFlowmeter)
                self.connect(self.haulInfoBtns[i][1], SIGNAL("clicked()"), self.getFlowmeter)
                self.haulInfoBtns[i][2].hide()
                self.haulInfoBtns[i][3].hide()
            for i in range(2,4):
                self.partitionLabels[i].hide()
            self.haulInfoBtns[2][0].hide()
            self.haulInfoBtns[2][1].hide()
            self.haulInfoBtns[2][2].hide()
            self.haulInfoBtns[2][3].hide()            
            self.groupBox1.setTitle('Flow Meter Start')
            self.groupBox2.setTitle('Flow Meter End')
            #self.partitionLabels[0].setText('Codend')
            self.partitions=['Codend_1',  'Codend_2']
            self.parameters=['FlowMeterStart', 'FlowMeterEnd']
        else:
            for i in range(0,2):
                self.connect(self.haulInfoBtns[i][0], SIGNAL("clicked()"), self.getFlowmeter)
            self.haulInfoBtns[2][0].hide()
            for i in range(1,4):
                self.partitionLabels[i].hide()
                for j in range(3):
                    self.haulInfoBtns[j][i].hide()

            self.groupBox1.setTitle('Flow Meter Start')
            self.groupBox2.setTitle('Flow Meter End')
            self.partitionLabels[0].setText('Codend')
            self.partitions=['Codend']
            self.parameters=['FlowMeterStart', 'FlowMeterEnd']


    def getFlowmeter(self):
        self.numpad.msgLabel.setText("Enter flowmeter number," + self.firstName)
        if self.numpad.exec_():
            self.sender().setText(self.numpad.value)


    def writeHaul(self):

        #  first check if all of the haul buttons have been completed
        haulInfoCompleteFlag = True
        for btns in self.haulInfoBtns:
            for btn in btns:
                if btn.isVisible() and btn.text()=='':
                    #  a button is empty - IOW the form isn't complete
                    haulInfoCompleteFlag = False

        if not haulInfoCompleteFlag:
            #  the form is incomplete - ask the user if they want to close it or fix it
            self.incomplete = True
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],'Haul information has not been completely ' +
                    'entered! Do you still want to close this form?','choice')
            ok = self.message.exec_()
            if ok:
                #  force the exit with an incomplete form
                self.forceExit = True
            else:
                #  we don't want to exit with an incomplete form
                self.forceExit = False

            #  either way, we don't write anything to the database so we return
            return

        # haul info data fields
        for i in range(len(self.partitions)):
            for j in range(len(self.parameters)):
                query = QtSql.QSqlQuery("SELECT * FROM event_data WHERE ship=" + self.ship + " AND survey=" + self.survey +
                                        " AND event_id=" + self.activeHaul + " AND partition='" + self.partitions[i] +
                                        "' AND event_parameter='" + self.parameters[j] + "'")
                if query.first():
                    #  There is an exisitng record - update it with new values
                    query = QtSql.QSqlQuery("UPDATE event_data SET parameter_value='" + self.haulInfoBtns[j][i].text() +
                                            "' WHERE ship=" + self.ship + " AND survey=" + self.survey + " AND event_id=" +
                                            self.activeHaul + " AND partition='" + self.partitions[i] +
                                            "' AND event_parameter='" + self.parameters[j] + "'")
                else:
                    #  This is a new record - insert it
                    query = QtSql.QSqlQuery("INSERT INTO event_data (ship, survey, event_id, partition, event_parameter," +
                                            " parameter_value) VALUES ("+ self.ship + "," + self.survey + "," +
                                            self.activeHaul + ",'" + self.partitions[i] + "','" + self.parameters[j] +
                                            "','" + self.haulInfoBtns[j][i].text() + "')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+ "," + query.lastQuery())

        #haul info data for pocketnets (i.e. partitions named like 'pocketnet' or 'pnet')            
        #find  all partitions named like 'pocketnet' or 'pnet'
        query=QtSql.QSqlQuery("SELECT partition FROM GEAR_OPTIONS, EVENTS WHERE GEAR_OPTIONS.GEAR = EVENTS.GEAR and EVENTS.SHIP = "+
                              self.ship + "  AND  " + "EVENTS.SURVEY = " + self.survey + " AND EVENTS.EVENT_ID = " +
                              self.activeHaul + " AND (LOWER(GEAR_OPTIONS.PARTITION) LIKE 'p-net' OR LOWER(GEAR_OPTIONS.PARTITION) LIKE '%pocketnet%')")
        
        #if there are pocketnets, get the partition names       
        if query.first():               
            
            partition_list = [query.value(0).toString()]
            while query.next():
                #print(partition_list)
                partition_list.append(query.value(0).toString())
                       
            for i in range(len(partition_list)):
                #check if the haul info is already in the database for these partitions (i.e. the haul form has already been opened for this haul); if it has, no need to update the info; otherwise enter info
                query_if_already_entered = QtSql.QSqlQuery("SELECT event_data.event_parameter FROM event_data WHERE event_data.ship = " + self.ship + "  AND event_data.SURVEY = " + self.survey + 
                " AND event_data.EVENT_ID = " + self.activeHaul + " AND event_data.partition = '" +partition_list[i]+ "' AND event_data.event_parameter = 'PartitionWeight'")
                
                #if nothing in database, loop through each pocketnet partition to set PartitionWeightType        
                if not query_if_already_entered.first():       
                
                    query2 = QtSql.QSqlQuery("INSERT INTO event_data (ship, survey, event_id, partition, event_parameter, parameter_value)" +
                                        " VALUES (" + self.ship+ "," + self.survey + "," + self.activeHaul + ",'" +partition_list[i]+ 
                                        "', 'PartitionWeightType','not_subsampled')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+ "," + query2.lastQuery())
                    query3 = QtSql.QSqlQuery("INSERT INTO event_data (ship, survey, event_id, partition, event_parameter, parameter_value) VALUES ("+
                                                        self.ship+ "," + self.survey+ "," + self.activeHaul+ ",'" +partition_list[i]+ "','PartitionWeight','TBD')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+ ","+query3.lastQuery())


        if (self.gearType == 'PlanktonNet'):
            query = QtSql.QSqlQuery("SELECT * FROM event_data WHERE ship=" + self.ship + " AND survey=" + self.survey +
                        " AND event_id=" + self.activeHaul + " AND event_parameter='PartitionWeightType'")
            if not query.first():
                query = QtSql.QSqlQuery("INSERT INTO event_data (ship, survey, event_id, partition, event_parameter, parameter_value)" +
                                        " VALUES (" + self.ship+ "," + self.survey + "," + self.activeHaul +
                                        ",'Codend','PartitionWeightType','not_subsampled')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+ "," + query.lastQuery())
                query = QtSql.QSqlQuery("INSERT INTO event_data (ship, survey, event_id, partition, event_parameter, parameter_value)" +
                                        " VALUES (" + self.ship+ "," + self.survey + "," + self.activeHaul +
                                        ",'Codend','PartitionWeight','TBD')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+ "," + query.lastQuery())

        if self.perfBoxFlag:
            perfCode=self.perfCode[self.perfBox.currentIndex()]
            query = QtSql.QSqlQuery("UPDATE events SET performance_code="+perfCode+ " WHERE ship=" + self.ship+
                    " AND survey=" + self.survey+ " AND event_id = " + self.activeHaul)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+ ","+query.lastQuery())


    def setFlag(self):
        self.perfBoxFlag = True


    def reloadData(self):
        # get existing data, populate lists, indicate selections

        # set haul gear type
        self.gearLabel.setText(self.gear)

        self.sciLabel.setText(self.scientist)
        #repopulate Haul Info
        for i in range(len(self.partitions)):
            for j in range(len(self.parameters)):
                query=QtSql.QSqlQuery("SELECT event_data.parameter_value FROM event_data WHERE event_data.ship="+
                    self.ship+ " AND event_data.survey=" + self.survey+ " AND event_data.event_id=" + self.activeHaul+
                    " AND event_data.partition='" + self.partitions[i]+ "' AND event_data.event_parameter = '" +
                    self.parameters[j]+ "'")
                if query.first():
                    self.haulInfoBtns[j][i].setText(query.value(0).toString())


    def getFullPerfList(self):
        if self.perfCheckBox.checkState():
            query=QtSql.QSqlQuery("SELECT event_performance.performance_code, event_performance.description FROM event_performance")
            self.perfBox.setEnabled(True)
            self.perfCode=[]
            self.perfBox.clear()
    #        self.typeBox.addItem('Select...')
            while query.next(): # populate haul type list
                self.perfBox.addItem(query.value(1).toString())
                self.perfCode.append(query.value(0).toString())
            self.perfBox.setCurrentIndex(-1)
            self.perfBoxFlag=False
        else:
            query=QtSql.QSqlQuery("SELECT event_performance.performance_code, event_performance.description FROM event_performance " +
                    "INNER JOIN gear_options ON event_performance.performance_code = gear_options.performance_code WHERE " +
                    "(((gear_options.gear)='"+self.gearBox.currentText()+"')) ORDER BY gear_options.perf_gui_order")
            self.perfBox.setEnabled(True)
            self.perfCode=[]
            self.perfBox.clear()
            while query.next(): # populate performance list
                self.perfBox.addItem(query.value(1).toString())
                self.perfCode.append(query.value(0).toString())
            self.perfBox.setCurrentIndex(-1)
            self.perfBoxFlag=False


    def getComment(self):
        keyDialog = keypad.KeyPad(self.comment,  self)
        keyDialog.exec_()
        if keyDialog.okFlag:
            self.comment=keyDialog.dispEdit.toPlainText()
            query = QtSql.QSqlQuery("UPDATE events SET comments='"+self.comment+ "' WHERE ship=" + self.ship+
                    " AND survey=" + self.survey+ " AND event_id = " + self.activeHaul)


    def goExit(self):
        self.close()


    def closeEvent(self, event):

        #  check if we're all filled in and write data to database
        self.writeHaul()

        #  check if our form was complete
        if self.incomplete:
            #  form is not complete - check if we're to exit anyways
            if (self.forceExit):
                #  user opted to exit without completing form
                event.setAccepted(False)
                self.reject()
            else:
                #  user has chosen to return to the form to complete it
                event.ignore()
        else:
            #  form is complete - we're done here
            event.accept()
            self.accept()
