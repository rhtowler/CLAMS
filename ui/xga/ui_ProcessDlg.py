# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\ProcessDlg.ui'
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

class Ui_processDlg(object):
    def setupUi(self, processDlg):
        processDlg.setObjectName(_fromUtf8("processDlg"))
        processDlg.resize(562, 185)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(processDlg.sizePolicy().hasHeightForWidth())
        processDlg.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(processDlg)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.haulLabel = QtGui.QLabel(processDlg)
        self.haulLabel.setGeometry(QtCore.QRect(280, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.haulLabel.setFont(font)
        self.haulLabel.setText(_fromUtf8(""))
        self.haulLabel.setObjectName(_fromUtf8("haulLabel"))
        self.cancelBtn = QtGui.QPushButton(processDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(10, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.editBtn = QtGui.QPushButton(processDlg)
        self.editBtn.setGeometry(QtCore.QRect(200, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName(_fromUtf8("editBtn"))
        self.procBtn = QtGui.QPushButton(processDlg)
        self.procBtn.setGeometry(QtCore.QRect(390, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.procBtn.setFont(font)
        self.procBtn.setObjectName(_fromUtf8("procBtn"))
        self.label_2 = QtGui.QLabel(processDlg)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.timeLabel = QtGui.QLabel(processDlg)
        self.timeLabel.setGeometry(QtCore.QRect(200, 70, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.timeLabel.setFont(font)
        self.timeLabel.setText(_fromUtf8(""))
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))

        self.retranslateUi(processDlg)
        QtCore.QMetaObject.connectSlotsByName(processDlg)

    def retranslateUi(self, processDlg):
        processDlg.setWindowTitle(_translate("processDlg", "Process Haul", None))
        self.label.setText(_translate("processDlg", "Current Haul is", None))
        self.cancelBtn.setText(_translate("processDlg", "Cancel", None))
        self.editBtn.setText(_translate("processDlg", "Edit past haul", None))
        self.procBtn.setText(_translate("processDlg", "Proceed", None))
        self.label_2.setText(_translate("processDlg", "Hauled back at", None))

