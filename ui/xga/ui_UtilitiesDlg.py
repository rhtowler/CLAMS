# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\UtilitiesDlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_utilitiesdlg(object):
    def setupUi(self, utilitiesdlg):
        utilitiesdlg.setObjectName(_fromUtf8("utilitiesdlg"))
        utilitiesdlg.resize(400, 359)
        self.verticalLayout = QtGui.QVBoxLayout(utilitiesdlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.exportFSCSBtn = QtGui.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.exportFSCSBtn.setFont(font)
        self.exportFSCSBtn.setObjectName(_fromUtf8("exportFSCSBtn"))
        self.verticalLayout.addWidget(self.exportFSCSBtn)
        self.setupBtn = QtGui.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.setupBtn.setFont(font)
        self.setupBtn.setObjectName(_fromUtf8("setupBtn"))
        self.verticalLayout.addWidget(self.setupBtn)
        self.loadStreamBtn = QtGui.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.loadStreamBtn.setFont(font)
        self.loadStreamBtn.setObjectName(_fromUtf8("loadStreamBtn"))
        self.verticalLayout.addWidget(self.loadStreamBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneBtn = QtGui.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.verticalLayout.addWidget(self.doneBtn)

        self.retranslateUi(utilitiesdlg)
        QtCore.QMetaObject.connectSlotsByName(utilitiesdlg)

    def retranslateUi(self, utilitiesdlg):
        utilitiesdlg.setWindowTitle(_translate("utilitiesdlg", "CLAMS Utilities", None))
        self.label.setText(_translate("utilitiesdlg", "CLAMS Utilities", None))
        self.exportFSCSBtn.setText(_translate("utilitiesdlg", "Export FSCS files", None))
        self.setupBtn.setText(_translate("utilitiesdlg", "Setup Serial Devices", None))
        self.loadStreamBtn.setText(_translate("utilitiesdlg", "load stream data", None))
        self.doneBtn.setText(_translate("utilitiesdlg", "Done", None))

