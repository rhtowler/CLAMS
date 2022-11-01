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
from ui.xga import ui_BinDialog
import numpad


class BinDialog(QDialog, ui_BinDialog.Ui_binDialog):
    def __init__(self, parent=None):
        super(BinDialog, self).__init__(parent)
        self.setupUi(self)
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message
       
        
        self.widthLabel.palette().setColor(self.widthLabel.backgroundRole(), QColor(255, 255, 255))
        self.lengthLabel.palette().setColor(self.lengthLabel.backgroundRole(), QColor(255, 255, 255))
        self.depthLabel.palette().setColor(self.depthLabel.backgroundRole(), QColor(255, 255, 255))
        self.haulWtLabel.palette().setColor(self.haulWtLabel.backgroundRole(), QColor(255, 255, 255))
        
        self.density=1
        
        self.widthFlag=False
        self.lengthFlag=False
        self.depthFlag=False
        self.densityFlag=False
        
        self.connect(self.widthBtn, SIGNAL("clicked()"), self.getWidth)
        self.connect(self.lengthBtn, SIGNAL("clicked()"), self.getLength)  
        self.connect(self.depthBtn, SIGNAL("clicked()"), self.getDepth)  
        self.connect(self.densityBtn, SIGNAL("clicked()"), self.getDensity)  
        self.connect(self.compBtn, SIGNAL("clicked()"), self.getCompute)  
        self.connect(self.okBtn, SIGNAL("clicked()"), self.OK)      
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.goExit)   
       
        self.numpad=numpad.NumPad( self ) 
        
    def getWidth(self):
        self.numpad.msgLabel.setText('Enter bin width')
        if self.numpad.exec_():
            width=self.numpad.value
            self.widthLabel.setText(width)
            self.widthFlag=True
    def getLength(self):
        self.numpad.msgLabel.setText('Enter bin length')
        if self.numpad.exec_():
            length=self.numpad.value
            self.lengthLabel.setText(length)
            self.lengthFlag=True
            
    def getDepth(self):
        self.numpad.msgLabel.setText('Enter bin fish level depth')
        if self.numpad.exec_():
            depth=self.numpad.value
            self.depthLabel.setText(depth)
            self.depthFlag=True
            
    def getDensity(self):
        self.numpad.msgLabel.setText('Enter density of fish (if other than 1)')
        if self.numpad.exec_():
            density=self.numpad.value
            self.densityLabel.setText(density)
            self.densityFlag=True
    
    def getCompute(self):
        if not self.widthFlag:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0], " No width was entered! ", 'info')
            self.message.exec_()
            return
        if not self.lengthFlag:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0], " No Length was entered! ", 'info')
            self.message.exec_()
            return
        if not self.depthFlag:
            self.message.setMessage(self.errorIcons[0],self.errorSounds[0], " No Depth was entered! ", 'info')
            self.message.exec_()
            return

        width=self.widthLabel.text().toFloat()
        length=self.lengthLabel.text().toFloat()
        depth=self.depthLabel.text().toFloat()
        density=self.densityLabel.text().toFloat()
        
        self.haulWT=str(round(width[0]*length[0]*depth[0]*density[0]*1000, 0))
        self.haulWtLabel.setText(self.haulWT)
            
    def OK(self):
        self.accept() 
        
    def goExit(self):
        self.reject()
    # put code for returning


