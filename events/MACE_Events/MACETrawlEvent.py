# coding=utf-8

#     National Oceanic and Atmospheric Administration (NOAA)
#     Alaskan Fisheries Science Center (AFSC)
#     Resource Assessment and Conservation Engineering (RACE)
#     Midwater Assessment and Conservation Engineering (MACE)

#  THIS SOFTWARE AND ITS DOCUMENTATION ARE CONSIDERED TO BE IN THE PUBLIC DOMAIN
#  AND THUS ARE AVAILABLE FOR UNRESTRICTED PUBLIC USE. THEY ARE FURNISHED "AS
#  IS."  THE AUTHORS, THE UNITED STATES GOVERNMENT, ITS INSTRUMENTALITIES,
#  OFFICERS, EMPLOYEES, AND AGENTS MAKE NO WARRANTY, EXPRESS OR IMPLIED,
#  AS TO THE USEFULNESS OF THE SOFTWARE AND DOCUMENTATION FOR ANY PURPOSE.
#  THEY ASSUME NO RESPONSIBILITY (1) FOR THE USE OF THE SOFTWARE AND
#  DOCUMENTATION; OR (2) TO PROVIDE TECHNICAL SUPPORT TO USERS.

"""
.. module:: MACETrawlEvent

    :synopsis: MACETrawlEvent implements the trawl event form used by the
               MACE group to collect metadata associated with the fishing
               operation. The form and code define the data to be collected
               and how and when it is collected.
               
               Events that retain catch (such as a trawl event) are the first
               step in collecting data with CLAMS.
               
| Developed by:  Rick Towler   <rick.towler@noaa.gov>
|                Kresimir Williams   <kresimir.williams@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assesment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
|       Kresimir Williams   <kresimir.williams@noaa.gov>
|       Mike Levine   <mike.levine@noaa.gov>
|       Nathan Lauffenburger   <nathan.lauffenburger@noaa.gov>
"""


from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from ui.xga import ui_MACETrawlEvent
import numpad
import keypad
import messagedlg
import listseldialog
import netdlg
import timedlg
from acquisition.scs import QSCSClient


class MACETrawlEvent(QDialog, ui_MACETrawlEvent.Ui_MACETrawlEvent):


    def __init__(self, parent=None):
        '''
            The CLAMS Trawl event dialog initialization method. This method will
            set some default attributes, connect signals, and perform some other
            basic setup tasks. It then fires off a single shot timer to continue
            init in a separate method.
        '''

        #  call superclass init methods and GUI form setup method
        super().__init__(parent)
        self.setupUi(self)
        
        self.setAttribute(Qt.WA_DeleteOnClose)

        #  copy some properties from our parent
        self.db = parent.db
        self.schema = parent.schema
        self.activeEvent=parent.activeEvent
        self.survey=parent.survey
        self.ship=parent.ship
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.workStation=parent.workStation
        self.birdStatus=parent.birdStatus
        self.mammalStatus=parent.mammalStatus
        self.testing=parent.testing
        self.reloaded = parent.reloaded

        #  setup reoccurring dialogs
        self.numpad = numpad.NumPad(self)
        self.message = messagedlg.MessageDlg(self)
        self.timeDlg = timedlg.TimeDlg(self)
        self.timeDlg.enableGetTimeButton(False)
        self.netdlg = netdlg.NetDlg(self)

        #  define default variable values
        self.fishingFlag = False
        self.recording = False
        self.abort = False
        self.displayMeasurements = ['Latitude', 'Longitude', 'BottomDepth']
        self.gearKey = []
        self.comment = ""
        self.incomplete = False
        self.gaCBList = [self.accessBox1, self.accessBox2, self.accessBox3,
                self.accessBox4]
        self.gaLabelList = [self.accessLabel1, self.accessLabel2,
                self.accessLabel3, self.accessLabel4]
        self.buttons=[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5
                ,self.btn6,self.btn7,self.btn8,self.btn9]
        self.eventTimer=QTime()
        self.recordStream=False
        self.dispVector=['','','']
        self.SCSPollRate = 1
        self.reloaded = False
        self.scsRetries = 0

        #  max number of seconds data extracted from haul_stream_data during event button edits
        #  are allow to differ from the new event time. This is the half window size. The closest
        #  value to the edit time within this window is used.
        self.streamWindowSeconds = 5

        #  set the SCS logging rate default values
        self.streamEQHBLogInterval = 2
        self.streamSlowLogInterval = 5
        self.SCSLogInterval = self.streamSlowLogInterval

        #  set the SCS "last write" time used to track SCS logging interval
        self.lastSCSWriteTime = QDateTime.currentDateTime()

        # color palettes
        self.red=QPalette()
        self.red.setColor(QPalette.ButtonText,QColor(230, 0, 0))
        self.green=QPalette()
        self.green.setColor(QPalette.ButtonText,QColor(0, 230, 0))
        self.yellow=QPalette()
        self.yellow.setColor(QPalette.ButtonText,QColor(180, 180, 0))
        self.haulLabel.setText(self.activeEvent)

#TODO: UPDATE SCS CLIENT
        #  create an instance of the SCS client and connect the signals
        self.scsClient = QSCSClient.QSCSClient(self.settings['SCSHost'],
                self.settings['SCSPort'])
        self.scsClient.SCSGetReceived.connect(self.writeStream)
        self.scsClient.SCSError.connect(self.errorSCS)

        #  attempt to connect to the SCS server
        if not self.testing:
            self.setupSCS()

        #  connect the form's signals
        self.gearBox.activated[int].connect(self.getOptions)
        self.perfCheckBox.stateChanged[int].connect(self.getFullPerfList)
        self.netDimBtn.clicked.connect(self.getNetDims)
        self.transBtn.clicked.connect(self.getTransect)
        self.stratumBtn.clicked.connect(self.getStratum)
        self.commentBtn.clicked.connect(self.getComment)
        self.doneBtn.clicked.connect(self.goExit)

        #  now connect the event action button signals
        for btn in self.buttons:
            btn.clicked.connect(self.getEventData)

        # setup table
        self.dataTable.verticalHeader().setVisible(False)
        for i in range(4):
            self.dataTable.setColumnWidth(i, self.dataTable.width()/4)

        #  create a statusbar
        self.statusBar = QStatusBar(self)
        self.statusLayout.addWidget(self.statusBar)

        #  set up the event duration timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.displayTime)

        #  set up the initialization timer
        initTimer = QTimer(self)
        initTimer.setSingleShot(True)
        initTimer.timeout.connect(self.initTrawlEventDialog)
        initTimer.start(0)


    def initTrawlEventDialog(self):
        '''
        initTrawlEventDialog queries out various parameters and LUT data to populate
        the trawl event form with data
        '''

        #  query out the "slow" and "fast" SCS write to database rates. These rates do not affect polling
        #  only the rate at which data is written to event_stream_data. This is done to limit the amount
        #  of data that is written to this table as it is becoming a query performance issue.
        query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema +
                ".application_configuration " + "WHERE ship=" + self.ship + " AND survey=" +
                self.survey + " AND parameter='EventStreamEQHBLogInt'")
        if query.first():
            (val,ok) = query.value(0).toInt()
            if ok:
                self.streamEQHBLogInterval = val
        query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema +
                ".application_configuration WHERE ship=" + self.ship + 
                " AND survey=" + self.survey + " AND parameter='EventStreamPreEQLogInt'")
        if query.first():
            (val,ok) = query.value(0).toInt()
            if ok:
                self.self.streamSlowLogInterval = val

        #  populate the gear combobox
        self.gearBox.setEnabled(True)
        query = QtSql.QSqlQuery("SELECT gear FROM " + self.schema + ".gear WHERE active=1 " +
                "ORDER BY gear_gui_order", self.db)
        while query.next():
            self.gearBox.addItem(query.value(0).toString())
        self.gearBox.setCurrentIndex(-1)

        # if this is a restart or continuation of an already started event, reload previously collected data
        query=QtSql.QSqlQuery("SELECT * FROM " + self.schema + ".events WHERE ship=" + self.ship +
                " AND survey=" + self.survey + " AND event_id=" + self.activeEvent)
        if query.first():
            #  this is a restart so reload any existing data
            self.reloaded = True
            self.reloadData()
        else:
            #  this is a new event - get scientist
            trawlSci = self.getScientistName('Identify the trawl scientist, please.')
            if trawlSci:
                #  sci selected
                self.scientist = trawlSci
                self.sciLabel.setText(self.scientist)
            else:
                #  scientist selection aborted - exit
                self.abort = True
                self.close()

