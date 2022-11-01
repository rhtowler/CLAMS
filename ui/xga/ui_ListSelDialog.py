# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\ListSelDialog.ui'
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

class Ui_listselDialog(object):
    def setupUi(self, listselDialog):
        listselDialog.setObjectName(_fromUtf8("listselDialog"))
        listselDialog.resize(415, 521)
        self.verticalLayout = QtGui.QVBoxLayout(listselDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(listselDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.itemList = QtGui.QListWidget(listselDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.itemList.setFont(font)
        self.itemList.setObjectName(_fromUtf8("itemList"))
        self.verticalLayout.addWidget(self.itemList)
        self.btnFrame = QtGui.QFrame(listselDialog)
        self.btnFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.btnFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.btnFrame.setObjectName(_fromUtf8("btnFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.btnFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exitBtn = QtGui.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.horizontalLayout.addWidget(self.exitBtn)
        self.okBtn = QtGui.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addWidget(self.btnFrame)

        self.retranslateUi(listselDialog)
        QtCore.QMetaObject.connectSlotsByName(listselDialog)

    def retranslateUi(self, listselDialog):
        listselDialog.setWindowTitle(_translate("listselDialog", "Select...", None))
        self.exitBtn.setText(_translate("listselDialog", "Cancel", None))
        self.okBtn.setText(_translate("listselDialog", "OK", None))

