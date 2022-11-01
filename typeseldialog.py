
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import  ui_TypeSelDialog


class TypeSelDialog(QDialog, ui_TypeSelDialog.Ui_typeselDialog):
    def __init__(self, parent=None):
        super(TypeSelDialog, self).__init__(parent)
        self.setupUi(self)
        self.basketType = None
        
        #hide buttons and hook up slots
        for i in range(4):
            exec(str("self.btn_"+str(i)+".hide()"))
            exec(str('self.connect(self.btn_'+str(i)+', SIGNAL("clicked()"), self.selType)'))
        # set it up
        for i in range(len(parent.basketTypes)):
            exec(str("self.btn_"+str(i)+".show()"))
            exec(str("self.btn_"+str(i)+".setText(parent.basketTypes[i])"))
        
        self.numDlg = parent.numpad
        
    def buttonSetup(self, validList):
        self.Type=None
        for i in range(len(validList)):
            if not validList[i]:
                exec(str("self.btn_"+str(i)+".setEnabled(False)"))
            else:
                exec(str("self.btn_"+str(i)+".setEnabled(True)"))
        

    def selType(self):
            self.count=None
            self.basketType=self.sender().text()
            if self.basketType=='Count':
                self.numDlg.msgLabel.setText("Enter Count")
                self.numDlg.exec_()
                if (self.numDlg.value != None):
                    #  get the value from the numpad
                    self.count=self.numDlg.value
                else:
                    # the user cancelled the numpad selection
                    return
            
                       
            self.accept()
            
    def closeEvent(self, event=None):
        if self.basketType==None:
            self.reject()
            pass

