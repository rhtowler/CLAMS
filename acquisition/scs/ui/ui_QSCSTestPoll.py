# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rtowler\AFSCsvn\CLAMS\trunk\application\acquisition\scs\ui\QSCSTestPoll.ui'
#
# Created: Mon Apr 18 11:08:22 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QSCSTestPoll(object):
    def setupUi(self, QSCSTestPoll):
        QSCSTestPoll.setObjectName(_fromUtf8("QSCSTestPoll"))
        QSCSTestPoll.resize(486, 312)
        self.centralwidget = QtGui.QWidget(QSCSTestPoll)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.sensorComboBox = QtGui.QComboBox(self.centralwidget)
        self.sensorComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.sensorComboBox.setObjectName(_fromUtf8("sensorComboBox"))
        self.horizontalLayout.addWidget(self.sensorComboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.scsText = QtGui.QTextBrowser(self.centralwidget)
        self.scsText.setObjectName(_fromUtf8("scsText"))
        self.verticalLayout.addWidget(self.scsText)
        QSCSTestPoll.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(QSCSTestPoll)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QSCSTestPoll.setStatusBar(self.statusbar)

        self.retranslateUi(QSCSTestPoll)
        QtCore.QMetaObject.connectSlotsByName(QSCSTestPoll)

    def retranslateUi(self, QSCSTestPoll):
        QSCSTestPoll.setWindowTitle(QtGui.QApplication.translate("QSCSTestPoll", "pyQt SCS Client Tester", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QSCSTestPoll", "SCS Sensor", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("QSCSTestPoll", "Send Request", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("QSCSTestPoll", "SCS Server Response", None, QtGui.QApplication.UnicodeUTF8))

