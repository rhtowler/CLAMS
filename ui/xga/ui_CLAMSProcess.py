# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CLAMS-Python-x64\CLAMS\ui\xga\CLAMSProcess.ui'
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

class Ui_clamsProcess(object):
    def setupUi(self, clamsProcess):
        clamsProcess.setObjectName(_fromUtf8("clamsProcess"))
        clamsProcess.resize(1020, 760)
        self.haulBtn = QtGui.QPushButton(clamsProcess)
        self.haulBtn.setEnabled(False)
        self.haulBtn.setGeometry(QtCore.QRect(120, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.haulBtn.setFont(font)
        self.haulBtn.setAutoFillBackground(True)
        self.haulBtn.setCheckable(False)
        self.haulBtn.setObjectName(_fromUtf8("haulBtn"))
        self.haulLabel = QtGui.QLabel(clamsProcess)
        self.haulLabel.setGeometry(QtCore.QRect(20, 30, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.haulLabel.setFont(font)
        self.haulLabel.setAutoFillBackground(True)
        self.haulLabel.setFrameShape(QtGui.QFrame.Panel)
        self.haulLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.haulLabel.setLineWidth(1)
        self.haulLabel.setText(_fromUtf8(""))
        self.haulLabel.setObjectName(_fromUtf8("haulLabel"))
        self.label = QtGui.QLabel(clamsProcess)
        self.label.setGeometry(QtCore.QRect(8, 0, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.doneBtn = QtGui.QPushButton(clamsProcess)
        self.doneBtn.setGeometry(QtCore.QRect(650, 680, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.doneBtn.setFont(font)
        self.doneBtn.setAutoFillBackground(True)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.catchBtn = QtGui.QPushButton(clamsProcess)
        self.catchBtn.setEnabled(False)
        self.catchBtn.setGeometry(QtCore.QRect(567, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.catchBtn.setFont(font)
        self.catchBtn.setAutoFillBackground(True)
        self.catchBtn.setCheckable(False)
        self.catchBtn.setObjectName(_fromUtf8("catchBtn"))
        self.lengthBtn = QtGui.QPushButton(clamsProcess)
        self.lengthBtn.setEnabled(False)
        self.lengthBtn.setGeometry(QtCore.QRect(707, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lengthBtn.setFont(font)
        self.lengthBtn.setAutoFillBackground(True)
        self.lengthBtn.setCheckable(False)
        self.lengthBtn.setObjectName(_fromUtf8("lengthBtn"))
        self.specBtn = QtGui.QPushButton(clamsProcess)
        self.specBtn.setEnabled(False)
        self.specBtn.setGeometry(QtCore.QRect(847, 30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.specBtn.setFont(font)
        self.specBtn.setAutoFillBackground(True)
        self.specBtn.setCheckable(False)
        self.specBtn.setObjectName(_fromUtf8("specBtn"))
        self.line = QtGui.QFrame(clamsProcess)
        self.line.setGeometry(QtCore.QRect(10, 80, 1001, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.picLabel = QtGui.QLabel(clamsProcess)
        self.picLabel.setGeometry(QtCore.QRect(10, 100, 981, 561))
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.partitionBox = QtGui.QComboBox(clamsProcess)
        self.partitionBox.setGeometry(QtCore.QRect(268, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.partitionBox.setFont(font)
        self.partitionBox.setObjectName(_fromUtf8("partitionBox"))
        self.label_2 = QtGui.QLabel(clamsProcess)
        self.label_2.setGeometry(QtCore.QRect(265, 0, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.fixSpeciesBtn = QtGui.QPushButton(clamsProcess)
        self.fixSpeciesBtn.setGeometry(QtCore.QRect(20, 620, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fixSpeciesBtn.setFont(font)
        self.fixSpeciesBtn.setAutoFillBackground(True)
        self.fixSpeciesBtn.setObjectName(_fromUtf8("fixSpeciesBtn"))
        self.editCodendStateBtn = QtGui.QPushButton(clamsProcess)
        self.editCodendStateBtn.setGeometry(QtCore.QRect(20, 680, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editCodendStateBtn.setFont(font)
        self.editCodendStateBtn.setObjectName(_fromUtf8("editCodendStateBtn"))

        self.retranslateUi(clamsProcess)
        QtCore.QMetaObject.connectSlotsByName(clamsProcess)

    def retranslateUi(self, clamsProcess):
        clamsProcess.setWindowTitle(_translate("clamsProcess", "CLAMS Haul Processing", None))
        self.haulBtn.setText(_translate("clamsProcess", "Haul Form", None))
        self.label.setText(_translate("clamsProcess", "Haul Number", None))
        self.doneBtn.setText(_translate("clamsProcess", "Finished processing haul", None))
        self.catchBtn.setText(_translate("clamsProcess", "Catch Form", None))
        self.lengthBtn.setText(_translate("clamsProcess", "Length Form", None))
        self.specBtn.setText(_translate("clamsProcess", "Specimen Form", None))
        self.label_2.setText(_translate("clamsProcess", "Partiton", None))
        self.fixSpeciesBtn.setText(_translate("clamsProcess", "Fix Species/Sex Assignment", None))
        self.editCodendStateBtn.setText(_translate("clamsProcess", "Edit Codend State", None))

