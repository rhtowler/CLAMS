# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\ABLImMatSalmonSpecialStudiesDlg.ui'
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

class Ui_ablimmatsalmonspeciesstudiesDlg(object):
    def setupUi(self, ablimmatsalmonspeciesstudiesDlg):
        ablimmatsalmonspeciesstudiesDlg.setObjectName(_fromUtf8("ablimmatsalmonspeciesstudiesDlg"))
        ablimmatsalmonspeciesstudiesDlg.resize(759, 217)
        self.groupBox = QtGui.QGroupBox(ablimmatsalmonspeciesstudiesDlg)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 721, 171))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.stomachBtn = QtGui.QPushButton(self.groupBox)
        self.stomachBtn.setGeometry(QtCore.QRect(10, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stomachBtn.setFont(font)
        self.stomachBtn.setCheckable(True)
        self.stomachBtn.setObjectName(_fromUtf8("stomachBtn"))
        self.thiamineBtn = QtGui.QPushButton(self.groupBox)
        self.thiamineBtn.setGeometry(QtCore.QRect(490, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thiamineBtn.setFont(font)
        self.thiamineBtn.setCheckable(True)
        self.thiamineBtn.setObjectName(_fromUtf8("thiamineBtn"))
        self.doneBtn = QtGui.QPushButton(self.groupBox)
        self.doneBtn.setGeometry(QtCore.QRect(490, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.clearBtn = QtGui.QPushButton(self.groupBox)
        self.clearBtn.setGeometry(QtCore.QRect(250, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.isotopeBtn = QtGui.QPushButton(self.groupBox)
        self.isotopeBtn.setGeometry(QtCore.QRect(250, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeBtn.setFont(font)
        self.isotopeBtn.setCheckable(True)
        self.isotopeBtn.setObjectName(_fromUtf8("isotopeBtn"))
        self.otolithBtn = QtGui.QPushButton(self.groupBox)
        self.otolithBtn.setGeometry(QtCore.QRect(10, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.otolithBtn.setFont(font)
        self.otolithBtn.setCheckable(True)
        self.otolithBtn.setObjectName(_fromUtf8("otolithBtn"))
        self.label_3 = QtGui.QLabel(ablimmatsalmonspeciesstudiesDlg)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 197, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(ablimmatsalmonspeciesstudiesDlg)
        QtCore.QMetaObject.connectSlotsByName(ablimmatsalmonspeciesstudiesDlg)

    def retranslateUi(self, ablimmatsalmonspeciesstudiesDlg):
        ablimmatsalmonspeciesstudiesDlg.setWindowTitle(_translate("ablimmatsalmonspeciesstudiesDlg", "Special Studies", None))
        self.stomachBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Stomach", None))
        self.thiamineBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Thiamine", None))
        self.doneBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Done", None))
        self.clearBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Clear", None))
        self.isotopeBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Isotope", None))
        self.otolithBtn.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Otolith", None))
        self.label_3.setText(_translate("ablimmatsalmonspeciesstudiesDlg", "Optional Special Studies", None))

