# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\MACE Apps\CLAMS-Python-x64\CLAMS\ui\xga\CollectionsDialog.ui'
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

class Ui_collectionsDlg(object):
    def setupUi(self, collectionsDlg):
        collectionsDlg.setObjectName(_fromUtf8("collectionsDlg"))
        collectionsDlg.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(collectionsDlg)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_1 = QtGui.QCheckBox(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.printExitButton = QtGui.QPushButton(collectionsDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printExitButton.setFont(font)
        self.printExitButton.setObjectName(_fromUtf8("printExitButton"))
        self.gridLayout.addWidget(self.printExitButton, 3, 0, 1, 1)
        self.cancelBtn = QtGui.QPushButton(collectionsDlg)
        self.cancelBtn.setMinimumSize(QtCore.QSize(0, 54))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(collectionsDlg)
        QtCore.QMetaObject.connectSlotsByName(collectionsDlg)

    def retranslateUi(self, collectionsDlg):
        collectionsDlg.setWindowTitle(_translate("collectionsDlg", "Collections Dialog", None))
        self.checkBox_1.setText(_translate("collectionsDlg", "CheckBox", None))
        self.checkBox_6.setText(_translate("collectionsDlg", "CheckBox", None))
        self.checkBox_5.setText(_translate("collectionsDlg", "CheckBox", None))
        self.checkBox_3.setText(_translate("collectionsDlg", "CheckBox", None))
        self.checkBox_2.setText(_translate("collectionsDlg", "CheckBox", None))
        self.checkBox_4.setText(_translate("collectionsDlg", "CheckBox", None))
        self.printExitButton.setText(_translate("collectionsDlg", "Print Label \n"
"and Exit", None))
        self.cancelBtn.setText(_translate("collectionsDlg", "Cancel", None))

