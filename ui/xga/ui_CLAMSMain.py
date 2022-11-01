# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\CLAMSMain.ui'
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

class Ui_clamsMain(object):
    def setupUi(self, clamsMain):
        clamsMain.setObjectName(_fromUtf8("clamsMain"))
        clamsMain.resize(1020, 750)
        clamsMain.setMinimumSize(QtCore.QSize(1020, 750))
        clamsMain.setMaximumSize(QtCore.QSize(1020, 750))
        self.centralwidget = QtGui.QWidget(clamsMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.picLabel = QtGui.QLabel(self.centralwidget)
        self.picLabel.setGeometry(QtCore.QRect(12, 4, 995, 740))
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(15, 4, 681, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(732, 399, 261, 333))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.trawlEventBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.trawlEventBtn.setEnabled(False)
        self.trawlEventBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.trawlEventBtn.setFont(font)
        self.trawlEventBtn.setObjectName(_fromUtf8("trawlEventBtn"))
        self.verticalLayout.addWidget(self.trawlEventBtn)
        self.procBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.procBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.procBtn.setFont(font)
        self.procBtn.setObjectName(_fromUtf8("procBtn"))
        self.verticalLayout.addWidget(self.procBtn)
        self.utilitiesBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.utilitiesBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.utilitiesBtn.setFont(font)
        self.utilitiesBtn.setObjectName(_fromUtf8("utilitiesBtn"))
        self.verticalLayout.addWidget(self.utilitiesBtn)
        self.adminBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.adminBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.adminBtn.setFont(font)
        self.adminBtn.setObjectName(_fromUtf8("adminBtn"))
        self.verticalLayout.addWidget(self.adminBtn)
        self.exitBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.exitBtn.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.verticalLayout.addWidget(self.exitBtn)
        self.shipLabel = QtGui.QLabel(self.centralwidget)
        self.shipLabel.setGeometry(QtCore.QRect(66, 618, 501, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.shipLabel.setFont(font)
        self.shipLabel.setObjectName(_fromUtf8("shipLabel"))
        self.shipLabel_2 = QtGui.QLabel(self.centralwidget)
        self.shipLabel_2.setGeometry(QtCore.QRect(15, 75, 671, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.shipLabel_2.setFont(font)
        self.shipLabel_2.setObjectName(_fromUtf8("shipLabel_2"))
        self.surveyLabel = QtGui.QLabel(self.centralwidget)
        self.surveyLabel.setGeometry(QtCore.QRect(23, 673, 671, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.surveyLabel.setFont(font)
        self.surveyLabel.setObjectName(_fromUtf8("surveyLabel"))
        self.schemaLabel = QtGui.QLabel(self.centralwidget)
        self.schemaLabel.setGeometry(QtCore.QRect(754, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.schemaLabel.setFont(font)
        self.schemaLabel.setText(_fromUtf8(""))
        self.schemaLabel.setObjectName(_fromUtf8("schemaLabel"))
        clamsMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(clamsMain)
        QtCore.QMetaObject.connectSlotsByName(clamsMain)

    def retranslateUi(self, clamsMain):
        clamsMain.setWindowTitle(_translate("clamsMain", "Catch Logger for Midwater Acoustic Surveys", None))
        self.titleLabel.setText(_translate("clamsMain", "Title Label", None))
        self.trawlEventBtn.setText(_translate("clamsMain", "Log Event", None))
        self.procBtn.setText(_translate("clamsMain", "Enter Catch", None))
        self.utilitiesBtn.setText(_translate("clamsMain", "Utilities", None))
        self.adminBtn.setText(_translate("clamsMain", "Administration", None))
        self.exitBtn.setText(_translate("clamsMain", "Exit", None))
        self.shipLabel.setText(_translate("clamsMain", "Ship:", None))
        self.shipLabel_2.setText(_translate("clamsMain", "Catch Logger for Acoustic Midwater Surveys", None))
        self.surveyLabel.setText(_translate("clamsMain", "Survey:", None))

