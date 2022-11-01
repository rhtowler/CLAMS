
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_MatSelDlgABL


class MatSelDlgABL(QDialog, ui_MatSelDlgABL.Ui_matselDlgABL):
    def __init__(self,  parent=None):
        super(MatSelDlgABL, self).__init__(parent)

        self.setupUi(self)
        
        self.connect(self.immatureBtn, SIGNAL("clicked()"), self.getMaturity)
        self.connect(self.maturingBtn, SIGNAL("clicked()"), self.getMaturity)

    def setup(self, parent):
        pass
        
    def getMaturity(self):
        self.result = (True, self.sender().text())
        self.accept()
    def closeEvent(self, event):

        self.result = (False, '')
        self.reject()