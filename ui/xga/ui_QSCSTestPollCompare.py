# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QSCSTestPollCompare.ui'
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

class Ui_QSCSTestPollCompare(object):
    def setupUi(self, QSCSTestPollCompare):
        QSCSTestPollCompare.setObjectName(_fromUtf8("QSCSTestPollCompare"))
        QSCSTestPollCompare.resize(486, 312)
        self.centralwidget = QtGui.QWidget(QSCSTestPollCompare)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.compareButton = QtGui.QPushButton(self.centralwidget)
        self.compareButton.setObjectName(_fromUtf8("compareButton"))
        self.horizontalLayout.addWidget(self.compareButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.scsText = QtGui.QTextBrowser(self.centralwidget)
        self.scsText.setObjectName(_fromUtf8("scsText"))
        self.verticalLayout.addWidget(self.scsText)
        QSCSTestPollCompare.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(QSCSTestPollCompare)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QSCSTestPollCompare.setStatusBar(self.statusbar)

        self.retranslateUi(QSCSTestPollCompare)
        QtCore.QMetaObject.connectSlotsByName(QSCSTestPollCompare)

    def retranslateUi(self, QSCSTestPollCompare):
        QSCSTestPollCompare.setWindowTitle(_translate("QSCSTestPollCompare", "pyQt SCS Client Tester", None))
        self.compareButton.setText(_translate("QSCSTestPollCompare", "Compare", None))
        self.label_2.setText(_translate("QSCSTestPollCompare", "Sensors from database compared to SCS stream", None))

