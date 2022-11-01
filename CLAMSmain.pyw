
"""
CLAMSmain is the entry point into the CLAMS application. CLAMSmain provides
the GUI form that all other forms are launched from.
"""

#  import packages
import sys
import os
import string
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
import messagedlg
import numpad
from ui.xga import ui_CLAMSMain
import CLAMSprocess
import admindlg
import utilitiesdlg
import processdlg
import logging
import logging.handlers
import EventLauncher

class CLAMSMain(QMainWindow, ui_CLAMSMain.Ui_clamsMain):

    def __init__(self, dataSource, schema, user, password, app_paths, parent=None):
        #  initialize the superclasses
        super(CLAMSMain, self).__init__(parent)
        self.setupUi(self)

        #  define version
        self.version = "V2.7"
        self.testing=False # change this for prime time!!
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
        self.connect(self.trawlEventBtn, SIGNAL("clicked()"), self.launchEvent)
        self.connect(self.procBtn, SIGNAL("clicked()"), self.processHaul)
        self.connect(self.utilitiesBtn, SIGNAL("clicked()"), self.utilities)
        self.connect(self.adminBtn, SIGNAL("clicked()"),self.administration)
        self.connect(self.exitBtn, SIGNAL("clicked()"), self.goExit)


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
        pic = QImage()
        if QDir().exists(self.settings[QString('ImageDir')]):
            try:
                imFile = str(self.settings[QString('ImageDir')] + 'backgrounds' + os.sep + self.version + ".jpg")
                if pic.load(imFile):
                    pic = pic.scaledToHeight(750, Qt.SmoothTransformation)
                    self.picLabel.setPixmap(QPixmap.fromImage(pic))
            except:
                pass
        
        #  establish the database connection
        self.db = QtSql.QSqlDatabase.addDatabase("QODBC")
        self.db.setDatabaseName(self.dbName)
        self.db.setUserName(self.dbUser)
        self.db.setPassword(self.dbPassword)
        self.db.open()
        if (self.db.isOpenError()) or (not self.db.isValid()):
            #  error messages (at least from Oracle/ODBC) have unicode characters so
            #  we strip them here - not elegant but it is sufficient
            msg = self.db.lastError().text().toAscii()
            msg = ''.join(s for s in str(msg) if s in string.printable)

            #  display the error dialog then close the application
            QMessageBox.critical(self, "Database Login Error", "<font size = 12> Unable to connect to the database. " +
                    "Does the clams.ini file exist? Are the values in it correct?\n Error text:" + msg)
            self.close()
            return

        # set the date format for our session
        sql="alter session set NLS_TIMESTAMP_FORMAT='MMDDYYYY HH24:MI:SS.FF3'"
        self.db.exec_(sql)

        #  determine our hostname and query database for workstation number
        computerName = os.getenv("COMPUTERNAME")
        query = QtSql.QSqlQuery("SELECT workstation_id FROM " + self.schema + ".workstations WHERE hostname ='" +
                                computerName + "'", self.db)
        if not query.first():
            QMessageBox.critical(self, "ERROR", "<font size = 12> Unable to find this computer name (" +
                    computerName + ") in the workstations table. This workstation must be added to and configured " +
                    "in the database before you can run CLAMS on it.")
            self.close()
            return
        else:
            self.workStation = query.value(0).toString()

        #  close station if the application didn't cleanly exit during the last run
        query = QtSql.QSqlQuery("SELECT status FROM " + self.schema + ".workstations WHERE workstation_id =" +
                self.workStation)
        query.first()
        if query.value(0).toString().toLower() == 'open':
            QtSql.QSqlQuery("UPDATE " + self.schema + ".workstations SET status='closed' " +
                    "WHERE workstation_ID=" + self.workStation)

        #  read in general application settings
        query = QtSql.QSqlQuery("SELECT parameter, parameter_value FROM " + self.schema +
                ".application_configuration " , self.db)
        while query.next():
            self.settings.update({query.value(0).toString():query.value(1).toString()})

        # check for a valid Active Survey and Ship
        if not self.settings.has_key(QString('ActiveSurvey')):
            #  no "ActiveSurvey" parameter exists in application_configuration
            QMessageBox.critical(self, "ERROR", "<font size = 12>ActiveSurvey parameter not found in " +
                                 "application_configuration table. Please contact your CLAMS administrator " +
                                 "to get this issue resolved.")
            self.close()
            return

        #  read in workstation specific settings
        query = QtSql.QSqlQuery("SELECT parameter, parameter_value FROM " + self.schema + ".workstation_configuration " +
                                "WHERE workstation_ID = " + self.workStation, self.db)
        #  only update missing keys so we don't overwrite any keys from the .ini
        while query.next():
            if query.value(0).toString() not in self.settings:
                self.settings.update({query.value(0).toString():query.value(1).toString()})
        
        #  query the db for the active survey and update the ship/survey state variables and the GUI
        self.setActiveSurvey()
        
        #  clean up and check our paths
        if self.settings.has_key(QString('ImageDir')):
            self.settings[QString('ImageDir')], exists = self.checkPath(self.settings[QString('ImageDir')], 'images')
        else:
            self.settings[QString('ImageDir')], exists = self.checkPath(None, 'images')
        if self.settings.has_key(QString('IconDir')):
            self.settings[QString('IconDir')], exists = self.checkPath(self.settings[QString('IconDir')], 'icons')
        else:
            self.settings[QString('IconDir')], exists = self.checkPath(None, 'icons')
        if self.settings.has_key(QString('SoundsDir')):
            self.settings[QString('SoundsDir')], exists = self.checkPath(self.settings[QString('SoundsDir')], 'sounds')
        else:
            self.settings[QString('SoundsDir')], exists = self.checkPath(None, 'sounds')

        #  load background image - try again if we failed earlier
        pic = QImage()
        if not QDir().exists(self.settings[QString('ImageDir')]):
            QMessageBox.critical(self, "ERROR", "<font size = 12>Image directory not found. ")
        else:
            imFile = str(self.settings[QString('ImageDir')] + 'backgrounds' + os.sep + self.version + ".jpg")
            if pic.load(imFile):
                pic = pic.scaledToHeight(750, Qt.SmoothTransformation)
                self.picLabel.setPixmap(QPixmap.fromImage(pic))

        #  load error dialog icons
        if not QDir().exists(self.settings[QString('IconDir')]):
            QMessageBox.critical(self, "ERROR", "<font size = 12>Icon directory not found. ")
            self.errorIcons = []
        else:
            dialogImage = QImage(self.settings[QString('IconDir')] + "squidworth.jpg")
            errorIcon = QPixmap.fromImage(dialogImage)
            dialogImage = QImage(self.settings[QString('IconDir')] + "spongebob.jpg")
            msgIcon = QPixmap.fromImage(dialogImage)
            dialogImage = QImage(self.settings[QString('IconDir')] + "patrick.jpg")
            overIcon = QPixmap.fromImage(dialogImage)
            dialogImage = QImage(self.settings[QString('IconDir')] + "sandy.jpg")
            okIcon = QPixmap.fromImage(dialogImage)
            self.errorIcons = [errorIcon,  msgIcon,  overIcon, okIcon]

        #  load error sounds
        if not QDir().exists(self.settings[QString('SoundsDir')]):
            QMessageBox.warning(self, "ERROR", "<font size = 12>Sound directory not found. " +
                    "CLAMS will operate with generic sounds.")
            self.errorSounds = []
            self.startSound = None
            self.printSound = None
        else:
            self.errorSounds = [QSound(self.settings[QString('SoundsDir')] + 'Error.wav'),
                                QSound(self.settings[QString('SoundsDir')] + 'Ding.wav'),
                                QSound(self.settings[QString('SoundsDir')] + 'Exclamation.wav'),
                                QSound(self.settings[QString('SoundsDir')] + 'Notify.wav'), ]

            #  load opening and printer sounds
            self.startSound = QSound(self.settings[QString('SoundsDir')] + 'opening.wav')
            self.printSound = QSound(self.settings[QString('SoundsDir')] + 'KARATE.wav')

        #  create instances of some of our common dialogs
        self.message = messagedlg.MessageDlg(self)
        self.numDialog = numpad.NumPad(self)

        #  setup local SQL logger - CLAMS creates a local text file that contains all of the SQL transactions
        if not QDir().exists(self.settings[QString('LoggingDir')]):
            reply=QMessageBox.question(self, "ERROR", "<font size = 12>SQL logging directory not found. " +
                    "Do you want to create it?", QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.Yes:
                QDir().mkdir(self.settings[QString('LoggingDir')])
            else:
                QMessageBox.critical(self, "ERROR", "<font size = 12>Sorry, CLAMS cannot operate without a " +
                        "SQL logging directory. Goodbye!")
                self.close()
                return
        loggerFilename = str('CLAMS_' + QDateTime.currentDateTime().toString('MMddyyyy_hhmmss') + '_SQL_Backup.log')
        self.backLogger=logging.getLogger('SQLBackup')
        self.backLogger.setLevel(logging.INFO)
        logDir = self.settings[QString('LoggingDir')]

        #  normalize the path and make sure we have a trailing separator
        logDir = os.path.normpath(str(logDir))
        if (logDir[-1] <> '/') or (logDir[-1] <> '\\'):
            logDir = logDir + os.sep

        #  create the logger
        handler = logging.handlers.RotatingFileHandler(logDir+loggerFilename, maxBytes=200000, backupCount=5)
        self.backLogger.addHandler(handler)

        #  Enable only the appropriate actions for this workstation
        try:
            actions = str(self.settings[QString('MainActions')] )
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
            updates the main CLAMS window.
        '''

        #  get the active ship and survey
        query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".application_configuration WHERE " +
                "parameter='ActiveSurvey'")
        query.first()
        self.survey = query.value(0).toString()
        self.settings[QString('ActiveSurvey')] = self.survey
        query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".application_configuration WHERE " +
                "parameter='ActiveShip'")
        query.first()
        self.ship = query.value(0).toString()
        self.settings[QString('ActiveShip')] = self.ship

        #  set the version, survey and ship in the main window
        self.titleLabel.setText("<font color=white> CLAMS &nbsp; " + self.version + " </font>")
        self.shipLabel_2.setText("<font color=white> Catch Logger for Acoustic Midwater Surveys </font>")
        query = QtSql.QSqlQuery("SELECT name FROM " + self.schema + ".ships WHERE ship=" + self.ship, self.db)
        query.first()
        self.shipName = query.value(0).toString()
        self.surveyLabel.setText("<font color=white>Survey: " + self.survey + "</font>")
        self.shipLabel.setText("<font color=white>Ship: " + self.shipName + "</font>")
        self.schemaLabel.setText("<font color=white>Schema: " + self.schema + "</font>")


    def launchEvent(self):
        """
          launchEvent opens up the event launcher allowing the user to select the event
          they want to log.
        """

        eventLauncher = EventLauncher.EventLauncher(self)
        eventLauncher.exec_()


    def processHaul(self):
        """
          processHaul is the entry point for all biological processing. If this method is
          run on a event processing station the trawl events are displayed if the user
          selects a event the CLAMSprocess module is started. If this is run on a a station
          that is not configured for event processing, the active event is queried from the db
          and the CLAMSprocess module is started.
        """

        #  build a list of the CLAMS modules allowed to run on this workstation
        string= str(self.settings[QString('Modules')]).lower()
        string = string.split(',')
        self.modules=[]
        for s in string:
            self.modules.append(s.strip().lower())

        #  check is this station is a event entry station
        if not 'haul' in self.modules:
            # not a event entry station, get active event from table
            query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema + ".application_configuration WHERE parameter=" +
                                    "'ActiveEvent'")
            query.first()
            self.activeEvent = query.value(0).toString()
            if (self.activeEvent == '0'):
                self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                        "There is currently no active event. Please select an event to" +
                                        " process from a event processing station.", 'info')
                self.message.exec_()
                return

        else:

            # This is a event processing station - first check that all stations are closed.
            query = QtSql.QSqlQuery()
            query.prepare("SELECT status FROM " + self.schema + ".workstations")
            query.exec_()
            stationOpen = False
            while query.next():
                if query.value(0).toString().toLower() == 'open':
                    stationOpen = True
                    break
            if stationOpen:
                pass
                #  one or more CLAMS workstations are open - do not update active ship/survey
#                QMessageBox.critical(self, "ERROR", "<font size = 12>One or more CLAMS workstations are open. " +
#                                     "The active event cannot be changed when workstations are open. Please " +
#                                     "close them.")
#                return

            # set busy cursor
            #QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

            #  get the active event from the database
            query = QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema +
                    ".application_configuration WHERE parameter='ActiveEvent'")
            query.first()
            event = query.value(0).toString()

            #  get the time the active event came on deck
            query= QtSql.QSqlQuery("SELECT parameter_value FROM " + self.schema +
                    ".event_data WHERE event_parameter='Haulback' AND event_id="+
                    query.value(0).toString() + "AND ship="+self.ship+" AND survey="+self.survey)
            if query.first():
                time=query.value(0).toString()
            else:
                time=''

            #  present the event selection dialog
            dlg = processdlg.ProcessDlg(event, time, parent=self)
            if dlg.exec_():
                event = dlg.activeEvent

                #  check if this event has catch to process

                #  get the gear for the active event
                query = QtSql.QSqlQuery("SELECT gear FROM " + self.schema + ".events WHERE ship="+self.ship+
                        " AND survey="+self.survey + " AND event_id=" + event)
                query.first()
                gear = query.value(0).toString()

                #  determine gear type
                query = QtSql.QSqlQuery("SELECT gear_type FROM gear WHERE gear='" + gear + "'")
                query.first()
                gearType=query.value(0).toString()

                #  and finally check if this gear retains catch
                query = QtSql.QSqlQuery("SELECT retains_catch FROM " + self.schema +
                        ".gear_types WHERE gear_type='" + gearType + "'")
                query.first()
                retainsCatch=query.value(0).toBool()

                if not retainsCatch:
                    #  this gear does not have a catch to process, why are we here?
                    QMessageBox.information(self, "Kipaumbele!", "<font size=14>The gear deployed for the " +
                            "event you have selected does not retain catch. Therefore we have nothing to " +
                            "do here. Maybe you didn't select the correct event?")
                    return

                #  event can have catch - proceed
                self.activeEvent = event

                #  update the active event in the database
                query = QtSql.QSqlQuery("UPDATE application_configuration SET parameter_value =" + self.activeEvent +
                        " WHERE parameter = 'ActiveEvent'")
                self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss') + "," + query.lastQuery())
            else:
                return

        #  create the CLAMSProcess window and display it
        procWindow = CLAMSprocess.CLAMSProcess(self) # changed
        procWindow.exec_()



    def utilities(self):
        '''
            Display the utilities dialog.
        '''
        dialog = utilitiesdlg.UtilitiesDlg(self)
        dialog.exec_()


    def administration(self):
        '''
            Display the administration dialog.
        '''
        dialog = admindlg.AdminDlg(self.db, self)
        dialog.exec_()
        self.setActiveSurvey()


    def goExit(self):
        self.close()


    def closeEvent(self, event=None):
        """
        Clean up when the CLAMS main window is closed.
        """

        #  close the local SQL logger
        if (self.backLogger):
            self.backLogger.handlers[0].close()

        #  close our connection to the database
        self.db.close()


    def checkPath(self, path, default):
        """
        checkPath cleans up a path and ensures that it has a trailing separator
        and then checks that it exists.
        """

        #  set the default path
        defaultPath =  '.' + os.sep + default + os.sep

        if path <> None:
            #  path provided - normalize the path
            path = os.path.normpath(str(path))

            #  make sure there is a trailing slash
            if (path[-1] <> '/') or (path[-1] <> '\\'):
                path = path + os.sep
        else:
            path = defaultPath

        #  check for the existence of one of our paths
        if not QDir().exists(path):
            if not QDir().exists(defaultPath):
                return (path, False)
            else:
                return (defaultPath, True)
        else:
            return (path, True)


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
    dataSource = str(initSettings.value('ODBC_Data_Source', 'NULL').toString())
    user = str(initSettings.value('User', 'NULL').toString())
    password = str(initSettings.value('Password', 'NULL').toString())
    schema = str(initSettings.value('Schema', 'NULL').toString())
    
    #  extract the application paths
    app_paths = {}
    app_paths[QString('LoggingDir')] = str(initSettings.value('LoggingDir', './sql_logs').toString())
    app_paths[QString('ImageDir')] = str(initSettings.value('ImageDir', './images').toString())
    app_paths[QString('SoundsDir')] = str(initSettings.value('SoundsDir', './sounds').toString())
    app_paths[QString('IconDir')] = str(initSettings.value('IconDir', './icons').toString())
    
    #  create an instance of QApplication
    app = QApplication(sys.argv)

    #  set the minimum GUI element size - We do this to force the scroll bars
    #  to be 40 pixels wide making them easier to use on a touch screen when
    #  wearing gloves
    app.setGlobalStrut(QSize(40, 20))

    #  create an instance of the CLAMS main form
    form = CLAMSMain(dataSource, schema, user, password, app_paths)

    #  show it
    form.show()

    #  and start the application...
    app.exec_()
