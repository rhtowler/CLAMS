# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\EventLauncher.ui'
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

class Ui_EventLauncher(object):
    def setupUi(self, EventLauncher):
        EventLauncher.setObjectName(_fromUtf8("EventLauncher"))
        EventLauncher.resize(566, 551)
        self.verticalLayout = QtGui.QVBoxLayout(EventLauncher)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.pbEvent1 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent1.setFont(font)
        self.pbEvent1.setObjectName(_fromUtf8("pbEvent1"))
        self.verticalLayout.addWidget(self.pbEvent1)
        self.pbEvent2 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent2.setFont(font)
        self.pbEvent2.setObjectName(_fromUtf8("pbEvent2"))
        self.verticalLayout.addWidget(self.pbEvent2)
        self.pbEvent3 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent3.setFont(font)
        self.pbEvent3.setObjectName(_fromUtf8("pbEvent3"))
        self.verticalLayout.addWidget(self.pbEvent3)
        self.pbEvent4 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent4.setFont(font)
        self.pbEvent4.setObjectName(_fromUtf8("pbEvent4"))
        self.verticalLayout.addWidget(self.pbEvent4)
        self.pbEvent5 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent5.setFont(font)
        self.pbEvent5.setObjectName(_fromUtf8("pbEvent5"))
        self.verticalLayout.addWidget(self.pbEvent5)
        self.pbEvent6 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent6.setFont(font)
        self.pbEvent6.setObjectName(_fromUtf8("pbEvent6"))
        self.verticalLayout.addWidget(self.pbEvent6)
        self.pbEvent7 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent7.setFont(font)
        self.pbEvent7.setObjectName(_fromUtf8("pbEvent7"))
        self.verticalLayout.addWidget(self.pbEvent7)
        self.pbEvent8 = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbEvent8.setFont(font)
        self.pbEvent8.setObjectName(_fromUtf8("pbEvent8"))
        self.verticalLayout.addWidget(self.pbEvent8)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pbCancel = QtGui.QPushButton(EventLauncher)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pbCancel.setFont(font)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.verticalLayout.addWidget(self.pbCancel)

        self.retranslateUi(EventLauncher)
        QtCore.QMetaObject.connectSlotsByName(EventLauncher)

    def retranslateUi(self, EventLauncher):
        EventLauncher.setWindowTitle(_translate("EventLauncher", "Event Launcher", None))
        self.label.setText(_translate("EventLauncher", "Select the event to log", None))
        self.pbEvent1.setText(_translate("EventLauncher", "Event 1", None))
        self.pbEvent2.setText(_translate("EventLauncher", "Event 2", None))
        self.pbEvent3.setText(_translate("EventLauncher", "Event 3", None))
        self.pbEvent4.setText(_translate("EventLauncher", "Event 4", None))
        self.pbEvent5.setText(_translate("EventLauncher", "Event 5", None))
        self.pbEvent6.setText(_translate("EventLauncher", "Event 6", None))
        self.pbEvent7.setText(_translate("EventLauncher", "Event 7", None))
        self.pbEvent8.setText(_translate("EventLauncher", "Event 8", None))
        self.pbCancel.setText(_translate("EventLauncher", "Cancel", None))

