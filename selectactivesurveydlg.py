from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_SelectActiveSurveyDlg


class SelectActiveSurveyDlg(QDialog, ui_SelectActiveSurveyDlg.Ui_selectactivesurveydlg):

    def __init__(self, db, parent=None):
        super(SelectActiveSurveyDlg, self).__init__(parent)
        self.setupUi(self)

        self.db = db

        #  get the list of ships from the database
        query = QtSql.QSqlQuery("SELECT ship, name FROM ships", self.db)
        self.vesselData = [[],[]]
        while query.next():
            self.vesselData[0].append(query.value(0).toString())
            self.vesselData[1].append(query.value(1).toString())

        #  populate the GUI fields
        self.ship.clear()
        self.ship.addItems(self.vesselData[1])
        self.ship.setCurrentIndex(-1)

        #  set up signals
        self.connect(self.ship, SIGNAL("activated(int)"), self.getSurveys)
        self.connect(self.okBtn, SIGNAL("clicked()"), self.okClicked)
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.cancelClicked)

        #  desensitize survey combo
        self.survey.setEnabled(False)

        #  show the dialog
        self.show()


    def getSurveys(self):

        #  get the ship number of the currently selected ship and populate survey list
        shipIndex = self.ship.currentIndex()
        self.shipNumber = self.vesselData[0][shipIndex]

        #  get the list of surveys and their ships in descending order
        query = QtSql.QSqlQuery("SELECT survey FROM surveys WHERE ship=" + self.shipNumber +
                                " ORDER BY start_date DESC", self.db)
        self.surveyData = []
        while query.next():
            self.surveyData.append(query.value(0).toString())

        self.survey.clear()
        self.survey.addItems(self.surveyData)
        self.survey.setCurrentIndex(-1)

        #  sensitize survey combo
        self.survey.setEnabled(True)


    def okClicked(self):

        #  ensure that a survey has been selected
        selectedIndex = self.survey.currentIndex()
        if (selectedIndex < 0):
            QMessageBox.critical(self, "ERROR", "<font size = 12>Please select a survey or select Cancel.")
            return

        #  make sure that all stations are closed
        query = QtSql.QSqlQuery()
        query.prepare("SELECT status FROM workstations")
        ok = query.exec_()
        if not ok:
            #  there was an error updating the data
            QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to check the status of CLAMS workstations. " +
                                 "Active Survey not changed. " + str(query.lastError().text()))
            return

        stationOpen = False
        while query.next():
            if query.value(0).toString().toLower() == 'open':
                stationOpen = True

        if stationOpen:
            #  one or more CLAMS workstations are open - do not update active ship/survey
            QMessageBox.critical(self, "ERROR", "<font size = 12>One or more CLAMS workstations are open. " +
                                 "The active survey cannot be changed when workstations are open.")

        else:
            #  all stations are closed - update the active ship and survey in the application_configuration table

            #  update the ActiveSurvey setting
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE application_configuration SET PARAMETER_VALUE = '" +
                          self.surveyData[selectedIndex] + "' WHERE PARAMETER='ActiveSurvey'")
            ok = query.exec_()
            if not ok:
                #  there was an error updating the data
                QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to set the active survey. " + str(query.lastError().text()))

            #  update the ActiveShip setting
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE application_configuration SET PARAMETER_VALUE = " +
                          self.shipNumber + " WHERE PARAMETER='ActiveShip'")
            ok = query.exec_()
            if not ok:
                #  there was an error updating the data
                QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to set the active ship. " + str(query.lastError().text()))

            #  zero out the active haul
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE application_configuration SET PARAMETER_VALUE ='0' " +
                          " WHERE PARAMETER='ActiveEvent'")
            ok = query.exec_()


            #  reset the sequences for the new ship/survey combo. This sets the sequence values to whatever is
            #  appropriate for this ship/survey.
            query = QtSql.QSqlQuery()
            ok = query.exec_("CALL reset_sequence_by_survey('baskets', 'basket_id'," + self.shipNumber + "," +
                        self.surveyData[selectedIndex] + ")")
            if not ok:
                #  there was an error executing the stored procedure
                QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to reset basket_id sequence. " +
                        self.__stripErrorChars(query.lastError().text().toAscii()))

            ok = query.exec_("CALL reset_sequence_by_survey('samples', 'sample_id'," + self.shipNumber + "," +
                        self.surveyData[selectedIndex] + ")")
            if not ok:
                #  there was an error executing the stored procedure
                QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to reset sample_id sequence. " +
                        self.__stripErrorChars(query.lastError().text().toAscii()))

            ok = query.exec_("CALL reset_sequence_by_survey('specimen', 'specimen_id'," + self.shipNumber + "," +
                        self.surveyData[selectedIndex] + ")")
            if not ok:
                #  there was an error executing the stored procedure
                QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to reset specimen_id sequence. " +
                        self.__stripErrorChars(query.lastError().text().toAscii()))
            
            #  reset the protected spp event ID sequence - new in 2019
            ok = query.exec_("CALL reset_sequence_by_survey('protected_spp_events', 'event_id'," + self.shipNumber + "," +
                        self.surveyData[selectedIndex] + ")")
            if not ok:
                #  there was an error executing the stored procedure
                QMessageBox.critical(self, "ERROR", "<font size = 12>Unable to reset protected_spp_events event_id sequence. " +
                        self.__stripErrorChars(query.lastError().text().toAscii()))


        # close the dialog
        self.accept()


    def __stripErrorChars(self, rawMsg):
        '''
        stripErrorChars is a simple method to extract the readable text from
        error messages returned by QSqlQuery.
        '''
        msg = []
        for s in rawMsg:
            if (s <> '\x00'):
                msg.append(s)
            else:
                break

        return ''.join(msg)


    def cancelClicked(self):
        self.reject()


    def closeEvent(self, event=None):
        self.reject()


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)

    db = QtSql.QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName('macebase_shop-64')
    db.setUserName('clamsbase2')
    db.setPassword('pollock')
    db.open()

    form = SelectActiveSurveyDlg(db)
    app.exec_()
