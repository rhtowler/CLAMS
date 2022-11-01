
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_SexSelDlg


class SexSelDlg(QDialog, ui_SexSelDlg.Ui_sexselDlg):
    def __init__(self,  parent=None):
        super(SexSelDlg, self).__init__(parent)

        self.setupUi(self)

        self.connect(self.maleBtn, SIGNAL("clicked()"), self.getSex)
        self.connect(self.femaleBtn, SIGNAL("clicked()"), self.getSex)
        self.connect(self.noneBtn, SIGNAL("clicked()"), self.getSex)

    def unsexStatus(self, unsexFlag):
        self.noneBtn.setEnabled(unsexFlag)

    def setup(self, parent):
        if 'maturity' in parent.measureType:
            self.noneBtn.setEnabled(False)

    def getSex(self):
        self.result = (True, self.sender().text())
        self.accept()

    def closeEvent(self, event):
        self.result = (False, '')
        self.reject()







