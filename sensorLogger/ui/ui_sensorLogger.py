# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\AKC0SS-N086\RACE_Users\rick.towler\My Documents\AFSCGit\SCS_Server\sensorLogger\ui\sensorLogger.ui'
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

class Ui_sensorLogger(object):
    def setupUi(self, sensorLogger):
        sensorLogger.setObjectName(_fromUtf8("sensorLogger"))
        sensorLogger.resize(782, 507)
        self.centralwidget = QtGui.QWidget(sensorLogger)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        sensorLogger.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(sensorLogger)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        sensorLogger.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(sensorLogger)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.retranslateUi(sensorLogger)
        QtCore.QMetaObject.connectSlotsByName(sensorLogger)

    def retranslateUi(self, sensorLogger):
        sensorLogger.setWindowTitle(_translate("sensorLogger", "sensorLogger", None))
        self.actionExit.setText(_translate("sensorLogger", "Exit", None))

