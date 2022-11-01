# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\TypeSelDialog.ui'
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

class Ui_typeselDialog(object):
    def setupUi(self, typeselDialog):
        typeselDialog.setObjectName(_fromUtf8("typeselDialog"))
        typeselDialog.resize(322, 353)
        self.typeBox = QtGui.QGroupBox(typeselDialog)
        self.typeBox.setEnabled(True)
        self.typeBox.setGeometry(QtCore.QRect(10, 40, 301, 301))
        self.typeBox.setTitle(_fromUtf8(""))
        self.typeBox.setObjectName(_fromUtf8("typeBox"))
        self.btn_0 = QtGui.QPushButton(self.typeBox)
        self.btn_0.setGeometry(QtCore.QRect(10, 10, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setText(_fromUtf8(""))
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.btn_1 = QtGui.QPushButton(self.typeBox)
        self.btn_1.setGeometry(QtCore.QRect(10, 80, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setText(_fromUtf8(""))
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.btn_2 = QtGui.QPushButton(self.typeBox)
        self.btn_2.setGeometry(QtCore.QRect(10, 150, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setText(_fromUtf8(""))
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.btn_3 = QtGui.QPushButton(self.typeBox)
        self.btn_3.setGeometry(QtCore.QRect(10, 220, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setText(_fromUtf8(""))
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.label = QtGui.QLabel(typeselDialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 249, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(typeselDialog)
        QtCore.QMetaObject.connectSlotsByName(typeselDialog)

    def retranslateUi(self, typeselDialog):
        typeselDialog.setWindowTitle(_translate("typeselDialog", "Sample Type", None))
        self.label.setText(_translate("typeselDialog", "Basket Sample Type?", None))

