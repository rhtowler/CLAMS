from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_AdminDlg
import CLAMSedit
import newSurveyDlg
import selectactivesurveydlg


class AdminDlg(QDialog, ui_AdminDlg.Ui_admindlg):

    def __init__(self, db, parent=None):
        super(AdminDlg, self).__init__(parent)
        self.setupUi(self)

        self.db = db

        #  set up signals
        self.connect(self.createSurveyBtn, SIGNAL("clicked()"), self.createClicked)
        self.connect(self.selectSurveyBtn, SIGNAL("clicked()"), self.selectClicked)
        self.connect(self.setupBtn, SIGNAL("clicked()"), self.setupClicked)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.doneClicked)

        self.show()


    def createClicked(self):
        """
          create a new survey.
        """
        self.hide()
        dialog = newSurveyDlg.newSurveyDlg(self.db, parent=self)
        ok = dialog.exec_()

        if ok:
            self.accept()
        else:
            self.show()


    def selectClicked(self):
        """
          Select the active survey.
        """
        self.hide()
        dialog = selectactivesurveydlg.SelectActiveSurveyDlg(self.db, parent=self)
        ok = dialog.exec_()

        if ok:
            self.accept()
        else:
            self.show()

    def setupClicked(self):
        """
          Configure application settings.
        """
        self.hide()
        dialog = CLAMSedit.CLAMSEdit(self)
        ok = dialog.exec_()

        # close the admin dialog
        if ok:
            self.accept()
        else:
            self.show()


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

    form = AdminDlg(db)
    app.exec_()
