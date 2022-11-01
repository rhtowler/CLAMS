# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\ScaleCardDlg.ui'
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

class Ui_scalecardDlg(object):
    def setupUi(self, scalecardDlg):
        scalecardDlg.setObjectName(_fromUtf8("scalecardDlg"))
        scalecardDlg.resize(265, 302)
        self.groupBox = QtGui.QGroupBox(scalecardDlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 241, 261))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cardBtn = QtGui.QPushButton(self.groupBox)
        self.cardBtn.setGeometry(QtCore.QRect(10, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cardBtn.setFont(font)
        self.cardBtn.setObjectName(_fromUtf8("cardBtn"))
        self.positionBtn = QtGui.QPushButton(self.groupBox)
        self.positionBtn.setGeometry(QtCore.QRect(10, 110, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.positionBtn.setFont(font)
        self.positionBtn.setObjectName(_fromUtf8("positionBtn"))
        self.doneBtn = QtGui.QPushButton(self.groupBox)
        self.doneBtn.setGeometry(QtCore.QRect(10, 200, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(scalecardDlg)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(scalecardDlg)
        QtCore.QMetaObject.connectSlotsByName(scalecardDlg)

    def retranslateUi(self, scalecardDlg):
        scalecardDlg.setWindowTitle(_translate("scalecardDlg", "Scale Location", None))
        self.cardBtn.setText(_translate("scalecardDlg", "enter", None))
        self.positionBtn.setText(_translate("scalecardDlg", "enter", None))
        self.doneBtn.setText(_translate("scalecardDlg", "Done", None))
        self.label.setText(_translate("scalecardDlg", "Card Number", None))
        self.label_2.setText(_translate("scalecardDlg", "Card Position", None))
        self.label_3.setText(_translate("scalecardDlg", "Fish Scale Location", None))

