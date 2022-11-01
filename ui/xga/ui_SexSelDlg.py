# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\SexSelDlg.ui'
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

class Ui_sexselDlg(object):
    def setupUi(self, sexselDlg):
        sexselDlg.setObjectName(_fromUtf8("sexselDlg"))
        sexselDlg.resize(264, 239)
        self.groupBox = QtGui.QGroupBox(sexselDlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 241, 191))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.maleBtn = QtGui.QPushButton(self.groupBox)
        self.maleBtn.setGeometry(QtCore.QRect(10, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maleBtn.setFont(font)
        self.maleBtn.setObjectName(_fromUtf8("maleBtn"))
        self.femaleBtn = QtGui.QPushButton(self.groupBox)
        self.femaleBtn.setGeometry(QtCore.QRect(10, 70, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.femaleBtn.setFont(font)
        self.femaleBtn.setObjectName(_fromUtf8("femaleBtn"))
        self.noneBtn = QtGui.QPushButton(self.groupBox)
        self.noneBtn.setGeometry(QtCore.QRect(10, 130, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noneBtn.setFont(font)
        self.noneBtn.setObjectName(_fromUtf8("noneBtn"))
        self.label = QtGui.QLabel(sexselDlg)
        self.label.setGeometry(QtCore.QRect(10, 10, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(sexselDlg)
        QtCore.QMetaObject.connectSlotsByName(sexselDlg)

    def retranslateUi(self, sexselDlg):
        sexselDlg.setWindowTitle(_translate("sexselDlg", "Sex Selection", None))
        self.maleBtn.setText(_translate("sexselDlg", "Male", None))
        self.femaleBtn.setText(_translate("sexselDlg", "Female", None))
        self.noneBtn.setText(_translate("sexselDlg", "Unsexed", None))
        self.label.setText(_translate("sexselDlg", "Select the sex...", None))

