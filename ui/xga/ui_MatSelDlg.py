# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\MatSelDlg.ui'
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

class Ui_matselDlg(object):
    def setupUi(self, matselDlg):
        matselDlg.setObjectName(_fromUtf8("matselDlg"))
        matselDlg.resize(388, 380)
        self.groupBox = QtGui.QGroupBox(matselDlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 371, 251))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mat1Btn = QtGui.QPushButton(self.groupBox)
        self.mat1Btn.setGeometry(QtCore.QRect(10, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat1Btn.setFont(font)
        self.mat1Btn.setCheckable(False)
        self.mat1Btn.setObjectName(_fromUtf8("mat1Btn"))
        self.mat5Btn = QtGui.QPushButton(self.groupBox)
        self.mat5Btn.setGeometry(QtCore.QRect(190, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat5Btn.setFont(font)
        self.mat5Btn.setCheckable(False)
        self.mat5Btn.setObjectName(_fromUtf8("mat5Btn"))
        self.mat2Btn = QtGui.QPushButton(self.groupBox)
        self.mat2Btn.setGeometry(QtCore.QRect(10, 70, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat2Btn.setFont(font)
        self.mat2Btn.setCheckable(False)
        self.mat2Btn.setObjectName(_fromUtf8("mat2Btn"))
        self.mat6Btn = QtGui.QPushButton(self.groupBox)
        self.mat6Btn.setGeometry(QtCore.QRect(190, 70, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat6Btn.setFont(font)
        self.mat6Btn.setCheckable(False)
        self.mat6Btn.setObjectName(_fromUtf8("mat6Btn"))
        self.mat3Btn = QtGui.QPushButton(self.groupBox)
        self.mat3Btn.setGeometry(QtCore.QRect(10, 130, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat3Btn.setFont(font)
        self.mat3Btn.setCheckable(False)
        self.mat3Btn.setObjectName(_fromUtf8("mat3Btn"))
        self.mat7Btn = QtGui.QPushButton(self.groupBox)
        self.mat7Btn.setGeometry(QtCore.QRect(190, 130, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat7Btn.setFont(font)
        self.mat7Btn.setCheckable(False)
        self.mat7Btn.setObjectName(_fromUtf8("mat7Btn"))
        self.mat4Btn = QtGui.QPushButton(self.groupBox)
        self.mat4Btn.setGeometry(QtCore.QRect(10, 190, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat4Btn.setFont(font)
        self.mat4Btn.setCheckable(False)
        self.mat4Btn.setObjectName(_fromUtf8("mat4Btn"))
        self.mat8Btn = QtGui.QPushButton(self.groupBox)
        self.mat8Btn.setGeometry(QtCore.QRect(190, 190, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mat8Btn.setFont(font)
        self.mat8Btn.setCheckable(False)
        self.mat8Btn.setObjectName(_fromUtf8("mat8Btn"))
        self.groupBox_2 = QtGui.QGroupBox(matselDlg)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 371, 80))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.guideBtn = QtGui.QPushButton(self.groupBox_2)
        self.guideBtn.setGeometry(QtCore.QRect(10, 10, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.guideBtn.setFont(font)
        self.guideBtn.setObjectName(_fromUtf8("guideBtn"))
        self.label = QtGui.QLabel(matselDlg)
        self.label.setGeometry(QtCore.QRect(10, 10, 139, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(matselDlg)
        QtCore.QMetaObject.connectSlotsByName(matselDlg)

    def retranslateUi(self, matselDlg):
        matselDlg.setWindowTitle(_translate("matselDlg", "Maturity Selection", None))
        self.mat1Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat5Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat2Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat6Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat3Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat7Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat4Btn.setText(_translate("matselDlg", "PushButton", None))
        self.mat8Btn.setText(_translate("matselDlg", "PushButton", None))
        self.guideBtn.setText(_translate("matselDlg", "View Maturity Guide", None))
        self.label.setText(_translate("matselDlg", "Select Maturity...", None))

