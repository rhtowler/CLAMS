# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\YesNoDlg.ui'
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

class Ui_YesNoDlg(object):
    def setupUi(self, YesNoDlg):
        YesNoDlg.setObjectName(_fromUtf8("YesNoDlg"))
        YesNoDlg.resize(354, 180)
        YesNoDlg.setMinimumSize(QtCore.QSize(354, 180))
        YesNoDlg.setMaximumSize(QtCore.QSize(354, 180))
        self.groupBox = QtGui.QGroupBox(YesNoDlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 33, 331, 141))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.yesBtn = QtGui.QPushButton(self.groupBox)
        self.yesBtn.setGeometry(QtCore.QRect(10, 15, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yesBtn.setFont(font)
        self.yesBtn.setObjectName(_fromUtf8("yesBtn"))
        self.noBtn = QtGui.QPushButton(self.groupBox)
        self.noBtn.setGeometry(QtCore.QRect(10, 75, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noBtn.setFont(font)
        self.noBtn.setObjectName(_fromUtf8("noBtn"))
        self.msgLabel = QtGui.QLabel(YesNoDlg)
        self.msgLabel.setGeometry(QtCore.QRect(10, 2, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.msgLabel.setFont(font)
        self.msgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))

        self.retranslateUi(YesNoDlg)
        QtCore.QMetaObject.connectSlotsByName(YesNoDlg)

    def retranslateUi(self, YesNoDlg):
        YesNoDlg.setWindowTitle(_translate("YesNoDlg", "Yes or No?", None))
        self.yesBtn.setText(_translate("YesNoDlg", "Yes", None))
        self.noBtn.setText(_translate("YesNoDlg", "No", None))
        self.msgLabel.setText(_translate("YesNoDlg", "Are you...", None))

