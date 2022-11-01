# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\StreamLoadDlg.ui'
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

class Ui_streamloaddlg(object):
    def setupUi(self, streamloaddlg):
        streamloaddlg.setObjectName(_fromUtf8("streamloaddlg"))
        streamloaddlg.resize(400, 333)
        self.verticalLayout = QtGui.QVBoxLayout(streamloaddlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(streamloaddlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.loadSBEBtn = QtGui.QPushButton(streamloaddlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.loadSBEBtn.setFont(font)
        self.loadSBEBtn.setObjectName(_fromUtf8("loadSBEBtn"))
        self.verticalLayout.addWidget(self.loadSBEBtn)
        self.depthBtn = QtGui.QPushButton(streamloaddlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.depthBtn.setFont(font)
        self.depthBtn.setObjectName(_fromUtf8("depthBtn"))
        self.verticalLayout.addWidget(self.depthBtn)
        self.GPSBtn = QtGui.QPushButton(streamloaddlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.GPSBtn.setFont(font)
        self.GPSBtn.setObjectName(_fromUtf8("GPSBtn"))
        self.verticalLayout.addWidget(self.GPSBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.progressBar = QtGui.QProgressBar(streamloaddlg)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.doneBtn = QtGui.QPushButton(streamloaddlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.verticalLayout.addWidget(self.doneBtn)

        self.retranslateUi(streamloaddlg)
        QtCore.QMetaObject.connectSlotsByName(streamloaddlg)

    def retranslateUi(self, streamloaddlg):
        streamloaddlg.setWindowTitle(_translate("streamloaddlg", "CLAMS Utilities", None))
        self.label.setText(_translate("streamloaddlg", "Load Stream Data", None))
        self.loadSBEBtn.setText(_translate("streamloaddlg", "Load SBE file", None))
        self.depthBtn.setText(_translate("streamloaddlg", "Load EK60 Depth Data", None))
        self.GPSBtn.setText(_translate("streamloaddlg", "Load MX420 GPS Data", None))
        self.doneBtn.setText(_translate("streamloaddlg", "Done", None))

