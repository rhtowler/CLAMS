
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
from ui.xga import ui_CodendStatusDlg
import numpad


class CodendStatusDlg(QDialog, ui_CodendStatusDlg.Ui_codendStatusDlg):
    def __init__(self, parent=None):
        super(CodendStatusDlg, self).__init__(parent)
        self.setupUi(self)
        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeHaul
        self.activePartition=parent.activePartition
        self.state_value=None
        self.firstName=parent.firstName
        self.errorIcons=parent.errorIcons
        self.errorSounds=parent.errorSounds
        self.message=parent.message
        self.btns=[self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5]
        for btn in self.btns:
            self.connect(btn, SIGNAL("clicked()"), self.getStatus)
        self.exitTimer = QTimer(self)
        self.exitTimer.setSingleShot(True)
        self.connect(self.exitTimer, SIGNAL("timeout()"), self.close)

        
    def getStatus(self):
        btn=self.sender()
        if btn.isChecked():
            self.state_value=btn.text()
            self.exitTimer.start(1000)
            
    def closeEvent(self, event):
        if not self.state_value:
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Sorry " +
                                    self.firstName + ", you need to select a codend state!", 'info')
            self.message.exec_()

