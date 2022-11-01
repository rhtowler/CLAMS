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
from ui.xga import ui_ListSelDialog


class ListSelDialog(QDialog, ui_ListSelDialog.Ui_listselDialog):
    def __init__(self, List, Type=None,  parent=None):
        super(ListSelDialog, self).__init__(parent)
        self.setupUi(self)
        self.itemList.addItems(QStringList(List))
        if Type=='Short':
            self.connect(self.itemList, SIGNAL("itemClicked (QListWidgetItem *)"), self.goOn)
            self.btnFrame.hide()
        else:
            self.connect(self.okBtn, SIGNAL("clicked()"),self.goOn)
            self.connect(self.exitBtn, SIGNAL("clicked()"),self.goExit)
        
    def goOn(self):
        self.accept()
    def goExit(self):
        self.reject()



