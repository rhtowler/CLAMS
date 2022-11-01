# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CLAMS-Python-x64\CLAMS\ui\CatchSummaryLoader.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(420, 190)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pbUpdateSurvey = QtGui.QPushButton(self.centralwidget)
        self.pbUpdateSurvey.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbUpdateSurvey.setFont(font)
        self.pbUpdateSurvey.setObjectName(_fromUtf8("pbUpdateSurvey"))
        self.gridLayout.addWidget(self.pbUpdateSurvey, 1, 2, 1, 1)
        self.cbShip = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbShip.setFont(font)
        self.cbShip.setObjectName(_fromUtf8("cbShip"))
        self.gridLayout.addWidget(self.cbShip, 0, 1, 1, 1)
        self.cbSurvey = QtGui.QComboBox(self.centralwidget)
        self.cbSurvey.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbSurvey.setFont(font)
        self.cbSurvey.setObjectName(_fromUtf8("cbSurvey"))
        self.gridLayout.addWidget(self.cbSurvey, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cbEvent = QtGui.QComboBox(self.centralwidget)
        self.cbEvent.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbEvent.setFont(font)
        self.cbEvent.setObjectName(_fromUtf8("cbEvent"))
        self.gridLayout.addWidget(self.cbEvent, 2, 1, 1, 1)
        self.pbUpdateEvent = QtGui.QPushButton(self.centralwidget)
        self.pbUpdateEvent.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbUpdateEvent.setFont(font)
        self.pbUpdateEvent.setObjectName(_fromUtf8("pbUpdateEvent"))
        self.gridLayout.addWidget(self.pbUpdateEvent, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CLAMS Catch Summary Loader", None))
        self.label.setText(_translate("MainWindow", "CLAMS Catch Summary Table Loader", None))
        self.label_3.setText(_translate("MainWindow", "Survey", None))
        self.pbUpdateSurvey.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click this button to update <span style=\" font-weight:600;\">all events</span> in the selected survey.</p></body></html>", None))
        self.pbUpdateSurvey.setText(_translate("MainWindow", "Update Survey", None))
        self.label_4.setText(_translate("MainWindow", "Event", None))
        self.label_2.setText(_translate("MainWindow", "Ship", None))
        self.pbUpdateEvent.setToolTip(_translate("MainWindow", "Click this button to update the selected event.", None))
        self.pbUpdateEvent.setText(_translate("MainWindow", "Update Event", None))

