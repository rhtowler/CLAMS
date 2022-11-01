
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.xga import ui_CollectionsDlg


class CollectionsDlg(QDialog, ui_CollectionsDlg.Ui_collectionsDlg):

    def __init__(self,  activeCollections=[], parent=None):
        super(CollectionsDlg, self).__init__(parent)
        self.setupUi(self)

        # Populate the GUI
	
        self.checkboxes=[self.checkBox_1,self.checkBox_2,self.checkBox_3,
		self.checkBox_4,self.checkBox_5,self.checkBox_6]
	for box in self.checkboxes:
	    box.hide()

        for i, col in enumerate(activeCollections):
            self.checkboxes[i].setText(col)
            self.checkboxes[i].show()

        self.connect(self.printExitButton, SIGNAL("clicked()"),self.goOnward)
        self.connect(self.cancelBtn, SIGNAL("clicked()"),self.goExit)


    def goOnward(self):
        self.accept()


    def goExit(self):
        self.reject()

