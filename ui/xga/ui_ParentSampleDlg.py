# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CLAMS_archive\CLAMS\ui\xga\ParentSampleDlg.ui'
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

class Ui_parentSampleDlg(object):
    def setupUi(self, parentSampleDlg):
        parentSampleDlg.setObjectName(_fromUtf8("parentSampleDlg"))
        parentSampleDlg.resize(273, 426)
        self.verticalLayout_2 = QtGui.QVBoxLayout(parentSampleDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(parentSampleDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.wholeHaulBtn = QtGui.QPushButton(self.groupBox)
        self.wholeHaulBtn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wholeHaulBtn.setFont(font)
        self.wholeHaulBtn.setCheckable(True)
        self.wholeHaulBtn.setAutoExclusive(True)
        self.wholeHaulBtn.setObjectName(_fromUtf8("wholeHaulBtn"))
        self.verticalLayout_3.addWidget(self.wholeHaulBtn)
        self.sortTableBtn = QtGui.QPushButton(self.groupBox)
        self.sortTableBtn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sortTableBtn.setFont(font)
        self.sortTableBtn.setCheckable(True)
        self.sortTableBtn.setAutoExclusive(True)
        self.sortTableBtn.setObjectName(_fromUtf8("sortTableBtn"))
        self.verticalLayout_3.addWidget(self.sortTableBtn)
        self.mix1Btn = QtGui.QPushButton(self.groupBox)
        self.mix1Btn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mix1Btn.setFont(font)
        self.mix1Btn.setCheckable(True)
        self.mix1Btn.setAutoExclusive(True)
        self.mix1Btn.setObjectName(_fromUtf8("mix1Btn"))
        self.verticalLayout_3.addWidget(self.mix1Btn)
        self.subMix1Btn = QtGui.QPushButton(self.groupBox)
        self.subMix1Btn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.subMix1Btn.setFont(font)
        self.subMix1Btn.setCheckable(True)
        self.subMix1Btn.setAutoExclusive(True)
        self.subMix1Btn.setObjectName(_fromUtf8("subMix1Btn"))
        self.verticalLayout_3.addWidget(self.subMix1Btn)
        self.mix2Btn = QtGui.QPushButton(self.groupBox)
        self.mix2Btn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mix2Btn.setFont(font)
        self.mix2Btn.setCheckable(True)
        self.mix2Btn.setAutoExclusive(True)
        self.mix2Btn.setObjectName(_fromUtf8("mix2Btn"))
        self.verticalLayout_3.addWidget(self.mix2Btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.okBtn = QtGui.QPushButton(parentSampleDlg)
        self.okBtn.setMinimumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout.addWidget(self.okBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelBtn = QtGui.QPushButton(parentSampleDlg)
        self.cancelBtn.setMinimumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(parentSampleDlg)
        QtCore.QMetaObject.connectSlotsByName(parentSampleDlg)

    def retranslateUi(self, parentSampleDlg):
        parentSampleDlg.setWindowTitle(_translate("parentSampleDlg", "Parent Sample Dialog", None))
        self.groupBox.setTitle(_translate("parentSampleDlg", "Sample Parent", None))
        self.wholeHaulBtn.setText(_translate("parentSampleDlg", "Whole Haul", None))
        self.sortTableBtn.setText(_translate("parentSampleDlg", "Sorting Table", None))
        self.mix1Btn.setText(_translate("parentSampleDlg", "Mix1", None))
        self.subMix1Btn.setText(_translate("parentSampleDlg", "SubMix 1", None))
        self.mix2Btn.setText(_translate("parentSampleDlg", "Mix 2", None))
        self.okBtn.setText(_translate("parentSampleDlg", "OK", None))
        self.cancelBtn.setText(_translate("parentSampleDlg", "Cancel", None))

