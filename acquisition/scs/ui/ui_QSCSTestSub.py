# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rtowler\AFSCsvn\CLAMS\trunk\application\acquisition\scs\ui\QSCSTestSub.ui'
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

class Ui_QSCSTestSub(object):
    def setupUi(self, QSCSTestSub):
        QSCSTestSub.setObjectName(_fromUtf8("QSCSTestSub"))
        QSCSTestSub.resize(526, 170)
        self.centralwidget = QtGui.QWidget(QSCSTestSub)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.windspeed = QtGui.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.windspeed.setFont(font)
        self.windspeed.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.windspeed.setProperty(_fromUtf8("intValue"), 12345)
        self.windspeed.setObjectName(_fromUtf8("windspeed"))
        self.gridLayout.addWidget(self.windspeed, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.depth = QtGui.QLCDNumber(self.centralwidget)
        self.depth.setObjectName(_fromUtf8("depth"))
        self.gridLayout.addWidget(self.depth, 2, 1, 1, 1)
        self.cog = QtGui.QLCDNumber(self.centralwidget)
        self.cog.setObjectName(_fromUtf8("cog"))
        self.gridLayout.addWidget(self.cog, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        QSCSTestSub.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(QSCSTestSub)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QSCSTestSub.setStatusBar(self.statusbar)

        self.retranslateUi(QSCSTestSub)
        QtCore.QMetaObject.connectSlotsByName(QSCSTestSub)

    def retranslateUi(self, QSCSTestSub):
        QSCSTestSub.setWindowTitle(QtGui.QApplication.translate("QSCSTestSub", "pyQt SCS Client Subscription Example", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QSCSTestSub", "Wind Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("QSCSTestSub", "Knots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("QSCSTestSub", "Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("QSCSTestSub", "Course Over Ground", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("QSCSTestSub", "Meters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("QSCSTestSub", "Degrees", None, QtGui.QApplication.UnicodeUTF8))

