# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\CLAMSEdit.ui'
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

class Ui_clamsEdit(object):
    def setupUi(self, clamsEdit):
        clamsEdit.setObjectName(_fromUtf8("clamsEdit"))
        clamsEdit.resize(1020, 760)
        self.deleteBtn = QtGui.QPushButton(clamsEdit)
        self.deleteBtn.setGeometry(QtCore.QRect(20, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName(_fromUtf8("deleteBtn"))
        self.tableBox = QtGui.QComboBox(clamsEdit)
        self.tableBox.setGeometry(QtCore.QRect(210, 30, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableBox.setFont(font)
        self.tableBox.setObjectName(_fromUtf8("tableBox"))
        self.label_4 = QtGui.QLabel(clamsEdit)
        self.label_4.setGeometry(QtCore.QRect(210, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.commitBtn = QtGui.QPushButton(clamsEdit)
        self.commitBtn.setGeometry(QtCore.QRect(20, 339, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commitBtn.setFont(font)
        self.commitBtn.setObjectName(_fromUtf8("commitBtn"))
        self.insertBtn = QtGui.QPushButton(clamsEdit)
        self.insertBtn.setGeometry(QtCore.QRect(20, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.insertBtn.setFont(font)
        self.insertBtn.setObjectName(_fromUtf8("insertBtn"))
        self.clearHaulBtn = QtGui.QPushButton(clamsEdit)
        self.clearHaulBtn.setGeometry(QtCore.QRect(20, 690, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearHaulBtn.setFont(font)
        self.clearHaulBtn.setObjectName(_fromUtf8("clearHaulBtn"))
        self.tableTypeBox = QtGui.QComboBox(clamsEdit)
        self.tableTypeBox.setGeometry(QtCore.QRect(20, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableTypeBox.setFont(font)
        self.tableTypeBox.setObjectName(_fromUtf8("tableTypeBox"))
        self.label_5 = QtGui.QLabel(clamsEdit)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cancelBtn = QtGui.QPushButton(clamsEdit)
        self.cancelBtn.setGeometry(QtCore.QRect(20, 460, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.dataView = QtGui.QTableView(clamsEdit)
        self.dataView.setGeometry(QtCore.QRect(210, 160, 781, 571))
        self.dataView.setObjectName(_fromUtf8("dataView"))
        self.fieldBox = QtGui.QComboBox(clamsEdit)
        self.fieldBox.setGeometry(QtCore.QRect(210, 100, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fieldBox.setFont(font)
        self.fieldBox.setObjectName(_fromUtf8("fieldBox"))
        self.label = QtGui.QLabel(clamsEdit)
        self.label.setGeometry(QtCore.QRect(460, 110, 46, 14))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.valueEdit = QtGui.QLineEdit(clamsEdit)
        self.valueEdit.setGeometry(QtCore.QRect(490, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valueEdit.setFont(font)
        self.valueEdit.setObjectName(_fromUtf8("valueEdit"))
        self.filterBtn = QtGui.QPushButton(clamsEdit)
        self.filterBtn.setGeometry(QtCore.QRect(730, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filterBtn.setFont(font)
        self.filterBtn.setObjectName(_fromUtf8("filterBtn"))
        self.label_6 = QtGui.QLabel(clamsEdit)
        self.label_6.setGeometry(QtCore.QRect(210, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(clamsEdit)
        self.label_7.setGeometry(QtCore.QRect(490, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(clamsEdit)
        QtCore.QMetaObject.connectSlotsByName(clamsEdit)

    def retranslateUi(self, clamsEdit):
        clamsEdit.setWindowTitle(_translate("clamsEdit", "CLAMS Data Editor", None))
        self.deleteBtn.setText(_translate("clamsEdit", "Delete Record", None))
        self.label_4.setText(_translate("clamsEdit", "Tables", None))
        self.commitBtn.setText(_translate("clamsEdit", "Commit changes", None))
        self.insertBtn.setText(_translate("clamsEdit", "Insert Record", None))
        self.clearHaulBtn.setText(_translate("clamsEdit", "Clear haul data", None))
        self.label_5.setText(_translate("clamsEdit", "Table Type", None))
        self.cancelBtn.setText(_translate("clamsEdit", "Cancel changes", None))
        self.label.setText(_translate("clamsEdit", "=", None))
        self.filterBtn.setText(_translate("clamsEdit", "Filter", None))
        self.label_6.setText(_translate("clamsEdit", "Field", None))
        self.label_7.setText(_translate("clamsEdit", "Value", None))

