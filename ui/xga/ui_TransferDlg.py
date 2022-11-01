# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\TransferDlg.ui'
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

class Ui_transferDlg(object):
    def setupUi(self, transferDlg):
        transferDlg.setObjectName(_fromUtf8("transferDlg"))
        transferDlg.resize(922, 347)
        font = QtGui.QFont()
        font.setPointSize(14)
        transferDlg.setFont(font)
        self.fromSampleSpc = QtGui.QComboBox(transferDlg)
        self.fromSampleSpc.setGeometry(QtCore.QRect(30, 70, 321, 51))
        self.fromSampleSpc.setObjectName(_fromUtf8("fromSampleSpc"))
        self.toSampleSpc = QtGui.QComboBox(transferDlg)
        self.toSampleSpc.setGeometry(QtCore.QRect(30, 210, 321, 51))
        self.toSampleSpc.setObjectName(_fromUtf8("toSampleSpc"))
        self.getWtBtn = QtGui.QPushButton(transferDlg)
        self.getWtBtn.setEnabled(False)
        self.getWtBtn.setGeometry(QtCore.QRect(630, 70, 121, 51))
        self.getWtBtn.setObjectName(_fromUtf8("getWtBtn"))
        self.wtLabel = QtGui.QLabel(transferDlg)
        self.wtLabel.setEnabled(True)
        self.wtLabel.setGeometry(QtCore.QRect(780, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wtLabel.setFont(font)
        self.wtLabel.setFrameShape(QtGui.QFrame.Box)
        self.wtLabel.setText(_fromUtf8(""))
        self.wtLabel.setObjectName(_fromUtf8("wtLabel"))
        self.cancelBtn = QtGui.QPushButton(transferDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(640, 284, 121, 51))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.okBtn = QtGui.QPushButton(transferDlg)
        self.okBtn.setGeometry(QtCore.QRect(780, 284, 121, 51))
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.label = QtGui.QLabel(transferDlg)
        self.label.setGeometry(QtCore.QRect(30, 10, 191, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(transferDlg)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 151, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.fromBasketType = QtGui.QComboBox(transferDlg)
        self.fromBasketType.setEnabled(False)
        self.fromBasketType.setGeometry(QtCore.QRect(370, 70, 231, 51))
        self.fromBasketType.setObjectName(_fromUtf8("fromBasketType"))
        self.toBasketType = QtGui.QComboBox(transferDlg)
        self.toBasketType.setEnabled(False)
        self.toBasketType.setGeometry(QtCore.QRect(370, 210, 231, 51))
        self.toBasketType.setObjectName(_fromUtf8("toBasketType"))
        self.label_3 = QtGui.QLabel(transferDlg)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 151, 24))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(transferDlg)
        self.label_4.setGeometry(QtCore.QRect(370, 180, 151, 24))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(transferDlg)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 151, 24))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(transferDlg)
        self.label_6.setGeometry(QtCore.QRect(370, 40, 151, 24))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cntLabel = QtGui.QLabel(transferDlg)
        self.cntLabel.setEnabled(True)
        self.cntLabel.setGeometry(QtCore.QRect(780, 130, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cntLabel.setFont(font)
        self.cntLabel.setFrameShape(QtGui.QFrame.Box)
        self.cntLabel.setText(_fromUtf8(""))
        self.cntLabel.setObjectName(_fromUtf8("cntLabel"))
        self.getCntBtn = QtGui.QPushButton(transferDlg)
        self.getCntBtn.setEnabled(False)
        self.getCntBtn.setGeometry(QtCore.QRect(630, 130, 121, 51))
        self.getCntBtn.setObjectName(_fromUtf8("getCntBtn"))

        self.retranslateUi(transferDlg)
        QtCore.QMetaObject.connectSlotsByName(transferDlg)

    def retranslateUi(self, transferDlg):
        transferDlg.setWindowTitle(_translate("transferDlg", "Catch Transfer Dialog", None))
        self.getWtBtn.setText(_translate("transferDlg", "Weight", None))
        self.cancelBtn.setText(_translate("transferDlg", "Cancel", None))
        self.okBtn.setText(_translate("transferDlg", "OK", None))
        self.label.setText(_translate("transferDlg", "Take from Sample", None))
        self.label_2.setText(_translate("transferDlg", "Put into Sample", None))
        self.label_3.setText(_translate("transferDlg", "Species", None))
        self.label_4.setText(_translate("transferDlg", "Sample Type", None))
        self.label_5.setText(_translate("transferDlg", "Species", None))
        self.label_6.setText(_translate("transferDlg", "Sample Type", None))
        self.getCntBtn.setText(_translate("transferDlg", "Count", None))

