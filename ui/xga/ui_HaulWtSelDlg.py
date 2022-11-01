# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\HaulWtSelDlg.ui'
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

class Ui_haulwtselDlg(object):
    def setupUi(self, haulwtselDlg):
        haulwtselDlg.setObjectName(_fromUtf8("haulwtselDlg"))
        haulwtselDlg.resize(322, 350)
        haulwtselDlg.setMinimumSize(QtCore.QSize(320, 350))
        self.verticalLayout = QtGui.QVBoxLayout(haulwtselDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(haulwtselDlg)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.btn_0 = QtGui.QPushButton(haulwtselDlg)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.verticalLayout.addWidget(self.btn_0)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_1 = QtGui.QPushButton(haulwtselDlg)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.verticalLayout.addWidget(self.btn_1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_2 = QtGui.QPushButton(haulwtselDlg)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.verticalLayout.addWidget(self.btn_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_3 = QtGui.QPushButton(haulwtselDlg)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.verticalLayout.addWidget(self.btn_3)

        self.retranslateUi(haulwtselDlg)
        QtCore.QMetaObject.connectSlotsByName(haulwtselDlg)

    def retranslateUi(self, haulwtselDlg):
        haulwtselDlg.setWindowTitle(_translate("haulwtselDlg", "Haul Weight Method", None))
        self.label.setText(_translate("haulwtselDlg", "Haul Weight Estimation", None))
        self.btn_0.setText(_translate("haulwtselDlg", "PushButton", None))
        self.btn_1.setText(_translate("haulwtselDlg", "PushButton", None))
        self.btn_2.setText(_translate("haulwtselDlg", "PushButton", None))
        self.btn_3.setText(_translate("haulwtselDlg", "PushButton", None))

