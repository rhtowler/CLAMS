# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\ABLSpecialStudiesDlg.ui'
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

class Ui_ablspeciesstudiesDlg(object):
    def setupUi(self, ablspeciesstudiesDlg):
        ablspeciesstudiesDlg.setObjectName(_fromUtf8("ablspeciesstudiesDlg"))
        ablspeciesstudiesDlg.resize(759, 299)
        self.groupBox = QtGui.QGroupBox(ablspeciesstudiesDlg)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 721, 251))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.otolithBtn = QtGui.QPushButton(self.groupBox)
        self.otolithBtn.setGeometry(QtCore.QRect(10, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.otolithBtn.setFont(font)
        self.otolithBtn.setCheckable(True)
        self.otolithBtn.setObjectName(_fromUtf8("otolithBtn"))
        self.stomachBtn = QtGui.QPushButton(self.groupBox)
        self.stomachBtn.setGeometry(QtCore.QRect(10, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stomachBtn.setFont(font)
        self.stomachBtn.setCheckable(True)
        self.stomachBtn.setObjectName(_fromUtf8("stomachBtn"))
        self.isotopeMarshBtn = QtGui.QPushButton(self.groupBox)
        self.isotopeMarshBtn.setGeometry(QtCore.QRect(250, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeMarshBtn.setFont(font)
        self.isotopeMarshBtn.setCheckable(True)
        self.isotopeMarshBtn.setObjectName(_fromUtf8("isotopeMarshBtn"))
        self.geneticsBtn = QtGui.QPushButton(self.groupBox)
        self.geneticsBtn.setGeometry(QtCore.QRect(250, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.geneticsBtn.setFont(font)
        self.geneticsBtn.setCheckable(True)
        self.geneticsBtn.setObjectName(_fromUtf8("geneticsBtn"))
        self.doneBtn = QtGui.QPushButton(self.groupBox)
        self.doneBtn.setGeometry(QtCore.QRect(490, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.clearBtn = QtGui.QPushButton(self.groupBox)
        self.clearBtn.setGeometry(QtCore.QRect(250, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.energeticBtn = QtGui.QPushButton(self.groupBox)
        self.energeticBtn.setGeometry(QtCore.QRect(10, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.energeticBtn.setFont(font)
        self.energeticBtn.setCheckable(True)
        self.energeticBtn.setObjectName(_fromUtf8("energeticBtn"))
        self.tsmriBtn = QtGui.QPushButton(self.groupBox)
        self.tsmriBtn.setGeometry(QtCore.QRect(490, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tsmriBtn.setFont(font)
        self.tsmriBtn.setCheckable(True)
        self.tsmriBtn.setObjectName(_fromUtf8("tsmriBtn"))
        self.isotopeAndrewsBtn = QtGui.QPushButton(self.groupBox)
        self.isotopeAndrewsBtn.setGeometry(QtCore.QRect(490, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeAndrewsBtn.setFont(font)
        self.isotopeAndrewsBtn.setCheckable(True)
        self.isotopeAndrewsBtn.setObjectName(_fromUtf8("isotopeAndrewsBtn"))
        self.label_3 = QtGui.QLabel(ablspeciesstudiesDlg)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(ablspeciesstudiesDlg)
        QtCore.QMetaObject.connectSlotsByName(ablspeciesstudiesDlg)

    def retranslateUi(self, ablspeciesstudiesDlg):
        ablspeciesstudiesDlg.setWindowTitle(_translate("ablspeciesstudiesDlg", "Special Studies", None))
        self.otolithBtn.setText(_translate("ablspeciesstudiesDlg", "Otolith", None))
        self.stomachBtn.setText(_translate("ablspeciesstudiesDlg", "Stomach", None))
        self.isotopeMarshBtn.setText(_translate("ablspeciesstudiesDlg", "Isotope_Marsh", None))
        self.geneticsBtn.setText(_translate("ablspeciesstudiesDlg", "Genetics", None))
        self.doneBtn.setText(_translate("ablspeciesstudiesDlg", "Done", None))
        self.clearBtn.setText(_translate("ablspeciesstudiesDlg", "Clear", None))
        self.energeticBtn.setText(_translate("ablspeciesstudiesDlg", "Energetics", None))
        self.tsmriBtn.setText(_translate("ablspeciesstudiesDlg", "TSMRI", None))
        self.isotopeAndrewsBtn.setText(_translate("ablspeciesstudiesDlg", "Isotope_Andrews", None))
        self.label_3.setText(_translate("ablspeciesstudiesDlg", "Optional Special Studies", None))