#        # update the form with the marine mammal interaction status
#        if self.mammalStatus=='Y':
#            self.marMammalBox.setChecked(True)
#        else:
#            self.marMammalBox.setChecked(False)
#        if self.birdStatus=='Y':
#            self.seaBirdBox.setChecked(True)
#        else:
#            self.seaBirdBox.setChecked(False)



    def getScientistName(self, dialogMessage):
        '''
        getScientistName displays a list of active scientists and returns
        the selected individual
        '''
        
        sciName = None
        
        query=QtSql.QSqlQuery("SELECT personnel.scientist FROM " + self.schema + ".personnel WHERE " +
                "personnel.active=1 ORDER BY personnel.scientist", self.db)
        # populate scientist list
        self.sciList=[]
        while query.next():
            self.sciList.append(query.value(0).toString())
        #  present the sci selection dialog
        self.listDialog = listseldialog.ListSelDialog(self.sciList, self)
        self.listDialog.label.setText(dialogMessage)
        if self.listDialog.exec():
            #  sci selected
            sciName = self.listDialog.itemList.currentItem().text()

        return sciName


    def getNetDims(self):
        """
        getNetDims is called when the user hits EQ or Haulback or the NetDims button
        """
        #  reload the net dimension values
        self.netdlg.reloadData

        #  display the dialog
        self.netdlg.exec()


    def reloadData(self):
        """
        reloadData populates the form with whatever data exists in the database for this event
        """
        #populate gear type, scientist
        queryOld = QtSql.QSqlQuery("SELECT gear, event_type, performance_code, scientist, comments " +
                    "FROM " + self.schema + ".events WHERE ship=" +self.ship +
                    " AND survey=" + self.survey + " AND event_id=" + self.activeEvent, self.db)
        # get values
        queryOld.first()

        # set event_id gear type
        ind = self.gearBox.findText(queryOld.value(0).toString())
        self.gear=queryOld.value(0).toString()
        self.gearBox.setCurrentIndex(ind)
        self.scientist=queryOld.value(3).toString()
        self.comment=queryOld.value(4).toString()

        #populate lists
        self.getOptions()

        #set up selections
        if queryOld.value(1).toString() in self.typeCode:
            ind=self.typeCode.index(queryOld.value(1).toString())
        else:
            ind=-1
        self.typeBox.setCurrentIndex(ind)
        self.sciLabel.setText(self.scientist)

        # get from short list, otherwise, get full list
        if queryOld.value(2).toString() in self.perfCode:
            ind=self.perfCode.index(queryOld.value(2).toString())
        else:
            self.perfCheckBox.setCheckState(Qt.Checked)
            self.getFullPerfList()
            ind=-1
            if queryOld.value(2).toString() in self.perfCode:
                ind=self.perfCode.index(queryOld.value(2).toString())
        self.perfBox.setCurrentIndex(ind)

        # gear accessories
        for i in range(len(self.accessories)):
            query = QtSql.QSqlQuery("SELECT gear_accessory_option FROM " + self.schema +
                    ".gear_accessory WHERE ship=" + self.ship + " AND survey=" +
                    self.survey + " AND event_id=" + self.activeEvent + " AND gear_accessory='" +
                    self.accessories[i]+"'")
            if query.first():
                self.gaCBList[i].setCurrentIndex(self.gaCBList[i].findText(query.value(0).toString()))

        #get transect
        query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship=" +
                self.ship + " AND survey=" + self.survey + " AND event_id=" + self.activeEvent +
                " AND event_parameter='Transect'")
        if query.first():
            self.transBtn.setText(query.value(0).toString())

        #get report
        query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship="+self.ship+
            " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='Stratum'")
        if query.first():
            self.stratumBtn.setText(query.value(0).toString())

        # reload mar mammal boxes
        query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship="+self.ship+
            " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='MarineMammalPresent'")
        query.first()
        if query.value(0).toString()=='Y':
            self.marMammalBox.setChecked(True)
        else:
            self.marMammalBox.setChecked(False)

        query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship="+self.ship+
            " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='EndangeredSeabirdPresent'")
        query.first()
        if query.value(0).toString()=='Y':
            self.seaBirdBox.setChecked(True)
        else:
            self.seaBirdBox.setChecked(False)

        # reload buttontimes
        row=0
        for btn in self.buttons:
            if btn.text().startsWith('C'):
                g=str(btn.text())
                partition='Codend_'+g[1]
                parameter=[g.split(' ')[1]]
            elif btn.text() in ['EQ', 'Haulback']:
                partition='Codend'
                parameter=[btn.text()]
            else:
                partition='MainTrawl'
                parameter=[btn.text()]

            query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship=" +
                    self.ship + " AND survey=" + self.survey + " AND event_id=" + self.activeEvent +
                    " AND partition='" + partition + "' AND event_parameter='" + parameter[0] + "'")

            if query.first():
                #  update the button's table values
                self.dataTable.setItem(row, 0, QTableWidgetItem(query.value(0).toString()))
                self.btnTimes[row]=QDateTime().fromString(query.value(0).toString(), 'MMddyyyy hh:mm:ss.zzz')
                buttonValues = self.getEventStreamValues(query.value(0).toString(), self.displayMeasurements)
                self.dataTable.setItem(row, 1, QTableWidgetItem(buttonValues[0]))
                self.dataTable.setItem(row, 2, QTableWidgetItem(buttonValues[1]))
                self.dataTable.setItem(row, 3, QTableWidgetItem(buttonValues[2]))
                self.buttons[row].setPalette(self.green)
            row+=1

        self.gearBox.setEnabled(False)
        self.recording=True

        #  check if this event has been completed. Completed is defined as having EQ and Haulback
        #  data. Once an event is completed, we only allow editing and do not collect stream data.
        for i in range(len(self.btnTimes)):
            #  check if either EQ or HB buttons are "empty"
            if self.btnTimes[i]==None and (self.buttons[i].text().endsWith('EQ') or self.buttons[i].text().endsWith('Haulback')):
                #  one of them is not complete - ask if we should consider this a live event
                reply = QMessageBox.question(self, 'Achtung!',"<font size = 14>This haul was not completed. " +
                        "Is this event still taking place?</font>", QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.Yes:
                    #  this event is ongoing - set up for an active event

                    #  determine what SCS logging rate we should use
                    if self.btnTimes[i]==None and self.buttons[i].text().endsWith('EQ'):
                        #  EQ has not been pressed yet
                        self.SCSLogInterval = self.streamSlowLogInterval
                        self.fishingFlag=False
                    else:
                        #  EQ has been pressed, but not HB
                        self.SCSLogInterval = self.streamEQHBLogInterval
                        self.fishingFlag=True

                    #  set other state variables for a "live" event
                    self.reloaded=False
                    self.recordStream=True
                    self.netdlg.reloaded = False
                else:
                    #  this is not a live event - treat this as an edit after the fact
                    self.reloaded=True
                    self.recordStream=False
                break

        #  brute force, but loop through again checking if BOTH EQ and HB have been pressed - if so,
        #  inform the user that they can only edit and not collect new data.
        nCompletedButtons = 0
        for i in range(len(self.btnTimes)):
            if self.btnTimes[i] <> None and (self.buttons[i].text().endsWith('EQ') or self.buttons[i].text().endsWith('Haulback')):
                nCompletedButtons = nCompletedButtons + 1
        if nCompletedButtons == 2:
            QMessageBox.information(self, 'Kipaumbele!',"<font size=14>This haul appears to have been completed. " +
                    "You can only edit it. New time values must be within the original time span of the event. " +
                    "No new stream data will be recorded.</font>", QMessageBox.Ok)


    def getOptions(self):

        self.gear = self.gearBox.currentText()

        # ENABLE BOXES
        self.optionsGroup.setEnabled(True)
        self.buttonsGroup.setEnabled(True)

        #  populate haul type combo box
        query = QtSql.QSqlQuery("SELECT " + self.schema + ".event_types.event_type, " + self.schema +
                ".event_types.description FROM " + self.schema + ".event_types INNER JOIN " + self.schema +
                ".gear_options ON " + self.schema + ".event_types.event_type = " + self.schema +
                ".gear_options.event_type WHERE (((" + self.schema + ".gear_options.gear)='" + self.gear + "')) " +
                "ORDER BY " + self.schema + ".gear_options.haultype_gui_order")
        self.typeBox.setEnabled(True)
        self.typeCode = []
        self.typeBox.clear()
        while query.next():
            self.typeBox.addItem(query.value(1).toString())
            self.typeCode.append(query.value(0).toString())
        self.typeBox.setCurrentIndex(-1)

        #  populate gear performance combo box
        query = QtSql.QSqlQuery("SELECT " + self.schema + ".event_performance.performance_code, " + self.schema +
                ".event_performance.description FROM " + self.schema + ".event_performance INNER JOIN " + self.schema +
                ".gear_options ON " + self.schema + ".event_performance.performance_code = " + self.schema +
                ".gear_options.performance_code WHERE " + "(((" + self.schema + ".gear_options.gear)='" +
                self.gear + "')) ORDER BY " + self.schema + ".gear_options.perf_gui_order")
        self.perfBox.setEnabled(True)
        self.perfCode=[]
        self.perfBox.clear()
        while query.next():
            self.perfBox.addItem(query.value(1).toString())
            self.perfCode.append(query.value(0).toString())
        self.perfBox.setCurrentIndex(-1)

        #  populate the gear accessory combo boxes
        nAccessoryCB = len(self.gaCBList)
        for i in range(nAccessoryCB):
            #  clear existing contents if any
            self.gaCBList[i].clear()
            self.gaCBList[i].setEnabled(False)
            self.gaLabelList[i].clear()
        #  get the accessory types for this gear
        query = QtSql.QSqlQuery("SELECT  " + self.schema + ".gear_accessory_types.gear_accessory, " + self.schema +
                ".gear_accessory_types.description FROM " + self.schema + ".gear_accessory_types INNER JOIN " +
                self.schema + ".gear_options ON " + self.schema + ".gear_accessory_types.gear_accessory = " +
                self.schema + ".gear_options.gear_accessory WHERE ((" + self.schema + ".gear_options.gear)='" +
                self.gear + "');")
        #  loop thru the returned accessory types and populate the combo boxes
        self.accessories = []
        thisAccessoryCB = 0
        while query.next():
            #  check to make sure we don't have too many accessory types for our form
            if thisAccessoryCB == nAccessoryCB:
                #  there are more accessory types than combo boxes on our form
                #  issue a warning to alert user that either the form needs to
                #  be re-tooled or the haul options table needs to be edited so
                #  the number of accessories for this gear type isn't greater
                #  then the number of combo boxes on the form.
                self.message.setMessage(self.errorIcons[0], self.errorSounds[0],
                    "The number of gear accessories for this gear type is greater than the number of gear accessory " +
                    "combo boxes on this form! You will not see all of the gear accessories. Change the form or remove " +
                    "gear accessories from the gear_options table for this gear.",'info')
                self.message.exec()
                break
            #  set the accessory type label
            self.accessories.append(query.value(0).toString())
            self.gaCBList[thisAccessoryCB].setEnabled(True)
            self.gaLabelList[thisAccessoryCB].setText(query.value(0).toString())
            #  query the db for the options for this accessory type
            query1 = QtSql.QSqlQuery("SELECT gear_accessory_option FROM " + self.schema + ".gear_accessory_options WHERE " +
                                   "gear_accessory='" + self.accessories[thisAccessoryCB] + "' and active = 1;")
            #  populate the combo box for this accessory type
            #self.accessories.sort()
            values=[]
            while query1.next():
                if query.value(1).toString()=='int':
                    values.append(int(query1.value(0).toString()))
                elif query.value(1).toString()=='float':
                    values.append(float(query1.value(0).toString()))
                else:
                    values.append(query1.value(0).toString())
            values.sort()
            for val in values:
                self.gaCBList[thisAccessoryCB].addItem(str(val))
            if self.gaCBList[thisAccessoryCB].count()>1:
                self.gaCBList[thisAccessoryCB].setCurrentIndex(-1)
            #  increment the combobox/label counter
            thisAccessoryCB += 1


        maxButtons = len(self.buttons)
        for btn in self.buttons:
            btn.hide()
        # setup the action buttons
        query = QtSql.QSqlQuery("SELECT event_parameter FROM " + self.schema + ".gear_options WHERE gear='" +
                self.gear + "' AND event_parameter IS NOT NULL ORDER BY haultype_gui_order")
        cnt=0
        self.btnTimes=[]
        if not self.reloaded:
            self.recordStream=True
        cntx=1
        while query.next():
            self.buttons[cnt].show()

            #  check if this is gear with multiple codends (and thus multiple EQs)
            if query.value(0).toString() in ['EQ','Haulback']:
                if self.gear in ['MOCC','Tucker']:
                    txt="C" + str(cntx) + " " + query.value(0).toString()
                    if query.value(0).toString() == 'Haulback':
                        cntx+=1
                else:
                    txt=query.value(0).toString()
                self.buttons[cnt].setPalette(self.red)
            else:
                txt=query.value(0).toString()
                self.buttons[cnt].setPalette(self.yellow)
            self.buttons[cnt].setText(txt)

            self.btnTimes.append(None)
            cnt=cnt+1
        self.endbutton=cnt-1
        self.dataTable.setRowCount(maxButtons)

        for i in range (maxButtons):
            self.dataTable.setRowHeight(i, 42)

        self.typeBoxFlag=False
        self.perfBoxFlag=False
        self.accessBox1Flag=False
        self.accessBox2Flag=False
        self.accessBox3Flag=False


    def displayTime(self):
        self.eventTimer=self.eventTimer.addSecs(1)
        self.elapseLabel.setText(self.eventTimer.toString('mm:ss'))


    def getEventStreamValues(self, time, parameters):
        """
        queryEventStreamValues queries the event_data_stream table for the specified parameter
        values at the specified time and returns the value closest to the time. If data is not
        available within the defined time window, empty strings are returned.

        ALL VALUES ARE RETURNED AS STRINGS
        """
        #  check that we've been given a list of one or more params
        if len(parameters) == 0 or not isinstance(parameters,list):
            return ''

        #  set up our default return value
        retVal = [''] * len(parameters)
        dt = [float('inf')] * len(parameters)

        #  convert our time to a QDateTime
        time = QDateTime().fromString(time, 'MMddyyyy hh:mm:ss.zzz')

        #  query the data from haul_stream data table within our window
        inClause = "'" + "','".join(parameters) + "'"
        query=QtSql.QSqlQuery("SELECT time_stamp,measurement_type,measurement_value FROM " + self.schema +
                ".event_stream_data WHERE time_stamp between to_timestamp('"+
                time.addSecs(-self.streamWindowSeconds).toString('MMddyyyy hh:mm:ss.zzz') +
                "','MMDDYYYY HH24:MI:SS.FF3') and to_timestamp('"+
                time.addSecs(self.streamWindowSeconds).toString('MMddyyyy hh:mm:ss.zzz') +
                "','MMDDYYYY HH24:MI:SS.FF3') AND measurement_type IN (" + inClause + ")")

        #  loop thru the returned values
        while query.next():
            try:
                #  get the index into our return array
                i = parameters.index(query.value(1).toString())
                #  calculate the time difference between this row and our specified time
                timeDiff = abs(QDateTime.fromString(query.value(0).toString(), 'MMddyyyy hh:mm:ss.zzz').secsTo(time))
                #  check if this delta is smaller
                if timeDiff < dt[i]:
                    #  difference is smaller, save this value
                    dt[i] = timeDiff
                    retVal[i] = query.value(2).toString()
            except:
                #  this is not the parameter we're looking for
                pass

        return retVal


    def getEventData(self):
        '''
        getEventData is called when an event button is pressed
        '''

        #  if this is the first button pressed, we lock the gear type, write the
        #  initial event record, and set the "recording" state (meaning we've locked
        #  in and are doing this event.)
        if not self.recording:
            self.writeHaulRecord()
            self.timer.start(1000)
            self.gearBox.setEnabled(False)
            self.recording=True

        #  get the index of the event action button that was pressed
        ind=self.buttons.index(self.sender())

        # get correct parameter
        time = str(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss.zzz'))
        lat = self.dispVector[0]
        lon = self.dispVector[1]
        g = str(self.buttons[ind].text())

        #  create a list of evet_data parameters we need to record for this button
        #  This should probably be configured in the database (define a button, then
        #  define the measurements recorded when that button is pressed) but we
        #  aren't doing that. We just hard code the list here so it needs to be
        #  updated if measurements are added.
        #
        #  This is even more messy since we are currently assuming if there is
        #  more than 1 param the others are just lat/lon. 
        
        # 1/10/22 RHT: Added ProtectedSppObsStart/Stop measurements which breaks
        #              the assumptions re: # of parameters and their values. This
        #              needs to be reworked so parameters and matched with values
        #              somehow and the logic doesn't have to be hard coded.
        if self.buttons[ind].text().endsWith('EQ'):

            if self.gear in ['MOCC','Tucker']:
                partition='Codend_'+g[1]
            else:
                partition='Codend'
            parameter=['EQ', 'EQLatitude', 'EQLongitude']
            if not self.reloaded:
                self.fishingFlag=True
                self.SCSLogInterval = self.streamEQHBLogInterval
                self.netdlg.setTime=time

        elif self.buttons[ind].text().endsWith('Haulback'):
            if self.gear in ['MOCC','Tucker']:
                partition='Codend_'+g[1]
            else:
                partition='Codend'
            parameter=['Haulback', 'HBLatitude', 'HBLongitude']
            if not self.reloaded:
                self.fishingFlag=False
                self.SCSLogInterval = self.streamSlowLogInterval
                self.netdlg.setTime=time
        elif self.buttons[ind].text() == 'ProtectedSppObsStart':
            #  create parameter list for the protected spp watch
            partition='MainTrawl'
            parameter=[self.buttons[ind].text(), 'ProtectedSppObserver']
        else:
            partition='MainTrawl'
            parameter=[self.buttons[ind].text()]


        #  check to see if we already have data for this button in the database
        gotVal=False
        query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship=" + self.ship +
                " AND survey=" + self.survey + "AND partition='" + partition + "' AND event_parameter='" + parameter[0] +
                "' AND event_id=" + self.activeEvent)
        if query.first():
            #  a value is already in the database for this button
            gotVal=True

        #  at this point we can be either be in the middle of a new haul or editing a previous haul
        #  we behave differently when editing vs running a new event so we branch here. This logic
        #  could probably be cleaned up a bit (lots of code replication) but it works...

        #  if we're editing a past haul (or continuing a haul after exiting out)
        if self.reloaded:
            if ind>0:
                #  check if we should set the time of the edit time dialog to the existing time for this button
                if self.btnTimes[ind-1]<>None:
                    self.timeDlg.setTime(str(self.btnTimes[ind-1].toString('MMddyyyy hh:mm:ss.zzz')))

            #  if there is already data recorded for this button inform the user they will be overwriting it
            if self.dataTable.item(ind, 0)<>None:
                reply = QMessageBox.question(self, 'Achtung!',"<font size = 14>This will change the button time, " +
                        "and if this is an EQ or HB button the GPS location of this button press. Are you " +
                        "sure you want to do this?</font>", QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.No:
                    #  user cancelled edit - nothing to do
                    return
                else:
                    #  set the time dialog with the existing time for this button
                    self.timeDlg.setTime(str(self.dataTable.item(ind, 0).text()))

            #  show the time select dialog so the user can change the time
            if self.timeDlg.exec():
                #  get the new time from the dialog
                time = self.timeDlg.time

                #  try to get a new lat/lon for the specified time so we can update these values if needed
                self.dispVector = self.getEventStreamValues(time, self.displayMeasurements)

                #  check if we got stream data
                if self.dispVector[0] == '':
                    #  we did not find any data, the time range must be outside the range of the available
                    #  event_stream_data. Warn the user if this is a event action that has stream data
                    #  values in the event_data table (like EQ and HB positions)
                    ok = QMessageBox.warning(self, 'Attenzione!',"<font size=14>The new event time appears to " +
                            "be out of the time span of the original event as no event stream data is " +
                            "available. If you continue, the existing event_data entries for this action will " +
                            "be empty and you will need to fill them manually. Are you SURE you want to do this?</font>",
                            QMessageBox.No | QMessageBox.Yes, QMessageBox.No)

                    if ok == QMessageBox.No:
                        #  user aborted edit
                        return

                #  extract the lat/lon
                lat = self.dispVector[0]
                lon = self.dispVector[1]

                # check if we've already have an entry for this button
                if not gotVal:
                    #  no previous data - insert
                    query=QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, partition, " +
                            "event_parameter, parameter_value) VALUES ("+ self.ship+","+self.survey+"," +
                            self.activeEvent + ",'" + partition + "','" + parameter[0] + "','" + time + "')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())


                    if len(parameter)>1:
                        #  this is an EQ or Haulback button so we insert a GPS location too
                        query=QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, " +
                                "partition, event_parameter, parameter_value) VALUES ("+ self.ship+","+self.survey+
                                ","+self.activeEvent+",'"+partition+"','"+parameter[1]+"','"+ lat+"')")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                        query=QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, " +
                                "partition, event_parameter, parameter_value) VALUES ("+ self.ship+","+
                                self.survey+","+self.activeEvent+",'"+partition+"','"+parameter[2]+"','" + lon+"')")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

                else:
                    #  data exists for this button - update record
                    query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+time+"' WHERE "+
                            "ship="+self.ship+" AND survey="+self.survey+" AND event_id="+self.activeEvent+
                            " AND partition='" + partition + "' AND event_parameter='" + parameter[0]+"'")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

                    if len(parameter)>1:
                        #  this is an EQ or Haulback button so we update the GPS location too
                        query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+lat+
                                "' WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+
                                self.activeEvent+" AND partition='"+partition+ "' AND event_parameter='"+
                                parameter[1]+"'")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                        query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+lon+
                                "' WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+
                                self.activeEvent+" AND partition='"+partition+ "' AND event_parameter='"+
                                parameter[2]+"'")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            else:
                #  user cancelled the time edit dialog - nothing to do
                return
        else:
            #  we're *not* editing a past haul and are currently in the middle of an event

            # check if we've already have an entry for this button
            if gotVal:
                reply = QMessageBox.question(self, 'Achtung!',"<font size = 14>You've already pressed the " +
                        self.buttons[ind].text() + " button, are you sure you want to do this?\n" +
                        "Doing so will overwrite the data in the database with current values.</font>",
                        QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.No:
                    #  user cancelled - nothing to do
                    return

                #  data exists for this button - update record
                query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+time+"' WHERE "+
                        "ship="+self.ship+" AND survey="+self.survey+" AND event_id="+self.activeEvent+
                        " AND partition='" + partition + "' AND event_parameter='" + parameter[0]+"'")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

                #  this code needs to be reworked to generalize it so we're not assuming if there is more than
                #  1 param that the other two are lat/lon.
                if len(parameter)>1:
                    
                    if parameter[1] == 'ProtectedSppObserver':
                        #  this is a protected spp observation start/stop
                        trawlSci = None
                        while not trawlSci:
                            trawlSci = self.getScientistName('Who is performing the watch?')
                            if trawlSci:
                                query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+trawlSci+
                                    "' WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+
                                    self.activeEvent+" AND partition='"+partition+ "' AND event_parameter='"+
                                    parameter[1]+"'")
                                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                            else:
                                #  for now we are forcing the selection
                                QMessageBox.warning(self, 'Achtung!',"<font size = 14>You must select a watch scientist.</font>")
                    else:
                    
                        #  this is an EQ or Haulback button so we update the GPS location too
                        query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+lat+
                                "' WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+
                                self.activeEvent+" AND partition='"+partition+ "' AND event_parameter='"+
                                parameter[1]+"'")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                        query=QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+lon+
                                "' WHERE ship="+self.ship+" AND survey="+self.survey+" AND event_id="+
                                self.activeEvent+" AND partition='"+partition+ "' AND event_parameter='"+
                                parameter[2]+"'")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            else:
                # this is a new record for this button
                query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, " +
                        "partition, event_parameter, parameter_value) VALUES ("+ self.ship+","+self.survey+","+
                        self.activeEvent + ",'" + partition + "','" + parameter[0] + "','" + time+"')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

                #  this is an EQ or Haulback button so we insert a GPS location too
                if len(parameter)>1:
                    if parameter[1] == 'ProtectedSppObserver':
                        #  this is a protected spp observation start/stop
                        trawlSci = None
                        while not trawlSci:
                            trawlSci = self.getScientistName('Who is performing the watch?')
                            if trawlSci:
                                query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, " +
                                "partition, event_parameter, parameter_value) VALUES (" + self.ship + "," + self.survey +
                                ","+self.activeEvent+",'"+partition+"','"+parameter[1]+"','"+ trawlSci+"')")
                                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                            else:
                                #  for now we are forcing the selection
                                QMessageBox.warning(self, 'Achtung!',"<font size = 14>You must select a watch scientist.</font>")
                    else:
                        query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, " +
                                "partition, event_parameter, parameter_value) VALUES (" + self.ship + "," + self.survey +
                                ","+self.activeEvent+",'"+partition+"','"+parameter[1]+"','"+ lat+"')")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                        query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id, " +
                                "partition, event_parameter, parameter_value) VALUES (" + self.ship + ","+self.survey+","+
                                self.activeEvent + ",'"+partition + "','" + parameter[2] + "','" + lon + "')")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            #  display the net dimensions dialog is this was an EQ or HB button press
            if (len(parameter)>1) and (parameter[1] != 'ProtectedSppObserver'):
                QTimer.singleShot(500,self.getNetDims)

        #  reset the event timer
        self.eventTimer.setHMS(0, 0, 0, 0)

        # query data back for validation
        query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship="+
                self.ship+" AND survey="+self.survey+" AND partition='"+  partition+"' AND event_parameter='"+
                parameter[0]+"' AND event_id="+self.activeEvent)

        #  display the data if the query (and this insert/update) was successful
        if query.first():
            self.buttons[ind].setPalette(self.green)
            self.dataTable.setItem(ind, 0, QTableWidgetItem(time))
            self.dataTable.setItem(ind, 1, QTableWidgetItem(self.dispVector[0]))
            self.dataTable.setItem(ind, 2, QTableWidgetItem(self.dispVector[1]))
            self.dataTable.setItem(ind, 3, QTableWidgetItem(self.dispVector[2]))

        #  clear the display values
        self.dispVector=['', '','']


    def getTransect(self):
        self.numpad.msgLabel.setText("Enter transect")
        if not self.numpad.exec():
            return
        self.transBtn.setText(self.numpad.value)


    def getStratum(self):
        self.numpad.msgLabel.setText("Enter Stratum")
        if not self.numpad.exec():
            return
        self.stratumBtn.setText(self.numpad.value)


    def writeHaulRecord(self):
        '''
        writeHaulRecord writes the initial records into the events and event_data tables
        '''
        #  write record to events table
        query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".events (ship,survey,event_id,gear,event_type," +
                "performance_code,scientist,comments) VALUES ("+self.ship+","+self.survey+","+self.activeEvent+
                ",'"+self.gear+ "',0,0,'"+self.scientist+"','"+self.comment+"')")
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
        #  and the initial record to the event_data table
        query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship,survey,event_id,partition," +
                "event_parameter,parameter_value) VALUES ("+ self.ship+","+self.survey+","+self.activeEvent+
                ",'MainTrawl','TrawlScientist','"+self.scientist+"')")
        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())


    def stopStream(self):
        self.timer.stop()
        self.scsClient.disconnect()


    def setupSCS(self):
        '''
        setupSCS starts the process of connecting to SCS and configuring the
        SCS sensor subscriptions
        '''

        #  try to connect to the scs server
        try:
            #  initiate connection with SCS server
            self.scsClient.connect()
        except:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0], "Failed to connect to " +
                "SCS server - check IP and port settings in application configuration!" +
                "If you continue, there will be NO SCS DATA LOGGED during the event.", 'info')
            self.message.exec()
            return

        #  request the sensor descriptions
        self.scsClient.getSensorDescriptions()

        #  the rest of the SCS setup is handled in receiveSCSDescriptions


    def receiveSCSDescriptions(self, data):
        '''
        receiveSCSDescriptions completes the SCS initialization
        '''

        self.sensorList=[]
        self.devices=[]
        self.deviceNames=[]
        self.measureTypes=[]
        badSCSDevices = []

        #  we've received the Sensor Description data - get the keys from the dictionary
        keys = data.keys()
        self.scsSensorList = []
        for k in keys:
            self.scsSensorList.append(k)

        #  now get the list of desired sensors from the database
        query = QtSql.QSqlQuery("SELECT " + self.schema + ".measurement_setup.measurement_type, " + self.schema +
                ".devices.device_id, " + self.schema + ".devices.device_name, " + self.schema +
                ".measurement_setup.device_interface FROM " + self.schema + ".measurement_setup, " +
                self.schema + ".devices " + "WHERE " + self.schema + ".measurement_setup.device_id=" +
                self.schema + ".devices.device_id AND "+ self.schema + ".measurement_setup.workstation_id=" +
                self.workStation+" AND " + self.schema + ".measurement_setup.gui_module='TrawlEvent'")

        while query.next():
            #  get the device name
            deviceName = str(query.value(2).toString())

            #  store our types, device ids, and names
            self.measureTypes.append(query.value(0).toString())
            self.devices.append(query.value(1).toString())
            self.deviceNames.append(deviceName)

            #  check if this is an SCS device
            if query.value(3).toString() == 'SCS':
                #  check if it is available from the server
                if (deviceName in self.scsSensorList):
                    #  device is available
                    self.sensorList.append(deviceName)
                else:
                    #  the device specified in the database is NOT available, note it
                    badSCSDevices.append(deviceName)

        #  report any bad SCS device names
        if (len(badSCSDevices) > 0):
            messageText = ('Error connecting one or more SCS devices. The following SCS device(s) do not exist:<br>' +
                    '     <br>'.join(badSCSDevices) + '<br>Consult with survey and update these sensor names in the DEVICES table.')
            QMessageBox.warning(self, "WARNING", "<font size = 13>" + messageText)

        #  create the SCS subscriptions
        self.scsSubscription = self.scsClient.subscribe(self.sensorList, self.SCSPollRate)


    def writeStream(self, data):
        """
        writeStream is called when we receive data from the SCS client.
        """

        #  update the status bar that SCS is alive
        self.statusBar.showMessage('Connected to SCS', 2000)
        self.scsRetries = 0

        #  check if we're recording data and return if not
        if not self.recordStream:
            return

        #  get the current time
        datetime = QDateTime.currentDateTime()
        time = str(datetime.toString('MMddyyyy hh:mm:ss.zzz'))

        #  iterate thru the the list of SCS sensor datagrams and write to database
        if self.testing:
            self.dispVector=['testlat', 'testlon', 'testdepth']
        else:
            wroteToDb = False
            for sensor, value in data.iteritems():
                try:
                    #  get the index into the sensor list
                    idx = self.deviceNames.index(sensor)

                    # get the measurement type
                    measurement = self.measureTypes[idx]

                    #  get the value
                    val = value['data_value']
                    
                    #  check that we have data for this sensor
                    if val is None or val.strip() == '':
                        continue

                    #  convert Lat/Lon to decimal degrees
                    if measurement in ['Latitude']:
                        val = self.convertDegToDecimalLat(val)
                    if measurement in ['Longitude']:
                        val = self.convertDegToDecimalLon(val)

                    #  check if we need to write this to the database
                    elapsedSecs = self.lastSCSWriteTime.secsTo(datetime)
                    if (elapsedSecs >= self.SCSLogInterval):
                        #  insert into the database
                        QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_stream_data (ship, survey, " +
                                "event_id, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeEvent+"," +
                                self.devices[idx]+",'"+time+"','"+measurement+"','"+val+"')")
                        wroteToDb = True

                    # copy  measurements we use for display in the GUI
                    if measurement in self.displayMeasurements:
                        ind = self.displayMeasurements.index(measurement)
                        self.dispVector[ind] = val

                except:
                    #  this sensor is not in our sensor list so just ignore it.
                    #  This shouldn't ever happen though...
                    pass

            #  update the write time if we wrote to the db
            if wroteToDb:
                self.lastSCSWriteTime = datetime


    def getFullPerfList(self):
        """
        getFullPerfList queries out the full list of gear performance options from the database
        and
        """
        if self.perfCheckBox.checkState():
            query=QtSql.QSqlQuery("SELECT event_performance.performance_code, event_performance.description " +
                    "FROM " + self.schema + ".event_performance ORDER BY event_performance.performance_code DESC")
            self.perfBox.setEnabled(True)
            self.perfCode=[]
            self.perfBox.clear()
            while query.next(): # populate haul type list
                self.perfBox.addItem(query.value(1).toString())
                self.perfCode.append(query.value(0).toString())
            self.perfBox.setCurrentIndex(-1)
            self.perfBoxFlag=False
        else:
            query=QtSql.QSqlQuery("SELECT event_performance.performance_code, event_performance.description FROM "+
                    self.schema + ".event_performance INNER JOIN gear_options ON event_performance.performance_code" +
                    "=gear_options.performance_code WHERE (((gear_options.gear)='"+self.gearBox.currentText()+
                    "')) ORDER BY gear_options.perf_gui_order")
            self.perfBox.setEnabled(True)
            self.perfCode=[]
            self.perfBox.clear()
            while query.next(): # populate performance list
                self.perfBox.addItem(query.value(1).toString())
                self.perfCode.append(query.value(0).toString())
            self.perfBox.setCurrentIndex(-1)
            self.perfBoxFlag=False


    def computeMeans(self):
        '''
        computeMeans computes the mean of various stream
        '''

        #  define the measurements we will be averaging
        inputMeasures=['NetHorizontalOpening', 'NetVerticalOpening', 'TrawlWireOut',
                'HeadRopeDepth', 'SurfaceTemp', 'BottomDepth']

        #  define the partitions to average
        if self.gear in ['MOCC', 'Tucker']:
            #  MOCC and Tucker have 3 codends
            partitions=['Codend_1', 'Codend_2', 'Codend_3']
        else:
            #  everything else has one
            partitions=['Codend']

        #  we will calculate the mean between EQ and Haulback
        parameters=['EQ', 'Haulback']

        #  do this for each partition
        for p in partitions:
            #  get the EQ time
            query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship="+
                    self.ship + " AND survey=" + self.survey + " AND event_id= " + self.activeEvent +
                    " AND partition='" + p + "' AND event_parameter = '" + parameters[0]+"'")
            if not query.first():
                continue
            eqTime=QDateTime().fromString(query.value(0).toString(),  'MMddyyyy hh:mm:ss.zzz')

            #  get the haulback time
            query=QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".event_data WHERE ship="+
                    self.ship + " AND survey=" + self.survey + " AND event_id = " + self.activeEvent +
                    " AND  partition='" + p + "' AND event_parameter = '" + parameters[1]+"'")
            if not query.first():
                continue
            hbTime=QDateTime().fromString(query.value(0).toString(),  'MMddyyyy hh:mm:ss.zzz')

            #  now loop thru the measurements defined above
            for m in inputMeasures:
                #  get all the values for this measurement
                query=QtSql.QSqlQuery("SELECT measurement_value, to_char(time_stamp, 'MMDDYYYY HH24:MI:SS.FF3') " +
                        "FROM " + self.schema + ".event_stream_data WHERE time_stamp between to_timestamp('"+
                        eqTime.addMSecs(-500).toString('MMddyyyy hh:mm:ss.zzz') + "','MMDDYYYY HH24:MI:SS.FF3') " +
                        "and to_timestamp('" + hbTime.addMSecs(500).toString('MMddyyyy hh:mm:ss.zzz') +
                        "','MMDDYYYY HH24:MI:SS.FF3') AND measurement_type='" + m + "'")
                vals=[]
                times=[]
                #  build lists of the values
                while query.next():
                    vals.append(query.value(0).toFloat()[0])
                    times.append(QDateTime().fromString(query.value(1).toString(),  'MMddyyyy hh:mm:ss.zzz'))

                #  if we have values, calculate the mean
                if len(times)>0:
                    totinterval = 0
                    totmean = 0
                    if (len(times) > 1):
                        for i in range(len(times)-1):
                            interval=times[i].secsTo(times[i+1])
                            totinterval+=interval
                            mean=(vals[i]+vals[i+1])/2
                            totmean+=mean*interval
                        if float(totinterval)==0:
                            break
                            return
                        totmean=float(totmean)/float(totinterval)
                    else:
                        #  only one value, not much to do
                        totmean = vals[0]

                    #  check if the average has previously been computed
                    query = QtSql.QSqlQuery("SELECT * FROM " + self.schema + ".event_data WHERE ship=" +
                            self.ship + " AND survey=" + self.survey + " AND event_id=" + self.activeEvent +
                            " AND partition='" + p + "' AND event_parameter='Avg" + m + "'")
                    if m == 'SurfaceTemp': # We have a mismatch where the value in the evat_stream_data table =SurfaceTemp,
                    # but the value in Event_Paremeters is equal to Surfacetemperature,
                    #so we're just assignigning it to the new variable name....
                            m= 'SurfaceTemperature'
                    if query.first():
                        #  it has, update it with the new value
                        query = QtSql.QSqlQuery("UPDATE " + self.schema + ".event_data SET parameter_value='"+
                                str(totmean) + "' WHERE ship=" + self.ship + " AND survey=" +
                                self.survey + " AND event_id=" + self.activeEvent + " AND partition='" + p +
                                "' AND event_parameter='Avg" + m + "'")
                    else:
                        #  it has not, insert the new value
                        query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship,survey," +
                                "event_id, partition, event_parameter, parameter_value) VALUES (" +
                                self.ship + "," + self.survey + "," + self.activeEvent + ",'" + p +
                                "','Avg" + m + "','" + str(totmean) + "')")

                    #  make an entry in the logger
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())


    def errorSCS(self, error):
        '''
        the error argument is an instance of QSCSError defined in QSCSTelnetThread. errCode can be 1
        when we are disconnected from SCS and 2 if there was a parsing error.
        '''
        #  we only really care if we're disconnected. For now we're ignoring parsing errors, though
        #  maybe they should be logged...
        if (error.errCode == 1):
            self.statusBar.showMessage('WARNING - Connection to SCS lost. Trying to reconnect...', 2500)
            self.dispVector=['', '', '']

            self.retrySCSConnect()


    def retrySCSConnect(self):
        '''
        retrySCSConnect is called via timer when we lose connection to SCS and
        tries to re-connect to the SCS server.
        '''

        #  increment the retry counter
        self.scsRetries = self.scsRetries + 1

        #  pop a dialog if this issue has gone on too long
        if (self.scsRetries == 10):
            QMessageBox.warning(self, "WARNING", "<font size = 13> Unable to reestablish connection to SCS server. "+
                    "I will continue to try, and please continue the trawl event, but be aware that there " +
                    "most likely are other issues and there will be a bit of a mess to clean up. " +
                    "You may need to use the SQL log files and SCS data files to rebuild the event.")

        try:
            #  initiate connection with SCS server
            self.scsClient.connect()
        except:
            #  couldn't connect - show a warning and retry
            self.statusBar.showMessage('WARNING - Connection to SCS lost. Trying to reconnect...', 2500)

            #  set up the retry timer
            retryTimer = QTimer(self)
            retryTimer.setSingleShot(True)
            self.connect(retryTimer, SIGNAL("timeout()"), self.retrySCSConnect)
            retryTimer.start(5000)


    def getComment(self):
        keyDialog = keypad.KeyPad(self.comment, self)
        keyDialog.exec()
        if keyDialog.okFlag:
            #  get the text and convert to plain text
            self.commentstr=keyDialog.dispEdit.toPlainText()
            string=str(keyDialog.dispEdit.toPlainText())
            #  strip the newlines
            string = string.split('\n')
            #  combine into one long string
            self.comment = ' '.join(string)
            #  replace quotes which will cause issues with out SQL strings
            self.comment = self.comment.replace("'", "`")
            self.comment = self.comment.replace('"', '`')

            #  check if an entry for this event exists yet. This needs to be done
            #  because comments can be made before an event is created.
            query = QtSql.QSqlQuery("SELECT event_id FROM " + self.schema + ".events WHERE ship="+
                    self.ship + " AND survey=" + self.survey + " AND event_id= " + self.activeEvent)
            if query.first():
                #  the event exists, update the comment
                if self.comment <> '':
                    query = QtSql.QSqlQuery("UPDATE " + self.schema + ".events SET comments = '"+ self.comment+
                        "' WHERE ship="+self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeEvent)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())



    def goExit(self):
        self.close()


    def exitCheck(self):
        '''
        exitCheck warns the user if any required form elements are not filled in
        '''
        self.incomplete = False
        incompleteElements = []

        # check if any buttons were NOT selected
        if self.fishingFlag:
            incompleteElements.append('Haulback Button')
            self.incomplete = True

        if  self.perfBox.currentIndex()==-1:
            incompleteElements.append('Gear Performance')
            self.incomplete = True

        if  self.typeBox.currentIndex()==-1:
            incompleteElements.append('Event Type')
            self.incomplete = True

        if str(self.transBtn.text()) == '':
            incompleteElements.append('Transect')
            self.incomplete = True

        if str(self.stratumBtn.text()) == '':
            incompleteElements.append('Stratum')
            self.incomplete = True

        # check if any accessories were NOT selected
        for box in self.gaCBList:
            if box.isEnabled() and box.currentIndex()==-1:# this accessory exists
                ind=self.gaCBList.index(box)
                incompleteElements.append(str(self.gaLabelList[ind].text()))
                self.incomplete = True

        #  we think this form is incomplete - ask the user what they think
        if (self.incomplete):
            messageText = ('It appears that your event form is incomplete.\nThe following fields are missing:\n' +
                    '     \n'.join(incompleteElements) + '\n\nAre you SURE you want to exit without completing it?')
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],messageText,'choice')
            ok = self.message.exec()

            if (ok):
                #  the user disagrees the form is incomplete
                self.incomplete = False


    def convertDegToDecimalLat(self,  deg):

        try:
            dec = float(deg[0:2]) + float(deg[2:-1])/60.
            if deg[-1:] in ['S', 'W']:
                dec = dec * -1
        except:
            dec=''
        return str(dec)


    def convertDegToDecimalLon(self,  deg):

        try:
            dec = float(deg[0:3]) + float(deg[3:-1])/60.
            if deg[-1:] in ['S', 'W']:
                dec = dec * -1
        except:
            dec=''
        return str(dec)


    def closeEvent(self, event):
        '''
        closeEvent is called when the window is closed or the "Done" button is pressed.
        '''

        #  check if gear has been selected - this check is different from the others
        #  since if gear has not been selected, there isn't an entry in the database
        #  for this event.
        if not self.recording:
            messageText = ('You have not started your event. If you exit now, no event will be created. ' +
                    '\n\nAre you sure you want to exit?')
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0],messageText,'choice')
            ok = self.message.exec()
            if (ok):
                #  user has chosen to exit
                self.abort = True

        if (not self.abort):

            #  check the rest of the form for completeness
            self.exitCheck()

            #  if the user agrees it is incomplete - go back to the form
            if self.incomplete:
                event.ignore()
                return

            #  stop recording stream data
            if not self.reloaded:
                self.stopStream()

            # update haul type
            query = QtSql.QSqlQuery("UPDATE events SET event_type = "+self.typeCode[self.typeBox.currentIndex()]+
                    " WHERE ship="+self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeEvent)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # update performance
            if  self.perfBox.currentIndex() != -1:
                query = QtSql.QSqlQuery("UPDATE events SET performance_code = " +
                        self.perfCode[self.perfBox.currentIndex()]+" WHERE ship="+self.ship+
                        " AND survey="+self.survey+" AND event_id="+self.activeEvent)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # update comment
            if self.comment <> '':
                query = QtSql.QSqlQuery("UPDATE " + self.schema + ".events SET comments = '"+self.comment+
                    "' WHERE ship="+self.ship+
                    " AND survey="+self.survey+" AND event_id="+self.activeEvent)
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            #delete current records if they exist
            query = QtSql.QSqlQuery("DELETE FROM " + self.schema + ".event_data WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='Transect'")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            query = QtSql.QSqlQuery("DELETE FROM " + self.schema + ".event_data WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='Stratum'")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            query = QtSql.QSqlQuery("DELETE FROM " + self.schema + ".event_data WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='MarineMammalPresent'")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            query = QtSql.QSqlQuery("DELETE FROM " + self.schema + ".event_data WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND event_parameter='EndangeredSeabirdPresent'")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            query = QtSql.QSqlQuery("DELETE FROM " + self.schema + ".gear_accessory WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeEvent)
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # write transect number
            if str(self.transBtn.text()) != '':
                query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id,partition,  event_parameter,  parameter_value) VALUES "+
                                    " ("+self.ship+","+self.survey+","+self.activeEvent+",'MainTrawl', 'Transect', '"+self.transBtn.text()+"')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # write stratum
            if str(self.stratumBtn.text()) != '':
                query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id,partition,  event_parameter,  parameter_value) VALUES "+
                                    " ("+self.ship+","+self.survey+","+self.activeEvent+",'MainTrawl', 'Stratum', '"+self.stratumBtn.text()+"')")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # write checkboxes
            if self.marMammalBox.isChecked():
                status='Y'
            else:
                status='N'
            query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id,partition,  event_parameter,  parameter_value) VALUES "+
                                    " ("+self.ship+","+self.survey+","+self.activeEvent+",'MainTrawl', 'MarineMammalPresent','"+status+"')")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            if self.seaBirdBox.isChecked():
                status='Y'
            else:
                status='N'
            query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".event_data (ship, survey, event_id,partition,  event_parameter,  parameter_value) VALUES "+
                                    " ("+self.ship+","+self.survey+","+self.activeEvent+",'MainTrawl', 'EndangeredSeabirdPresent','"+status+"')")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            # write accessories
            for accessory in self.gaLabelList:
                if (self.gaCBList[self.gaLabelList.index(accessory)].currentIndex() > -1):
                    value = self.gaCBList[self.gaLabelList.index(accessory)].currentText()
                    query = QtSql.QSqlQuery("INSERT INTO " + self.schema + ".gear_accessory (ship, survey, event_id," +
                            "gear_accessory, gear_accessory_option) VALUES ("+self.ship+","+self.survey+","+
                            self.activeEvent+",'"+accessory.text()+"','"+value+"')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

            #  update the active event
            query = QtSql.QSqlQuery("UPDATE " + self.schema + ".application_configuration SET parameter_value=" +
                            self.activeEvent + " WHERE parameter='ActiveEvent'")

            self.computeMeans()

        else:
            #  we've aborted this trawl before it began - do nothing
            pass

        event.accept()

