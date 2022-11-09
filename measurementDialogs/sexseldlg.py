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
from ui.xga import ui_SexSelDlg
from sys import argv


class SexSelDlg(QDialog, ui_SexSelDlg.Ui_sexselDlg):
    def __init__(self,  parent=None):
        super(SexSelDlg, self).__init__(parent)
        self.setupUi(self)

        # variable declarations
        self.result = ()

        self.maleBtn.clicked.connect(self.getSex)
        self.femaleBtn.clicked.connect(self.getSex)
        self.noneBtn.clicked.connect(self.getSex)
        # todo: add not determined button for nwfsc

    def unsexStatus(self, unsexFlag):
        # todo: is this even called?
        self.noneBtn.setEnabled(unsexFlag)

    def setup(self, parent):
        if 'maturity' in parent.measureType:
            self.noneBtn.setEnabled(False)

    def getSex(self):
        """
        sets the result tuple to access from the calling dialog with the variables
        :return: self.accept the dialog and return
        """
        self.result = (True, self.sender().text())
        self.accept()

    def closeEvent(self, event):
        """
        sets the result tuple to access from the calling dialog
        :return: self.reject and return
        """
        self.result = (False, '')
        self.reject()


"""
if __name__ == "__main__":
    #  create an instance of QApplication
    app = QApplication(argv)
    #  create an instance of the dialog
    form = SexSelDlg()
    #  show it
    form.show()
    #  and start the application...
    app.exec()
"""