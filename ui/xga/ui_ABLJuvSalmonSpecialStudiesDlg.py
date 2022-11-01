# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\ABLJuvSalmonSpecialStudiesDlg.ui'
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

class Ui_abljuvsalmonspeciesstudiesDlg(object):
    def setupUi(self, abljuvsalmonspeciesstudiesDlg):
        abljuvsalmonspeciesstudiesDlg.setObjectName(_fromUtf8("abljuvsalmonspeciesstudiesDlg"))
        abljuvsalmonspeciesstudiesDlg.resize(759, 299)
        self.groupBox = QtGui.QGroupBox(abljuvsalmonspeciesstudiesDlg)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 721, 251))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.wfBtn = QtGui.QPushButton(self.groupBox)
        self.wfBtn.setGeometry(QtCore.QRect(10, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wfBtn.setFont(font)
        self.wfBtn.setCheckable(True)
        self.wfBtn.setObjectName(_fromUtf8("wfBtn"))
        self.stomachBtn = QtGui.QPushButton(self.groupBox)
        self.stomachBtn.setGeometry(QtCore.QRect(10, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stomachBtn.setFont(font)
        self.stomachBtn.setCheckable(True)
        self.stomachBtn.setObjectName(_fromUtf8("stomachBtn"))
        self.biaBtn = QtGui.QPushButton(self.groupBox)
        self.biaBtn.setGeometry(QtCore.QRect(490, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.biaBtn.setFont(font)
        self.biaBtn.setCheckable(True)
        self.biaBtn.setObjectName(_fromUtf8("biaBtn"))
        self.thiamineBtn = QtGui.QPushButton(self.groupBox)
        self.thiamineBtn.setGeometry(QtCore.QRect(10, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thiamineBtn.setFont(font)
        self.thiamineBtn.setCheckable(True)
        self.thiamineBtn.setObjectName(_fromUtf8("thiamineBtn"))
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
        self.igfBtn = QtGui.QPushButton(self.groupBox)
        self.igfBtn.setGeometry(QtCore.QRect(490, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.igfBtn.setFont(font)
        self.igfBtn.setCheckable(True)
        self.igfBtn.setObjectName(_fromUtf8("igfBtn"))
        self.isotopeBtn = QtGui.QPushButton(self.groupBox)
        self.isotopeBtn.setGeometry(QtCore.QRect(250, 100, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isotopeBtn.setFont(font)
        self.isotopeBtn.setCheckable(True)
        self.isotopeBtn.setObjectName(_fromUtf8("isotopeBtn"))
        self.fhBtn = QtGui.QPushButton(self.groupBox)
        self.fhBtn.setGeometry(QtCore.QRect(250, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fhBtn.setFont(font)
        self.fhBtn.setCheckable(True)
        self.fhBtn.setObjectName(_fromUtf8("fhBtn"))
        self.label_3 = QtGui.QLabel(abljuvsalmonspeciesstudiesDlg)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 197, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(abljuvsalmonspeciesstudiesDlg)
        QtCore.QMetaObject.connectSlotsByName(abljuvsalmonspeciesstudiesDlg)

    def retranslateUi(self, abljuvsalmonspeciesstudiesDlg):
        abljuvsalmonspeciesstudiesDlg.setWindowTitle(_translate("abljuvsalmonspeciesstudiesDlg", "Special Studies", None))
        self.wfBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Whole Fish", None))
        self.stomachBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Stomach", None))
        self.biaBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "BIA", None))
        self.thiamineBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Thiamine", None))
        self.doneBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Done", None))
        self.clearBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Clear", None))
        self.igfBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "IGF", None))
        self.isotopeBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Isotope", None))
        self.fhBtn.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Fish Head", None))
        self.label_3.setText(_translate("abljuvsalmonspeciesstudiesDlg", "Optional Special Studies", None))

