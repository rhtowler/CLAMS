# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\AFSCGit\CLAMS\MACE\application\SBE Downloader\ui\sbeSetInterval.ui'
#
# Created: Wed Jan 27 13:06:21 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_sbeSetInterval(object):
    def setupUi(self, sbeSetInterval):
        sbeSetInterval.setObjectName(_fromUtf8("sbeSetInterval"))
        sbeSetInterval.resize(339, 101)
        sbeSetInterval.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(sbeSetInterval)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(sbeSetInterval)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(sbeSetInterval)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cbRTO = QtGui.QCheckBox(sbeSetInterval)
        self.cbRTO.setText(_fromUtf8(""))
        self.cbRTO.setObjectName(_fromUtf8("cbRTO"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbRTO)
        self.spinInterval = QtGui.QSpinBox(sbeSetInterval)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinInterval.setFont(font)
        self.spinInterval.setMinimum(0)
        self.spinInterval.setMaximum(32766)
        self.spinInterval.setProperty("value", 0)
        self.spinInterval.setObjectName(_fromUtf8("spinInterval"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinInterval)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(478, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbCancel = QtGui.QPushButton(sbeSetInterval)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(sbeSetInterval)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout.addWidget(self.pbOK)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(sbeSetInterval)
        QtCore.QMetaObject.connectSlotsByName(sbeSetInterval)

    def retranslateUi(self, sbeSetInterval):
        sbeSetInterval.setWindowTitle(_translate("sbeSetInterval", "Set Sampling Interval", None))
        self.label.setText(_translate("sbeSetInterval", "SBE Sampling Interval", None))
        self.label_2.setText(_translate("sbeSetInterval", "Display Real-Time Output", None))
        self.spinInterval.setToolTip(_translate("sbeSetInterval", "Interval (in seconds) between samples.", None))
        self.spinInterval.setSuffix(_translate("sbeSetInterval", " seconds", None))
        self.pbCancel.setText(_translate("sbeSetInterval", "Cancel", None))
        self.pbOK.setText(_translate("sbeSetInterval", "OK", None))

