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
.. module:: CLAMSmain

    :synopsis: CLAMSmain is...
               
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

import sys
import os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import messagedlg
import numpad
from ui.xga import ui_CLAMSMain
import CLAMSprocess
import admindlg
import utilitiesdlg
import processdlg
import EventLauncher


class CLAMSMain(QMainWindow, ui_CLAMSMain.Ui_clamsMain):

    def __init__(self, dataSource, schema, user, password, app_paths, parent=None):
        #  initialize the superclasses
        super().__init__(parent)
        
        #  set up the UI
        self.setupUi(self)

        #  define version
        self.version = "V3.0"
        self.testing = False
        
        #  define defaults
        self.backLogger = None

        #  set database credentials
        self.schema = schema
        self.dbName = dataSource
        self.dbUser = user
        self.dbPassword = password
        self.settings = app_paths

        #  setup the application window
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.setGeometry((screen.width() - window.width()) / 2,
                         (screen.height() - window.height()) / 2,
                          window.width(), window.height())

        #  connect signals
        self.trawlEventBtn.clicked.connect(self.launchEvent)
        self.procBtn.clicked.connect(self.processHaul)
        self.utilitiesBtn.clicked.connect(self.utilities)
        self.adminBtn.clicked.connect(self.administration)
        self.exitBtn.clicked.connect(self.goExit)
        
        #  set the base directory path - this is the full path to this application
        self.baseDir = reduce(lambda l,r: l + os.path.sep + r,
                os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
        #  set the window icon
        try:
            self.setWindowIcon(QIcon(self.baseDir + os.sep + 'icons/giant_clam.png'))
        except:
            pass

        #  create a single-shot timer that runs the application initialization code
        #  this allows the application to complete the main window init method before
        #  the rest of the initialization code runs. We do this because we can't
        #  close the main window (as we would if there was an initialization error)
        #  from the window's init method.
        initTimer = QTimer(self)
        initTimer.setSingleShot(True)
        self.connect(initTimer, SIGNAL("timeout()"), self.applicationInit)
        initTimer.start(0)


    def applicationInit(self):
        """
        applicationInit creates a connection to the CLAMS database and sets up the
        CLAMS application depending on how the workstation running the application
        is configured. This method is called only once during QMainWindow::Init via
        a timer so that we can call the main window's close method if we run into
        an error.
        """
        
        #  try to load the background image. This will only work here if ImageDir is
        #  set in the .ini file. We do this so if we have an image, we can display it
        #  here so if the DB connection fails the dialog doesn't look so janky.
        # https://forum.qt.io/topic/1378/is-it-possible-to-set-a-background-image-to-a-widget/13
        if QDir().exists(self.settings['ImageDir']):
            try:
                imFile = (self.settings['ImageDir'] + 'backgrounds' + os.sep +
                        self.version + ".jpg")
                self.parent.setStyleSheet("QMainWindow::background-image:url(" + imFile + ")")
            except:
                pass
        
        #  create an instance of our dbConnection
        self.db = dbConnection.dbConnection(self.dbName, self.dbUser,
                self.dbPassword, label='CLAMS', isOracle=True)

        #  and try to connect
        try:
            self.db.dbOpen()
        except Exception as err:
            #  display the error dialog then close the application
            QMessageBox.critical(self, "Database Login Error", "<font size = 12> Unable " +
                    "to connect to the database.  Does the clams.ini file exist? Are the " +
                    "values in it correct?\n Error text:" + err)
            self.close()
            return

        #  determine our hostname and query database for workstation number
        computerName = os.getenv("COMPUTERNAME")
        sql = ("SELECT workstation_id FROM " + self.schema +
                ".workstations WHERE hostname ='" + computerName + "'")
        query = self.db.dbQuery(sql)
        self.workStation, = query.first()
        
        if self.workStation is None:
            QMessageBox.critical(self, "ERROR", "<font size = 12> Unable to find this " +
                    "computer name (" + computerName + ") in the workstations table. " +
                    "This workstation must be added to and configured in the database " +
                    "before you can run CLAMS on it.")
            self.close()
            return

        #  close station if the application didn't cleanly exit during the last run
        sql = ("SELECT status FROM " + self.schema + ".workstations WHERE workstation_id =" +
                self.workStation)
        query = self.db.dbQuery(sql)
        status, = query.first()
        if status.toLower() == 'open':
            #  the workstation is marked as open so we set it closed
            sql = ("UPDATE " + self.schema + ".workstations SET status='closed' " +
                    "WHERE workstation_ID=" + self.workStation)
            self.db.dbExec(sql)

        #  read in general application settings
        sql = ("SELECT parameter, parameter_value FROM " + self.schema +
                ".application_configuration ")
        query = self.db.dbQuery(sql)
        for parameter, parameter_value in query:
            self.settings.update({parameter:parameter_value})

        # check for a valid Active Survey and Ship
        if not self.settings.has_key(QString('ActiveSurvey')):
            #  no "ActiveSurvey" parameter exists in application_configuration
            QMessageBox.critical(self, "ERROR", "<font size = 12>ActiveSurvey parameter not found in " +
                    "application_configuration table. Please contact your CLAMS administrator " +
                    "to get this issue resolved.")
            self.close()
            return

        #  read in workstation specific settings
        sql = ("SELECT parameter, parameter_value FROM " + self.schema +
                ".workstation_configuration WHERE workstation_ID = " +
                self.workStation)
        query = self.db.dbQuery(sql)
        #  only update missing keys so we don't overwrite any keys from the .ini
        for parameter, parameter_value in query:
            if parameter not in self.settings:
                self.settings.update({parameter:parameter_value})
        
        #  query the db for the active survey and update the ship/survey state variables and the GUI
        self.setActiveSurvey()
        
        #  clean up and check our paths
        if self.settings.has_key('ImageDir'):
            self.settings['ImageDir'], exists = self.checkPath(self.settings['ImageDir'], 'images')
        else:
            self.settings['ImageDir'], exists = self.checkPath(None, 'images')
        if self.settings.has_key('IconDir'):
            self.settings['IconDir'], exists = self.checkPath(self.settings['IconDir'], 'icons')
        else:
            self.settings['IconDir'], exists = self.checkPath(None, 'icons')
        if self.settings.has_key('SoundsDir'):
            self.settings['SoundsDir'], exists = self.checkPath(self.settings['SoundsDir'], 'sounds')
        else:
            self.settings['SoundsDir'], exists = self.checkPath(None, 'sounds')

        #  load background image - try again if we failed earlier
        if not QDir().exists(self.settings['ImageDir']):
             QMessageBox.critical(self, "ERROR", "<font size = 12>Image directory not found. ")
        else:
            imFile = (self.settings['ImageDir'] + 'backgrounds' + os.sep +
                    self.version + ".jpg")
            self.parent.setStyleSheet("QMainWindow::background-image:url(" + imFile + ")")

        #  load error dialog icons
        if not QDir().exists(self.settings['IconDir']):
            QMessageBox.critical(self, "ERROR", "<font size = 12>Icon directory not found. ")
            self.errorIcons = []
        else:
            dialogImage = QImage(self.settings['IconDir'] + "squidworth.jpg")
            errorIcon = QPixmap.fromImage(dialogImage)
            dialogImage = QImage(self.settings['IconDir'] + "spongebob.jpg")
            msgIcon = QPixmap.fromImage(dialogImage)
            dialogImage = QImage(self.settings['IconDir'] + "patrick.jpg")
            overIcon = QPixmap.fromImage(dialogImage)
            dialogImage = QImage(self.settings['IconDir'] + "sandy.jpg")
            okIcon = QPixmap.fromImage(dialogImage)
            self.errorIcons = [errorIcon,  msgIcon,  overIcon, okIcon]

        #  load error sounds
        if not QDir().exists(self.settings['SoundsDir']):
            QMessageBox.warning(self, "ERROR", "<font size = 12>Sound directory not found. " +
                    "CLAMS will operate with generic sounds.")
            self.errorSounds = []
            self.startSound = None
            self.printSound = None
        else:
            self.errorSounds = [QSound(self.settings['SoundsDir'] + 'Error.wav'),
                                QSound(self.settings['SoundsDir'] + 'Ding.wav'),
                                QSound(self.settings['SoundsDir'] + 'Exclamation.wav'),
                                QSound(self.settings['SoundsDir'] + 'Notify.wav'), ]

            #  load opening and printer sounds
            self.startSound = QSound(self.settings['SoundsDir'] + 'opening.wav')
            self.printSound = QSound(self.settings['SoundsDir'] + 'KARATE.wav')

        #  create instances of some of our common dialogs
        self.message = messagedlg.MessageDlg(self)
        self.numDialog = numpad.NumPad(self)

        #  setup local SQL logger - CLAMS creates a local text file that contains all of the SQL transactions
        #  First, normalize the path and make sure we have a trailing separator
        self.settings['LoggingDir'] = os.path.normpath(self.settings['LoggingDir'])
        if (self.settings['LoggingDir'][-1] != '/') or (self.settings['LoggingDir'][-1] != '\\'):
            self.settings['LoggingDir'] = self.settings['LoggingDir'] + os.sep
            
        #  check if the logging directory exists
        if not QDir().exists(self.settings['LoggingDir']):
            reply = QMessageBox.question(self, "ERROR", "<font size = 12>SQL logging directory not found. " +
                    "Do you want to create it?", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                QDir().mkdir(self.settings['LoggingDir'])
            else:
                QMessageBox.critical(self, "ERROR", "<font size = 12>Sorry, CLAMS cannot operate without a " +
                        "SQL logging directory. Goodbye!")
                self.close()
                return

        #  generate the log file name
        loggerFilename = ('CLAMS_' + QDateTime.currentDateTime().toString('MMddyyyy_hhmmss') +
                '_SQL_Backup.log')

        #  and enable dbConnection logging 
        self.db.enableLogging(self.settings['LoggingDir'] + loggerFilename)

        #  Enable only the appropriate actions for this workstation
        try:
            actions = str(self.settings['MainActions'] )
            actions = actions.split(',')
            self.trawlEventBtn.setEnabled(False)
            self.procBtn.setEnabled(False)
            self.adminBtn.setEnabled(False)
            self.utilitiesBtn.setEnabled(False)

            for i in actions:
                if (i.strip().lower() == 'trawl event'):
                    self.trawlEventBtn.setEnabled(True)
                if (i.strip().lower() == 'enter catch'):
                    self.procBtn.setEnabled(True)
                if (i.strip().lower() == 'administration'):
                    self.adminBtn.setEnabled(True)
                if (i.strip().lower() == 'utilities'):
                    self.utilitiesBtn.setEnabled(True)
        except:
            QMessageBox.critical(self, "ERROR", "<font size = 12>Error configuring workstation. " +
                                 "Unable to find this workstation's main actions.")
            self.close()
            return


    def setActiveSurvey(self):
        '''
            setActiveSurvey queries the database for the active ship and survey then
            updates some attributes and the main CLAMS window with the new survey info.
        '''

        #  get the active ship and survey
        sql = ("SELECT parameter_value FROM " + self.schema + ".application_configuration WHERE " +
                "parameter='ActiveSurvey'")
        query = self.db.dbQuery(sql)
        self.survey, = query.first()
        self.settings['ActiveSurvey'] = self.survey
        sql = ("SELECT parameter_value FROM " + self.schema + ".application_configuration WHERE " +
                "parameter='ActiveShip'")
        query = self.db.dbQuery(sql)
        self.ship, = query.first()
        self.settings['ActiveShip'] = self.ship
        
        #  set the version, survey and ship in the main window
        self.titleLabel.setText("<font color=white>CLAMS &nbsp; " + self.version + " </font>")
        self.subtitleLabel.setText("<font color=white>Catch Logger for Acoustic Midwater Surveys</font>")
        
        #  update the ship name in the GUI
        sql = "SELECT name FROM " + self.schema + ".ships WHERE ship=" + self.ship
        query = self.db.dbQuery(sql)
        self.shipName, = query.first()
        self.surveyLabel.setText("<font color=white>Survey: " + self.survey + "</font>")
        self.shipLabel.setText("<font color=white>Ship: " + self.shipName + "</font>")
        self.schemaLabel.setText("<font color=white>Schema: " + self.schema + "</font>")


    def launchEvent(self):
        """
          launchEvent opens up the event launcher allowing the user to select the event
          they want to log.
        """

        eventLauncher = EventLauncher.EventLauncher(self)
        eventLauncher.exec()


    def processHaul(self):
        """
          processHaul is the entry point for all biological processing. 
          
          CLAMS assumes that stations with the haul module enabled will coordinate catch
          processing and so these stations will be presented with the event selection
          dialog when they press the process haul button. The event selected is then set as
          the active event. Other stations will not see the event selection dialog. When
          CLAMSprocess is started on these stations, the active event will be queried from
          the db and used.
          
          IMPORTANT NOTE: CLAMS only queries the active event when the process button is
          pressed. If the haul station starts processing a new event while other stations are
          finishing up the previous event, THE OTHER STATIONS MUST CLOSE THE PROCESS MODULE
          WHEN THEY ARE FINISHED WITH THE PREVIOUS EVENT. If they don't, they will not pick
          up the new active event ID and data from the new event will be entered into the
          previous one.
        """

        #  build a list of the CLAMS modules allowed to run on this workstation
        module_string = self.settings['Modules'].lower()
        module_bits = module_string.split(',')
        self.modules=[]
        for module in module_bits:
            self.modules.append(module.strip())

        #  check is this station is a event entry station
        if not 'haul' in self.modules:
            #  not a event entry station, get active event from the
            #  application_configuration table
            sql = ("SELECT parameter_value FROM " + self.schema +
                    ".application_configuration WHERE parameter='ActiveEvent'")
            query = self.db.dbQuery(sql)
            self.activeEvent, = query.first()
            if self.activeEvent == '0':
                self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                        "There is currently no active event. Please select an event to" +
                        " process from an event processing station.", 'info')
                self.message.exec()
                return

        else:
            # This is a event processing station - first check if we allow the event to
            # be changed when any other stations are open.

            sql = ("SELECT parameter_value FROM " + self.schema + ".application_configuration " +
                    "WHERE parameter='allowEventChangeWhileProcessing'")
            query = self.db.dbQuery(sql)
            allowChange, = query.first()
            if allowChange is None or allowChange.lower() == 'false':
                #  we do not allow a change when other stations are open so check if any are
                stationOpen = False
                sql = "SELECT status FROM " + self.schema + ".workstations"
                query = self.db.dbQuery(sql)
                for status, in query:
                    if sation.lower() == 'open':
                        stationOpen = True
                        break
                if stationOpen:
                    #  This check
                    pass
                    #  one or more CLAMS workstations are open - do not update active ship/survey
                    QMessageBox.critical(self, "ERROR", "<font size = 12>One or more CLAMS workstations "+
                            "are open. The active event cannot be changed when workstations are open. " +
                            "Please close them.")
                    return

            #  get the active event from the database
            sql = ("SELECT parameter_value FROM " + self.schema +
                    ".application_configuration WHERE parameter='ActiveEvent'")
            query = self.db.dbQuery(sql)
            event, = query.first()

            #  get the time the active event came on deck
            sql = ("SELECT parameter_value FROM " + self.schema +
                    ".event_data WHERE event_parameter='Haulback' AND event_id="+
                    event + "AND ship="+self.ship+" AND survey="+self.survey)
            query = self.db.dbQuery(sql)
            eventTime, = query.first()
            if eventTime is None:
                eventTime = ''

            #  present the event selection dialog
            dlg = processdlg.ProcessDlg(event, eventTime, parent=self)
            if dlg.exec():
                event = dlg.activeEvent

                #  check if this event has catch to process

                #  get the gear for the active event
                sql = ("SELECT gear FROM " + self.schema + ".events WHERE ship="+self.ship+
                        " AND survey="+self.survey + " AND event_id=" + event)
                query = self.db.dbQuery(sql)
                gear, = query.first()
            
                #  determine gear type
                sql = "SELECT gear_type FROM gear WHERE gear='" + gear + "'"
                query = self.db.dbQuery(sql)
                gearType, = query.first()
                
                #  and finally check if this gear retains catch
                sql = ("SELECT retains_catch FROM " + self.schema +
                        ".gear_types WHERE gear_type='" + gearType + "'")
                query = self.db.dbQuery(sql)
                retainsCatch, = query.first()

                if not retainsCatch:
                    #  this gear does not have a catch to process, why are we here?
                    QMessageBox.information(self, "Kipaumbele!", "<font size=14>The gear deployed for the " +
                            "event you have selected does not retain catch. Therefore we have nothing to " +
                            "do here. Did you select the correct event?")
                    return

                #  event can have catch - proceed
                self.activeEvent = event

                #  update the active event in the database
                sql = ("UPDATE application_configuration SET parameter_value=" + self.activeEvent +
                        " WHERE parameter='ActiveEvent'")
                self.db.dbExec(sql)
            else:
                return

        #  create the CLAMSProcess window and display it
        procWindow = CLAMSprocess.CLAMSProcess(self) # changed
        procWindow.exec()



    def utilities(self):
        '''
            Display the utilities dialog.
        '''
        dialog = utilitiesdlg.UtilitiesDlg(self)
        dialog.exec()


    def administration(self):
        '''
            Display the administration dialog.
        '''
        dialog = admindlg.AdminDlg(self.db, self)
        dialog.exec()
        self.setActiveSurvey()


    def goExit(self):
        self.close()


    def closeEvent(self, event=None):
        """
        Clean up when the CLAMS main window is closed.
        """
        #  close our connection to the database
        self.db.dbClose()


    def checkPath(self, thisPath, default):
        """
        checkPath cleans up a path and ensures that it has a trailing separator
        and then checks that it exists.
        """

        #  set the default path
        defaultPath =  '.' + os.sep + default + os.sep

        if thisPath is not None:
            #  path provided - normalize the path
            thisPath = os.path.normpath(str(thisPath))

            #  make sure there is a trailing slash
            if (thisPath[-1] != '/') or (thisPath[-1] != '\\'):
                thisPath = thisPath + os.sep
        else:
            thisPath = defaultPath

        #  check for the existence of one of our paths
        if not QDir().exists(thisPath):
            if not QDir().exists(defaultPath):
                return (thisPath, False)
            else:
                return (defaultPath, True)
        else:
            return (thisPath, True)


if __name__ == "__main__":

    #  see if the ini file path was passed in
    if (len(sys.argv) > 1):
        iniFile = sys.argv[1]
        iniFile = os.path.normpath(iniFile)
    else:
        #  no argument provided, use default
        iniFile = 'clams.ini'

    #  create an instance of QSettings to load fundamental CLAMS settings
    initSettings = QSettings(iniFile, QSettings.IniFormat)

    #  extract connection parameters
    dataSource = initSettings.value('ODBC_Data_Source', 'NULL')
    user = initSettings.value('User', 'NULL')
    password = initSettings.value('Password', 'NULL')
    schema = initSettings.value('Schema', 'NULL')
    
    #  extract the application paths
    app_paths = {}
    app_paths['LoggingDir'] = initSettings.value('LoggingDir', './sql_logs')
    app_paths['ImageDir'] = initSettings.value('ImageDir', './images')
    app_paths['SoundsDir'] = initSettings.value('SoundsDir', './sounds')
    app_paths['IconDir'] = initSettings.value('IconDir', './icons')
    
    #  create an instance of QApplication
    app = QApplication(sys.argv)

#TODO: THIS NEEDS TO BE UPDATED TO USE A STYLE SHEET AS app.setGlobalStrut()
#      IS DEPRECATED.

    #  set the minimum GUI element size - We do this to force the scroll bars
    #  to be 40 pixels wide making them easier to use on a touch screen when
    #  wearing gloves
#    https://doc.qt.io/qt-6/stylesheet-examples.html#customizing-qmainwindow
#    https://doc.qt.io/qt-6/stylesheet-examples.html
#    
#    QScrollBar:vertical {
#    width: 40px;
#    height: 20px;
#    }
#    self.setStyleSheet("background-image:url(" + imFile + ")")
#    self.parent.setStyleSheet("QMainWindow::background-image:url(" + imFile + ")")
#    app.setGlobalStrut(QSize(40, 20))

    #  create an instance of the CLAMS main form
    form = CLAMSMain(dataSource, schema, user, password, app_paths, parent=app)

    #  show it
    form.show()

    #  and start the application...
    app.exec()
