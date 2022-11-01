# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\AdminDlg.ui'
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

class Ui_admindlg(object):
    def setupUi(self, admindlg):
        admindlg.setObjectName(_fromUtf8("admindlg"))
        admindlg.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(admindlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(admindlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.createSurveyBtn = QtGui.QPushButton(admindlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.createSurveyBtn.setFont(font)
        self.createSurveyBtn.setObjectName(_fromUtf8("createSurveyBtn"))
        self.verticalLayout.addWidget(self.createSurveyBtn)
        self.selectSurveyBtn = QtGui.QPushButton(admindlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.selectSurveyBtn.setFont(font)
        self.selectSurveyBtn.setObjectName(_fromUtf8("selectSurveyBtn"))
        self.verticalLayout.addWidget(self.selectSurveyBtn)
        self.setupBtn = QtGui.QPushButton(admindlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.setupBtn.setFont(font)
        self.setupBtn.setObjectName(_fromUtf8("setupBtn"))
        self.verticalLayout.addWidget(self.setupBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneBtn = QtGui.QPushButton(admindlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.verticalLayout.addWidget(self.doneBtn)

        self.retranslateUi(admindlg)
        QtCore.QMetaObject.connectSlotsByName(admindlg)

    def retranslateUi(self, admindlg):
        admindlg.setWindowTitle(_translate("admindlg", "CLAMS Administration", None))
        self.label.setText(_translate("admindlg", "CLAMS Administration", None))
        self.createSurveyBtn.setText(_translate("admindlg", "Create Survey", None))
        self.selectSurveyBtn.setText(_translate("admindlg", "Change Active Survey", None))
        self.setupBtn.setText(_translate("admindlg", "Edit and Setup", None))
        self.doneBtn.setText(_translate("admindlg", "Done", None))

