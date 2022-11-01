# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V:\AFSCGit\CLAMS\application\ui\sbeSetLocation.ui'
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

class Ui_sbeSetLocation(object):
    def setupUi(self, sbeSetLocation):
        sbeSetLocation.setObjectName(_fromUtf8("sbeSetLocation"))
        sbeSetLocation.resize(494, 133)
        sbeSetLocation.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(sbeSetLocation)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.text = QtGui.QLabel(sbeSetLocation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName(_fromUtf8("text"))
        self.verticalLayout.addWidget(self.text)
        self.cbLocation = QtGui.QComboBox(sbeSetLocation)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbLocation.setFont(font)
        self.cbLocation.setObjectName(_fromUtf8("cbLocation"))
        self.verticalLayout.addWidget(self.cbLocation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(478, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbCancel = QtGui.QPushButton(sbeSetLocation)
        self.pbCancel.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbCancel.setFont(font)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(sbeSetLocation)
        self.pbOK.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbOK.setFont(font)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout.addWidget(self.pbOK)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(sbeSetLocation)
        QtCore.QMetaObject.connectSlotsByName(sbeSetLocation)

    def retranslateUi(self, sbeSetLocation):
        sbeSetLocation.setWindowTitle(_translate("sbeSetLocation", "Set SBE Mounting Location", None))
        self.text.setText(_translate("sbeSetLocation", "Please specify the SBE Mounting Location ", None))
        self.pbCancel.setText(_translate("sbeSetLocation", "Cancel", None))
        self.pbOK.setText(_translate("sbeSetLocation", "OK", None))

