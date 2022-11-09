"""
updated November 2022 to PyQt6 and Python 3 by Alicia Billings, NWFSC
specific updates:
- PyQt import statement
- signal/slot connections
- moved variable declarations into __init__
- changed order of functions to put setup first
- added some function explanation
- fixed any PEP8 issues
- added a main to test if works (commented out)
"""

from PyQt6.QtWidgets import *
from ui.xga import ui_ScaleCardDlg
import numpad
from sys import argv


class ScaleCardDlg(QDialog, ui_ScaleCardDlg.Ui_scalecardDlg):
    def __init__(self,  parent=None):
        super(ScaleCardDlg, self).__init__(parent)
        self.setupUi(self)

        # variable declarations
        self.card = None
        self.pos = None
        self.result = ()

        # signal/slot connection
        self.cardBtn.clicked.connect(self.getCard)
        self.positionBtn.clicked.connect(self.getPosition)
        self.doneBtn.clicked.connect(self.goExit)
        self.numpad = numpad.NumPad(self)

    def setup(self, parent):
        pass
        
    def getCard(self):
        self.numpad.msgLabel.setText("Punch in the Card number")
        if not self.numpad.exec():
            return
        self.card = self.numpad.value
        self.cardBtn.setText(self.card)
        
    def getPosition(self):
        self.numpad.msgLabel.setText("Punch in the Card position")
        if not self.numpad.exec():
            return
        self.pos = self.numpad.value
        self.positionBtn.setText(self.pos)
        
    def goExit(self):
        # todo: there should be a check here since they have to enter both...
        # exit check
        self.close()
        
    def closeEvent(self, event):

        if not self.card or not self.pos:
            self.reject()
        else:
            self.result = (True, self.card + "_" + self.pos)
            self.accept()


#"""
if __name__ == "__main__":
    #  create an instance of QApplication
    app = QApplication(argv)
    #  create an instance of the dialog
    form = ScaleCardDlg()
    #  show it
    form.show()
    #  and start the application...
    app.exec()
#"""