# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\MatSelDlgABL.ui'
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

class Ui_matselDlgABL(object):
    def setupUi(self, matselDlgABL):
        matselDlgABL.setObjectName(_fromUtf8("matselDlgABL"))
        matselDlgABL.resize(264, 171)
        self.groupBox = QtGui.QGroupBox(matselDlgABL)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 241, 131))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.immatureBtn = QtGui.QPushButton(self.groupBox)
        self.immatureBtn.setGeometry(QtCore.QRect(10, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.immatureBtn.setFont(font)
        self.immatureBtn.setObjectName(_fromUtf8("immatureBtn"))
        self.maturingBtn = QtGui.QPushButton(self.groupBox)
        self.maturingBtn.setGeometry(QtCore.QRect(10, 70, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maturingBtn.setFont(font)
        self.maturingBtn.setObjectName(_fromUtf8("maturingBtn"))
        self.label = QtGui.QLabel(matselDlgABL)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(matselDlgABL)
        QtCore.QMetaObject.connectSlotsByName(matselDlgABL)

    def retranslateUi(self, matselDlgABL):
        matselDlgABL.setWindowTitle(_translate("matselDlgABL", "Maturity Selection", None))
        self.immatureBtn.setText(_translate("matselDlgABL", "Immature", None))
        self.maturingBtn.setText(_translate("matselDlgABL", "Maturing", None))
        self.label.setText(_translate("matselDlgABL", "Select the maturity...", None))

