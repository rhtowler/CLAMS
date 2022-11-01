# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\EventSelDlg.ui'
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

class Ui_eventselDlg(object):
    def setupUi(self, eventselDlg):
        eventselDlg.setObjectName(_fromUtf8("eventselDlg"))
        eventselDlg.resize(543, 454)
        self.verticalLayout_2 = QtGui.QVBoxLayout(eventselDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(eventselDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.eventTable = QtGui.QTableWidget(eventselDlg)
        self.eventTable.setMaximumSize(QtCore.QSize(16777215, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eventTable.setFont(font)
        self.eventTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.eventTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.eventTable.setRowCount(10)
        self.eventTable.setColumnCount(3)
        self.eventTable.setObjectName(_fromUtf8("eventTable"))
        item = QtGui.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.eventTable)
        self.newEventBtn = QtGui.QPushButton(eventselDlg)
        self.newEventBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newEventBtn.setFont(font)
        self.newEventBtn.setObjectName(_fromUtf8("newEventBtn"))
        self.verticalLayout.addWidget(self.newEventBtn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelBtn = QtGui.QPushButton(eventselDlg)
        self.cancelBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.okBtn = QtGui.QPushButton(eventselDlg)
        self.okBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(eventselDlg)
        QtCore.QMetaObject.connectSlotsByName(eventselDlg)

    def retranslateUi(self, eventselDlg):
        eventselDlg.setWindowTitle(_translate("eventselDlg", "Event Selection", None))
        self.label.setText(_translate("eventselDlg", "Events in database", None))
        item = self.eventTable.horizontalHeaderItem(0)
        item.setText(_translate("eventselDlg", "Event", None))
        item = self.eventTable.horizontalHeaderItem(1)
        item.setText(_translate("eventselDlg", "Gear", None))
        item = self.eventTable.horizontalHeaderItem(2)
        item.setText(_translate("eventselDlg", "Haulback Time", None))
        self.newEventBtn.setText(_translate("eventselDlg", "Start New Event", None))
        self.cancelBtn.setText(_translate("eventselDlg", "Cancel", None))
        self.okBtn.setText(_translate("eventselDlg", "OK", None))

