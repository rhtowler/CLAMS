# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\SpecimenDelDlg.ui'
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

class Ui_specimendelDlg(object):
    def setupUi(self, specimendelDlg):
        specimendelDlg.setObjectName(_fromUtf8("specimendelDlg"))
        specimendelDlg.resize(765, 227)
        self.okBtn = QtGui.QPushButton(specimendelDlg)
        self.okBtn.setGeometry(QtCore.QRect(520, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.cancelBtn = QtGui.QPushButton(specimendelDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(270, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.label = QtGui.QLabel(specimendelDlg)
        self.label.setGeometry(QtCore.QRect(20, 9, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.delSpecimen = QtGui.QTableWidget(specimendelDlg)
        self.delSpecimen.setGeometry(QtCore.QRect(20, 40, 721, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.delSpecimen.setFont(font)
        self.delSpecimen.setSelectionBehavior(QtGui.QAbstractItemView.SelectColumns)
        self.delSpecimen.setObjectName(_fromUtf8("delSpecimen"))
        self.delSpecimen.setColumnCount(0)
        self.delSpecimen.setRowCount(0)
        self.delBtn = QtGui.QPushButton(specimendelDlg)
        self.delBtn.setGeometry(QtCore.QRect(20, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName(_fromUtf8("delBtn"))

        self.retranslateUi(specimendelDlg)
        QtCore.QMetaObject.connectSlotsByName(specimendelDlg)

    def retranslateUi(self, specimendelDlg):
        specimendelDlg.setWindowTitle(_translate("specimendelDlg", "Delete Specimen", None))
        self.okBtn.setText(_translate("specimendelDlg", "Done", None))
        self.cancelBtn.setText(_translate("specimendelDlg", "Cancel", None))
        self.label.setText(_translate("specimendelDlg", "Select measurement to delete", None))
        self.delBtn.setText(_translate("specimendelDlg", "Delete", None))

