#!/usr/bin/env python
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT
 #ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_LoadCellDialog
import numpad



class LoadCellDialog(QDialog, ui_LoadCellDialog.Ui_loadcellDialog):
    def __init__(self, parent=None):
        super(LoadCellDialog, self).__init__(parent)
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message

        self.setupUi(self)
        self.grossLabel.palette().setColor(self.grossLabel.backgroundRole(), QColor(255, 255, 255))
        self.tareLabel.palette().setColor(self.tareLabel.backgroundRole(), QColor(255, 255, 255))
        self.haulWtLabel.palette().setColor(self.haulWtLabel.backgroundRole(), QColor(255, 255, 255))
        
        self.connect(self.grossBtn, SIGNAL("clicked()"), self.getGross)
        self.connect(self.tareBtn, SIGNAL("clicked()"), self.getTare)  
        self.connect(self.okBtn, SIGNAL("clicked()"), self.goOK)      
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.goExit)    
        
        self.numpad=numpad.NumPad(self)
        
    def getGross(self):
        self.numpad.msgLabel.setText('Enter total bag weight')
        if self.numpad.exec_():
            grossWT=self.numpad.value
            self.grossLabel.setText(grossWT)
            self.tareBtn.setEnabled(True)
    
    def getTare(self):
        self.numpad.msgLabel.setText('Enter empty bag weight')
        if self.numpad.exec_():
            if float(self.numpad.value)>float(self.settings[QString('MaxTareWt')]):
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1], "The Load Cell Tare Weight Exceeds "+self.settings[QString('MaxTareWt')]+".  Does this concern you?", 'choice')
                if self.message.exec_():
                    return
            self.tareLabel.setText(self.numpad.value)
            tareWTnum=float(self.numpad.value)
            grossWTnum=float(self.grossLabel.text())
            haulWT=grossWTnum-tareWTnum
            self.haulWtLabel.setNum(haulWT)
            self.okBtn.setEnabled(True)
    
 
    def goOK(self):
        num=float(self.haulWtLabel.text())
        if self.radioLb.isChecked():
            num=num/2.2046
        num=round(num, 0)
        self.haulWt=str(num)
        self.done(1) 
        
    def goExit(self):
        self.done(0)
    # put code for returning


