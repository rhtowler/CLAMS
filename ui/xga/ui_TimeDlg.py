# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\TimeDlg.ui'
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

class Ui_timeDlg(object):
    def setupUi(self, timeDlg):
        timeDlg.setObjectName(_fromUtf8("timeDlg"))
        timeDlg.resize(383, 216)
        self.timeEdit = QtGui.QTimeEdit(timeDlg)
        self.timeEdit.setGeometry(QtCore.QRect(20, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.dateEdit = QtGui.QDateEdit(timeDlg)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.okBtn = QtGui.QPushButton(timeDlg)
        self.okBtn.setGeometry(QtCore.QRect(220, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.cancelBtn = QtGui.QPushButton(timeDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(30, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.label = QtGui.QLabel(timeDlg)
        self.label.setGeometry(QtCore.QRect(30, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pbGetCurrentTime = QtGui.QPushButton(timeDlg)
        self.pbGetCurrentTime.setGeometry(QtCore.QRect(200, 70, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbGetCurrentTime.setFont(font)
        self.pbGetCurrentTime.setObjectName(_fromUtf8("pbGetCurrentTime"))

        self.retranslateUi(timeDlg)
        QtCore.QMetaObject.connectSlotsByName(timeDlg)

    def retranslateUi(self, timeDlg):
        timeDlg.setWindowTitle(_translate("timeDlg", "Edit Event Time", None))
        self.timeEdit.setDisplayFormat(_translate("timeDlg", "hh:mm:ss", None))
        self.okBtn.setText(_translate("timeDlg", "OK", None))
        self.cancelBtn.setText(_translate("timeDlg", "Cancel", None))
        self.label.setText(_translate("timeDlg", "Enter a date and time", None))
        self.pbGetCurrentTime.setText(_translate("timeDlg", "Get Current Time", None))

