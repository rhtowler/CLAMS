

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import  ui_BasketEditDlg
import numpad

class BasketEditDlg(QDialog, ui_BasketEditDlg.Ui_basketeditDlg):
    def __init__(self, header,  items,  parent=None):
        super(BasketEditDlg, self).__init__(parent)
        self.setupUi(self)
        self.validList=parent.validList
        self.typeDlg=parent.typeDlg
        self.serMonitor=parent.serMonitor
        self.devices=parent.devices
        self.sounds=parent.sounds
        self.errorIcons=parent.errorIcons
        self.errorSounds=parent.errorSounds
        

        self.editBasket.setColumnCount(len(header))
        self.editBasket.setRowCount(1)
        self.editBasket.verticalHeader().setVisible(False)
        self.editBasket.setColumnWidth(0, 150)
        self.editBasket.setColumnWidth(1, 116)
        self.editBasket.setColumnWidth(2, 116)
        self.editBasket.setColumnWidth(3, 116)
        for i in range(len(header)):
            self.editBasket.setHorizontalHeaderItem(i,QTableWidgetItem(header[i]))
            self.editBasket.setItem(0, i, QTableWidgetItem(items[i]))
        self.weight=items[1]
        self.count=items[2]
        self.basketType=items[3]
        self.numpad = numpad.NumPad(self)
        self.connect(self.editBasket, SIGNAL("itemSelectionChanged()"), self.getEdit)
        self.connect(self.okBtn, SIGNAL("clicked()"), self.getOK)
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.getCancel)
        self.connect(self.serMonitor, SIGNAL("SerialDataReceived"), self.getAuto)
        
    
    def getEdit(self):
        col=self.editBasket.currentColumn()
        if col==1:# selected weight
            self.numpad.msgLabel.setText("Punch in the New Weight")
            if not self.numpad.exec_():
                return
            self.weight=self.numpad.value
            self.editBasket.setItem(0, 1, QTableWidgetItem(self.weight))
        elif col==2:
            currentCount=self.editBasket.currentItem().text()
            if currentCount=='-':
                self.basketType="Count"
                self.editBasket.setItem(0, 3, QTableWidgetItem(self.basketType))
            self.numpad.msgLabel.setText("Enter the New Count")
            if not self.numpad.exec_():
                return
            self.count=self.numpad.value
            self.editBasket.setItem(0, 2, QTableWidgetItem(self.count))
        elif col==3:
            self.keep=None
            self.typeDlg.exec_()
            self.basketType=self.typeDlg.basketType
            self.editBasket.setItem(0, 3, QTableWidgetItem(self.basketType))
            if self.basketType=='Count':
                self.count=self.typeDlg.count
                self.editBasket.setItem(0, 2, QTableWidgetItem(self.count))
            else:
                self.count='-'
                self.editBasket.setItem(0, 2, QTableWidgetItem('-'))
                
    def getAuto(self, device, val):
        self.weight=val
        self.editBasket.setItem(0, 1, QTableWidgetItem(self.weight))
        self.transDevice=device
        self.sounds[self.devices.index(device)].play()
        
    def getOK(self):
        self.okFlag=True
        self.done(1) 
        
    def getCancel(self):
        self.okFlag=False
        self.done(1)
