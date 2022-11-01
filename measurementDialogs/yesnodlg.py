
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import  ui_YesNoDlg


class YesNoDlg(QDialog, ui_YesNoDlg.Ui_YesNoDlg):
    def __init__(self,  parent=None):
        super(YesNoDlg, self).__init__(parent)
        self.setupUi(self)
        
        #  connect signals
        self.connect(self.yesBtn, SIGNAL("clicked()"), self.getResponse)
        self.connect(self.noBtn, SIGNAL("clicked()"), self.getResponse)
    
    def setCaption(self, text):
        self.msgLabel.setText(text)
        
    def setup(self, parent):
        pass
        
    def getResponse(self):
        #  return the text 
        self.result =   (True, self.sender().text())
        self.accept()
        
    def closeEvent(self, event):
        
        self.result =   (False, '')
        self.reject()
        

        
 


