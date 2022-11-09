"""
updated November 2022 to PyQt6 and Python 3 by Alicia Billings, NWFSC
specific updates:
- PyQt import statements
- added some function explanation
- fixed any PEP8 issues
- added a main to test if works (commented out)
"""

from PyQt6.QtWidgets import *
from ui.xga import ui_MatSelDlgABL
from sys import argv


class MatSelDlgABL(QDialog, ui_MatSelDlgABL.Ui_matselDlgABL):
    def __init__(self,  parent=None):
        super(MatSelDlgABL, self).__init__(parent)
        self.setupUi(self)

        # variable declarations
        self.result = ()
        
        self.immatureBtn.clicked.connect(self.getMaturity)
        self.maturingBtn.clicked.connect(self.getMaturity)

    def setup(self, parent):
        """
        does nothing
        :param parent: not used in this function
        :return: none
        """
        pass
        
    def getMaturity(self):
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
    form = MatSelDlgABL()
    #  show it
    form.show()
    #  and start the application...
    app.exec()
"""