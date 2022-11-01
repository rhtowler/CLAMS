

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_UtilitiesDlg
import streamloaddlg
import devicesetupdlg
#import shutil
#import CLAMSedit
#import eventseldlg
#import fscsload


class UtilitiesDlg(QDialog, ui_UtilitiesDlg.Ui_utilitiesdlg):

    def __init__(self, parent=None):
        super(UtilitiesDlg, self).__init__(parent)
        self.setupUi(self)

        self.db=parent.db
        self.ship=parent.ship
        self.survey=parent.survey
        self.settings=parent.settings
        self.workStation=parent.workStation

        #  set up signals
        #self.connect(self.exportFSCSBtn, SIGNAL("clicked()"), self.createFSCSfiles)
        self.connect(self.loadStreamBtn, SIGNAL("clicked()"), self.loadStreamData)
        self.connect(self.setupBtn, SIGNAL("clicked()"), self.setupDevices)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.doneClicked)
        
        self.exportFSCSBtn.setEnabled(False)
        self.loadStreamBtn.setEnabled(False)

        self.show()


#    def createFSCSfiles(self):
#        '''
#        createFSCSfiles creates a set of csv files that mimic the output of FSCS 1.x
#        '''
#
#        #  get the Haul
#
#        hlDialog = eventseldlg.EventSelDlg(self)
#        hlDialog.newEventBtn.hide()
#        if not hlDialog.exec_():
#            #  user cancelled action
#            return
#
#        self.activeHaul = hlDialog.activeEvent
#        self.doneBtn.setEnabled(False)
#        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
#        FSCSload = fscsload.Fscsload(self)
#        FSCSload.makeFiles()
#        QApplication.restoreOverrideCursor()
#        self.doneBtn.setEnabled(True)
#
#        if (not FSCSload.errormsg == None):
#            QMessageBox.critical(self, "ERROR", "<font size = 10>FSCS file creation failed." + FSCSload.errormsg)
#        else:
#            QMessageBox.information(self, "INFO", "<font size = 10>FSCS files successfully exported to " + FSCSload.folder)


    def setupDevices(self):
        dlg = devicesetupdlg.DeviceSetupDlg(self)
        dlg.exec_()


    def loadStreamData(self):
        '''
        readSCSStreamfiles uploads SCS stream data into clams, in case trawl event hiccups.
        '''

        #  get the Haul
        query = QtSql.QSqlQuery("SELECT HAUL.HAUL, HAUL_DATA.PARAMETER_VALUE FROM HAUL, " +
                                "HAUL_DATA  WHERE HAUL_DATA.SHIP=HAUL.SHIP and HAUL_DATA.SURVEY=HAUL.SURVEY " +
                                "and HAUL_DATA.HAUL=HAUL.HAUL and " +
                                "HAUL_DATA.SHIP = " + self.ship + " and " +
                                "HAUL_DATA.SURVEY = " + self.survey + " and " +
                                "HAUL_DATA.HAUL_PARAMETER='Haulback' and partition in ('Codend','Codend_1')")
        Hauls = []
        EQTimes = []
        while query.next():
            Hauls.append(query.value(0).toString())
            EQTimes.append(query.value(1).toString())

        hlDialog = haulseldialog.HaulSelDialog(Hauls, EQTimes, self.db, self)
        hlDialog.editBtn.setText('Load Stream Data')
        hlDialog.notBtn.hide()
        hlDialog.haulTab.setCurrentIndex(1)
        hlDialog.haulTab.setTabEnabled(0, False)
        if not hlDialog.exec_():
            #  user cancelled action
            return


        self.activeHaul = hlDialog.activeHaul
        loaddlg = streamloaddlg.StreamLoadDlg(self)
        loaddlg.exec_()

    def doneClicked(self):
        self.reject()


    def closeEvent(self, event=None):
        self.reject()



if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)

    db = QtSql.QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName('mbdev')
    db.setUserName('mbdev')
    db.setPassword('pollock')
    db.schema = 'mbdev'
    db.open()

    form = UtilitiesDlg(db)
    app.exec_()
