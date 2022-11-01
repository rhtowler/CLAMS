# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\BasketEditDlg.ui'
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

class Ui_basketeditDlg(object):
    def setupUi(self, basketeditDlg):
        basketeditDlg.setObjectName(_fromUtf8("basketeditDlg"))
        basketeditDlg.resize(533, 238)
        self.okBtn = QtGui.QPushButton(basketeditDlg)
        self.okBtn.setGeometry(QtCore.QRect(300, 170, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.cancelBtn = QtGui.QPushButton(basketeditDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(20, 170, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.label = QtGui.QLabel(basketeditDlg)
        self.label.setGeometry(QtCore.QRect(20, 15, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.editBasket = QtGui.QTableWidget(basketeditDlg)
        self.editBasket.setGeometry(QtCore.QRect(20, 40, 501, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editBasket.setFont(font)
        self.editBasket.setObjectName(_fromUtf8("editBasket"))
        self.editBasket.setColumnCount(0)
        self.editBasket.setRowCount(0)

        self.retranslateUi(basketeditDlg)
        QtCore.QMetaObject.connectSlotsByName(basketeditDlg)

    def retranslateUi(self, basketeditDlg):
        basketeditDlg.setWindowTitle(_translate("basketeditDlg", "Edit", None))
        self.okBtn.setText(_translate("basketeditDlg", "OK", None))
        self.cancelBtn.setText(_translate("basketeditDlg", "Cancel", None))
        self.label.setText(_translate("basketeditDlg", "Select field to edit ...", None))

