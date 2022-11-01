# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CLAMS-Python-x64\CLAMS\ui\xga\MessageDlg.ui'
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

class Ui_messageDlg(object):
    def setupUi(self, messageDlg):
        messageDlg.setObjectName(_fromUtf8("messageDlg"))
        messageDlg.resize(750, 415)
        self.msgLabel = QtGui.QLabel(messageDlg)
        self.msgLabel.setGeometry(QtCore.QRect(300, 20, 431, 301))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.msgLabel.setFont(font)
        self.msgLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.msgLabel.setText(_fromUtf8(""))
        self.msgLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.msgLabel.setWordWrap(True)
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))
        self.btn_1 = QtGui.QPushButton(messageDlg)
        self.btn_1.setGeometry(QtCore.QRect(530, 340, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.btn_2 = QtGui.QPushButton(messageDlg)
        self.btn_2.setGeometry(QtCore.QRect(10, 340, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.iconLabel = QtGui.QLabel(messageDlg)
        self.iconLabel.setGeometry(QtCore.QRect(30, 20, 271, 300))
        self.iconLabel.setText(_fromUtf8(""))
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
        self.btn_3 = QtGui.QPushButton(messageDlg)
        self.btn_3.setGeometry(QtCore.QRect(270, 340, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setText(_fromUtf8(""))
        self.btn_3.setObjectName(_fromUtf8("btn_3"))

        self.retranslateUi(messageDlg)
        QtCore.QMetaObject.connectSlotsByName(messageDlg)

    def retranslateUi(self, messageDlg):
        messageDlg.setWindowTitle(_translate("messageDlg", "Ack.. A Question...", None))
        self.btn_1.setText(_translate("messageDlg", "Yes", None))
        self.btn_2.setText(_translate("messageDlg", "No", None))

