# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\InteractionCheckDlg.ui'
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

class Ui_interactionCheckDlg(object):
    def setupUi(self, interactionCheckDlg):
        interactionCheckDlg.setObjectName(_fromUtf8("interactionCheckDlg"))
        interactionCheckDlg.resize(584, 397)
        self.label = QtGui.QLabel(interactionCheckDlg)
        self.label.setGeometry(QtCore.QRect(180, 20, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(interactionCheckDlg)
        self.label_2.setGeometry(QtCore.QRect(180, 178, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pic1 = QtGui.QLabel(interactionCheckDlg)
        self.pic1.setGeometry(QtCore.QRect(30, 20, 121, 121))
        self.pic1.setText(_fromUtf8(""))
        self.pic1.setObjectName(_fromUtf8("pic1"))
        self.pic2 = QtGui.QLabel(interactionCheckDlg)
        self.pic2.setGeometry(QtCore.QRect(30, 180, 121, 121))
        self.pic2.setText(_fromUtf8(""))
        self.pic2.setObjectName(_fromUtf8("pic2"))
        self.groupBox = QtGui.QGroupBox(interactionCheckDlg)
        self.groupBox.setGeometry(QtCore.QRect(180, 90, 361, 61))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.noBtn1 = QtGui.QPushButton(self.groupBox)
        self.noBtn1.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noBtn1.setFont(font)
        self.noBtn1.setCheckable(True)
        self.noBtn1.setAutoExclusive(True)
        self.noBtn1.setObjectName(_fromUtf8("noBtn1"))
        self.yesBtn1 = QtGui.QPushButton(self.groupBox)
        self.yesBtn1.setGeometry(QtCore.QRect(220, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yesBtn1.setFont(font)
        self.yesBtn1.setCheckable(True)
        self.yesBtn1.setAutoExclusive(True)
        self.yesBtn1.setObjectName(_fromUtf8("yesBtn1"))
        self.abortBtn = QtGui.QPushButton(interactionCheckDlg)
        self.abortBtn.setGeometry(QtCore.QRect(40, 340, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.abortBtn.setFont(font)
        self.abortBtn.setObjectName(_fromUtf8("abortBtn"))
        self.proceedBtn = QtGui.QPushButton(interactionCheckDlg)
        self.proceedBtn.setGeometry(QtCore.QRect(360, 340, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.proceedBtn.setFont(font)
        self.proceedBtn.setObjectName(_fromUtf8("proceedBtn"))
        self.groupBox_2 = QtGui.QGroupBox(interactionCheckDlg)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 250, 361, 61))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.noBtn2 = QtGui.QPushButton(self.groupBox_2)
        self.noBtn2.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noBtn2.setFont(font)
        self.noBtn2.setCheckable(True)
        self.noBtn2.setAutoExclusive(True)
        self.noBtn2.setObjectName(_fromUtf8("noBtn2"))
        self.yesBtn2 = QtGui.QPushButton(self.groupBox_2)
        self.yesBtn2.setGeometry(QtCore.QRect(220, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yesBtn2.setFont(font)
        self.yesBtn2.setCheckable(True)
        self.yesBtn2.setAutoExclusive(True)
        self.yesBtn2.setObjectName(_fromUtf8("yesBtn2"))

        self.retranslateUi(interactionCheckDlg)
        QtCore.QMetaObject.connectSlotsByName(interactionCheckDlg)

    def retranslateUi(self, interactionCheckDlg):
        interactionCheckDlg.setWindowTitle(_translate("interactionCheckDlg", "Mammal and Bird Interaction Check", None))
        self.label.setText(_translate("interactionCheckDlg", "Are there any marine mammals present in the vicinity of the boat?", None))
        self.label_2.setText(_translate("interactionCheckDlg", "Are there any endangered seabirds present in the vicinity of the boat?", None))
        self.noBtn1.setText(_translate("interactionCheckDlg", "No", None))
        self.yesBtn1.setText(_translate("interactionCheckDlg", "Yes", None))
        self.abortBtn.setText(_translate("interactionCheckDlg", "Abort", None))
        self.proceedBtn.setText(_translate("interactionCheckDlg", "Proceed", None))
        self.noBtn2.setText(_translate("interactionCheckDlg", "No", None))
        self.yesBtn2.setText(_translate("interactionCheckDlg", "Yes", None))

