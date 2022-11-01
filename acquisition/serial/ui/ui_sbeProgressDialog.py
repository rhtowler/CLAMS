# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rtowler\AFSCsvn\CLAMS\trunk\application\acquisition\serial\ui\sbeProgressDialog.ui'
#
# Created: Mon Dec 05 13:47:02 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_sbeProgressDialog(object):
    def setupUi(self, sbeProgressDialog):
        sbeProgressDialog.setObjectName(_fromUtf8("sbeProgressDialog"))
        sbeProgressDialog.setWindowModality(QtCore.Qt.WindowModal)
        sbeProgressDialog.resize(400, 84)
        sbeProgressDialog.setWindowTitle(QtGui.QApplication.translate("sbeProgressDialog", "SBE Download Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(sbeProgressDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(sbeProgressDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.abortButton = QtGui.QPushButton(sbeProgressDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.abortButton.setFont(font)
        self.abortButton.setText(QtGui.QApplication.translate("sbeProgressDialog", "Abort Download", None, QtGui.QApplication.UnicodeUTF8))
        self.abortButton.setObjectName(_fromUtf8("abortButton"))
        self.horizontalLayout.addWidget(self.abortButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(sbeProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(sbeProgressDialog)

    def retranslateUi(self, sbeProgressDialog):
        pass

