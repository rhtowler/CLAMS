
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_ScaleCardDlg
import numpad


class ScaleCardDlg(QDialog, ui_ScaleCardDlg.Ui_scalecardDlg):
    def __init__(self,  parent=None):
        super(ScaleCardDlg, self).__init__(parent)
        self.card=None
        self.pos=None

        self.setupUi(self)
        
        self.connect(self.cardBtn, SIGNAL("clicked()"), self.getCard)
        self.connect(self.positionBtn, SIGNAL("clicked()"), self.getPosition)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.goExit)
        self.numpad = numpad.NumPad(self)


    def setup(self, parent):
        pass
        
    def getCard(self):
        self.numpad.msgLabel.setText("Punch in the Card number")
        if not self.numpad.exec_():
            return
        self.card=self.numpad.value
        self.cardBtn.setText(self.card)
        
    def getPosition(self):
        self.numpad.msgLabel.setText("Punch in the Card position")
        if not self.numpad.exec_():
            return
        self.pos=self.numpad.value
        self.positionBtn.setText(self.pos)
        
    def goExit(self):
        # exit check
        self.close()
        
    def closeEvent(self, event):
        if not self.card or not self.pos:
            self.reject()
        else:
            self.result = (True, self.card+"_"+self.pos)
            self.accept()
