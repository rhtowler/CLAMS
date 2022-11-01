
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import  ui_MatSelDlg
import matguide

class MatSelDlg(QDialog, ui_MatSelDlg.Ui_matselDlg):
    def __init__(self,  parent=None):
        super(MatSelDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.db
        self.settings=parent.settings
        self.speciesName=parent.activeSpcName
        # get maturity stage names
        query0=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE lower(species_parameter)='maturity_table' AND species_code="+parent.activeSpcCode)
        if not query0.first():
            return

        query=QtSql.QSqlQuery("SELECT MATURITY_DESCRIPTION.BUTTON_TEXT, "+
                              "MATURITY_DESCRIPTION.DESCRIPTION_TEXT_FEMALE FROM MATURITY_DESCRIPTION, "+
                              "MATURITY_TABLES WHERE ( MATURITY_TABLES.MATURITY_TABLE = "+
                              "MATURITY_DESCRIPTION.MATURITY_TABLE ) and ( MATURITY_TABLES.MATURITY_TABLE = "+query0.value(0).toString()+")")
        maturityBtnText=[]
        while query.next():
            maturityBtnText.append(query.value(0).toString())

        self.connect(self.guideBtn, SIGNAL("clicked()"), self.getGuide)
        self.buttons=[self.mat1Btn, self.mat2Btn, self.mat3Btn, self.mat4Btn, self.mat5Btn, self.mat6Btn, self.mat7Btn, self.mat8Btn]
        for btn in self.buttons:
            self.connect(btn, SIGNAL("clicked()"), self.getMat)
            try:
                btn.setText(maturityBtnText[self.buttons.index(btn)])
            except:
                btn.setText(' -  ')
                btn.setEnabled(False)

    def setup(self, parent):
        pass


    def getMat(self):
        self.result = (True, self.sender().text())
        self.accept()


    def getGuide(self):
        matGuide = matguide.MatGuide(self)
        matGuide.exec_()

    def closeEvent(self, event):

        self.result =  (False, '')
        self.reject()

