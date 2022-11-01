# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q:\ui\xga\CodendStatusDlg.ui'
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

class Ui_codendStatusDlg(object):
    def setupUi(self, codendStatusDlg):
        codendStatusDlg.setObjectName(_fromUtf8("codendStatusDlg"))
        codendStatusDlg.resize(376, 551)
        self.verticalLayout = QtGui.QVBoxLayout(codendStatusDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(codendStatusDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btn_5 = QtGui.QPushButton(self.groupBox)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_5.setFont(font)
        self.btn_5.setCheckable(True)
        self.btn_5.setAutoExclusive(True)
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.verticalLayout_2.addWidget(self.btn_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_1 = QtGui.QPushButton(self.groupBox)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_1.setFont(font)
        self.btn_1.setCheckable(True)
        self.btn_1.setAutoExclusive(True)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.verticalLayout_2.addWidget(self.btn_1)
        self.btn_2 = QtGui.QPushButton(self.groupBox)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_2.setFont(font)
        self.btn_2.setCheckable(True)
        self.btn_2.setAutoExclusive(True)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.verticalLayout_2.addWidget(self.btn_2)
        self.btn_3 = QtGui.QPushButton(self.groupBox)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_3.setFont(font)
        self.btn_3.setCheckable(True)
        self.btn_3.setAutoExclusive(True)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.verticalLayout_2.addWidget(self.btn_3)
        self.btn_4 = QtGui.QPushButton(self.groupBox)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_4.setFont(font)
        self.btn_4.setCheckable(True)
        self.btn_4.setAutoExclusive(True)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.verticalLayout_2.addWidget(self.btn_4)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(codendStatusDlg)
        QtCore.QMetaObject.connectSlotsByName(codendStatusDlg)

    def retranslateUi(self, codendStatusDlg):
        codendStatusDlg.setWindowTitle(_translate("codendStatusDlg", "Codend Status", None))
        self.groupBox.setTitle(_translate("codendStatusDlg", "Select Codend Status...", None))
        self.btn_5.setText(_translate("codendStatusDlg", "Codend Status OK", None))
        self.btn_1.setText(_translate("codendStatusDlg", "Codend Open INTENTIONALLY", None))
        self.btn_2.setText(_translate("codendStatusDlg", "Codend Open MALFUNCTION", None))
        self.btn_3.setText(_translate("codendStatusDlg", "Codend Closed NO CATCH", None))
        self.btn_4.setText(_translate("codendStatusDlg", "Codend Closed UNPROCESSED", None))

