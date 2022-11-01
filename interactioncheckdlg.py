from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_InteractionCheckDlg



class InteractionCheckDlg(QDialog, ui_InteractionCheckDlg.Ui_interactionCheckDlg):

    def __init__(self, db, parent=None):
        super(InteractionCheckDlg, self).__init__(parent)
        self.setupUi(self)
        self.buttons=[self.noBtn1, self.yesBtn1,self.noBtn2, self.yesBtn2 ]

        #  set up signals
        self.connect(self.proceedBtn, SIGNAL("clicked()"), self.proceed)
        self.connect(self.abortBtn, SIGNAL("clicked()"), self.abort)

    def proceed(self):
        """
          Do the haul, interactions are not likely
        """
        if self.checkStuff():
            
            self.returnFlag=False
            self.accept()
    def checkStuff(self):
        check=0
        for btn in self.buttons:
            if btn.isChecked():
                check+=1
        if check<2:
            QMessageBox.critical(self, "ERROR", "<font size = 12> You have to make a choice first!")
            return False
        else:
            return True

    def abort(self):
        """
          Don't do the haul, interactions are possible
        """
        self.returnFlag=True
        self.reject()

    def closeEvent(self, event):
        
        self.returnFlag=True
        self.reject()
