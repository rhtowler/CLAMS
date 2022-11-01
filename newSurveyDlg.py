
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_NewSurveyDlg


class newSurveyDlg(QDialog, ui_NewSurveyDlg.Ui_newSurveyDlg):
    def __init__(self, db,  parent=None):
        super(newSurveyDlg, self).__init__(parent)
        self.setupUi(self)

        #  set up the GUI
        self.surveyNumEdit.setInputMask(QString("999990"))
        self.startDateEdit.setDate(QDate.currentDate())
        self.startDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QDate.currentDate())
        self.endDateEdit.setCalendarPopup(True)
        self.connect(self.createBtn, SIGNAL("clicked()"), self.createSurvey)
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.cancelClicked)

        self.db=db
        self.shipNumbers = []

        if not self.db.isOpen():
            self.db.open()

        #  get the list of ships from the database
        query = QtSql.QSqlQuery("SELECT ship, name FROM ships WHERE active=1", self.db)
        while query.next():
            self.shipNumbers.append(query.value(0).toString())
            self.cbShip.addItem(query.value(1).toString())

        #  get the list of personnel from the database
        query = QtSql.QSqlQuery("SELECT scientist FROM personnel", self.db)
        while query.next():
            self.cbChiefSci.addItem(query.value(0).toString())

        #  get the list of sea areas from the database
        query = QtSql.QSqlQuery("SELECT iho_sea_area FROM survey_sea_areas", self.db)
        while query.next():
            self.cbSeaArea.addItem(query.value(0).toString())

        #  get the list of regions from the database
        query = QtSql.QSqlQuery("SELECT region FROM survey_regions", self.db)
        while query.next():
            self.cbRegion.addItem(query.value(0).toString())

        #  get the list of regions from the database
        query = QtSql.QSqlQuery("SELECT port FROM survey_ports WHERE active=1", self.db)
        while query.next():
            self.cbStartPort.addItem(query.value(0).toString())
            self.cbEndPort.addItem(query.value(0).toString())


    def createSurvey(self):

        #  make sure the dates are sane
        if (self.endDateEdit.date() < self.startDateEdit.date()):
            QMessageBox.critical(self, "ERROR", "<font size = 12> The start date is later than the end date. Please fix.")
            return

        #  scrub quotes from our free form strings
        abstract = str(self.abstractEdit.toPlainText()).replace("'",'"')
        surveyName = str(self.surveyNameEdit.text()).replace("'",'"')

        #  extract some of our params
        ship = self.shipNumbers[self.cbShip.currentIndex()]
        surveyNumber = self.surveyNumEdit.text()
        startDate = QDate(self.startDateEdit.date())
        endDate = QDate(self.endDateEdit.date())

        # check that survey doesn't exist
        query = QtSql.QSqlQuery("SELECT survey FROM surveys WHERE ship=" + ship+ " AND survey=" +
                surveyNumber,  self.db)
        if query.first():
            QMessageBox.critical(self, 'Error', 'Error creating survey. Survey already exists in the database.')
            return

        #  insert the new survey
        query = QtSql.QSqlQuery("INSERT INTO surveys (survey,ship,name,chief_scientist,start_date,end_date," +
                "start_port,end_port,sea_area,abstract,region) VALUES ("+ surveyNumber + "," + ship + ",'" +
                surveyName + "','" + self.cbChiefSci.currentText() + "',TO_DATE('" +
                startDate.toString('MM/dd/yyyy')+"','MM/DD/YYYY')," + "TO_DATE('" + endDate.toString('MM/dd/yyyy') +
                "','MM/DD/YYYY'),'" + self.cbStartPort.currentText() + "','" + self.cbEndPort.currentText() +
                "','" + self.cbSeaArea.currentText()+"','" + abstract+ "','" +
                self.cbRegion.currentText() + "')", self.db)

        # check that it was successful
        query = QtSql.QSqlQuery("SELECT survey FROM surveys WHERE ship=" + ship+ " AND survey=" +
                surveyNumber,  self.db)
        if not query.first():
            QMessageBox.critical(self, 'Error', 'Error creating survey. ' + str(query.lastError().text()))
            return

        else:
            QMessageBox.information(self, 'Success', 'Survey created successfully. Remeber to set it as ' +
                    'the active survey if that is your intention.')
        self.accept()


    def cancelClicked(self):
        self.reject()


    def closeEvent(self, event=None):
        self.reject()



