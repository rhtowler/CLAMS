
from PyQt4 import QtCore, QtGui
from ui import ui_ConnectDlg
import dbConnection


class ConnectDlg(QtGui.QDialog, ui_ConnectDlg.Ui_connectDlg):

    def __init__(self, label=None, parent=None):
        #  set up the GUI
        super(ConnectDlg, self).__init__(parent)
        self.setupUi(self)

        self.dbLabel = label

        #  set up signals
        self.connect(self.connectBtn, QtCore.SIGNAL("clicked()"), self.connectClicked)
        self.connect(self.cancelBtn, QtCore.SIGNAL("clicked()"), self.cancelClicked)

        #  create a QSettings object with a (potentially) unique registry key. This allows
        #  different apps to store different creds
        self.regKey = 'ConnectDlg'
        if (label):
            self.regKey = self.regKey + '_' + str(self.dbLabel)
        self.__appSettings = QtCore.QSettings('afsc.noaa.gov', self.regKey)

        # load in bio schema options
        self.schemaBox.addItems(['clamsbase2', 'clams2abl'])

        #  restore the dialog state - NEVER STORE THE PASSWORD
        self.__userName = self.__appSettings.value('username', '').toString()
        self.userName.setText(self.__userName)
        self.__dbName = self.__appSettings.value('dbname', '').toString()
        self.databaseName.setText(self.__dbName)
        self.__password = ''
        self.passwordName.setText(self.__password)
        self.bioSchema = self.__appSettings.value('bioschema', '').toString()
        self.schemaBox.setCurrentIndex(self.schemaBox.findText(self.bioSchema, QtCore.Qt.MatchExactly))


    def connectClicked(self):
        """
          connect to the database.
        """

        #  create the database connection object
        self.db = dbConnection.dbConnection(self.databaseName.text(), self.userName.text(),
                self.passwordName.text(), self.dbLabel)
        self.db.bioSchema=self.schemaBox.currentText()
        try:
            #  attempt to connect to the database
            self.db.dbOpen()
            #  save the updated credentials
            self.__appSettings.setValue('dbName',self.databaseName.text())
            self.__appSettings.setValue('username',self.userName.text())
            self.__appSettings.setValue('bioschema',self.schemaBox.currentText())
            #  accept the event
            self.accept()

        except dbConnection.DBError as e:
            #  ooops, there was a problem
            errorMsg = 'Unable to connect to ' + self.databaseName.text() + '\n' + e.error
            QtGui.QMessageBox.warning(self, "Databse Login Error", errorMsg)
            self.reject()


    def cancelClicked(self):
        """
          Cancel connection.
        """
        self.reject()


