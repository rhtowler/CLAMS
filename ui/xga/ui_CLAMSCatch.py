# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\CLAMSCatch.ui'
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

class Ui_clamsCatch(object):
    def setupUi(self, clamsCatch):
        clamsCatch.setObjectName(_fromUtf8("clamsCatch"))
        clamsCatch.setWindowModality(QtCore.Qt.NonModal)
        clamsCatch.resize(1020, 645)
        self.sciLabel = QtGui.QLabel(clamsCatch)
        self.sciLabel.setGeometry(QtCore.QRect(620, 40, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sciLabel.setFont(font)
        self.sciLabel.setAutoFillBackground(True)
        self.sciLabel.setFrameShape(QtGui.QFrame.Panel)
        self.sciLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.sciLabel.setLineWidth(1)
        self.sciLabel.setText(_fromUtf8(""))
        self.sciLabel.setObjectName(_fromUtf8("sciLabel"))
        self.sumTable = QtGui.QTableWidget(clamsCatch)
        self.sumTable.setEnabled(False)
        self.sumTable.setGeometry(QtCore.QRect(347, 370, 271, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sumTable.setFont(font)
        self.sumTable.setRowCount(0)
        self.sumTable.setColumnCount(2)
        self.sumTable.setObjectName(_fromUtf8("sumTable"))
        item = QtGui.QTableWidgetItem()
        self.sumTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.sumTable.setHorizontalHeaderItem(1, item)
        self.label_10 = QtGui.QLabel(clamsCatch)
        self.label_10.setGeometry(QtCore.QRect(619, 9, 162, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_7 = QtGui.QLabel(clamsCatch)
        self.label_7.setGeometry(QtCore.QRect(620, 90, 163, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_11 = QtGui.QLabel(clamsCatch)
        self.label_11.setGeometry(QtCore.QRect(20, 9, 163, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.bottomBox = QtGui.QGroupBox(clamsCatch)
        self.bottomBox.setGeometry(QtCore.QRect(10, 550, 1001, 61))
        self.bottomBox.setTitle(_fromUtf8(""))
        self.bottomBox.setObjectName(_fromUtf8("bottomBox"))
        self.delBtn = QtGui.QPushButton(self.bottomBox)
        self.delBtn.setGeometry(QtCore.QRect(170, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName(_fromUtf8("delBtn"))
        self.doneBtn = QtGui.QPushButton(self.bottomBox)
        self.doneBtn.setGeometry(QtCore.QRect(839, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.editBtn = QtGui.QPushButton(self.bottomBox)
        self.editBtn.setGeometry(QtCore.QRect(330, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName(_fromUtf8("editBtn"))
        self.commentBtn = QtGui.QPushButton(self.bottomBox)
        self.commentBtn.setGeometry(QtCore.QRect(653, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commentBtn.setFont(font)
        self.commentBtn.setObjectName(_fromUtf8("commentBtn"))
        self.transBtn = QtGui.QPushButton(self.bottomBox)
        self.transBtn.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.transBtn.setFont(font)
        self.transBtn.setObjectName(_fromUtf8("transBtn"))
        self.printBtn = QtGui.QPushButton(self.bottomBox)
        self.printBtn.setGeometry(QtCore.QRect(491, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printBtn.setFont(font)
        self.printBtn.setObjectName(_fromUtf8("printBtn"))
        self.picLabel = QtGui.QLabel(clamsCatch)
        self.picLabel.setGeometry(QtCore.QRect(350, 10, 261, 196))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.picLabel.setFont(font)
        self.picLabel.setAutoFillBackground(True)
        self.picLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.picLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.addspcBtn = QtGui.QPushButton(clamsCatch)
        self.addspcBtn.setGeometry(QtCore.QRect(350, 220, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.addspcBtn.setFont(font)
        self.addspcBtn.setObjectName(_fromUtf8("addspcBtn"))
        self.manualBtn = QtGui.QPushButton(clamsCatch)
        self.manualBtn.setGeometry(QtCore.QRect(20, 490, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manualBtn.setFont(font)
        self.manualBtn.setObjectName(_fromUtf8("manualBtn"))
        self.label_8 = QtGui.QLabel(clamsCatch)
        self.label_8.setGeometry(QtCore.QRect(350, 340, 163, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.speciesList = QtGui.QTableWidget(clamsCatch)
        self.speciesList.setGeometry(QtCore.QRect(20, 40, 311, 431))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.speciesList.setFont(font)
        self.speciesList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.speciesList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.speciesList.setObjectName(_fromUtf8("speciesList"))
        self.speciesList.setColumnCount(2)
        self.speciesList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.speciesList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.speciesList.setHorizontalHeaderItem(1, item)
        self.speciesList.verticalHeader().setDefaultSectionSize(60)
        self.speciesList.verticalHeader().setMinimumSectionSize(50)
        self.basketView = QtGui.QTableView(clamsCatch)
        self.basketView.setGeometry(QtCore.QRect(630, 120, 381, 411))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.basketView.setFont(font)
        self.basketView.setObjectName(_fromUtf8("basketView"))
        self.basketView.verticalHeader().setVisible(False)

        self.retranslateUi(clamsCatch)
        QtCore.QMetaObject.connectSlotsByName(clamsCatch)

    def retranslateUi(self, clamsCatch):
        clamsCatch.setWindowTitle(_translate("clamsCatch", "CLAMS Catch", None))
        item = self.sumTable.horizontalHeaderItem(0)
        item.setText(_translate("clamsCatch", "Weight", None))
        item = self.sumTable.horizontalHeaderItem(1)
        item.setText(_translate("clamsCatch", "Basket Count", None))
        self.label_10.setText(_translate("clamsCatch", "Today\'s Scientist", None))
        self.label_7.setText(_translate("clamsCatch", "Basket Weights", None))
        self.label_11.setText(_translate("clamsCatch", "Species List", None))
        self.delBtn.setText(_translate("clamsCatch", "Delete", None))
        self.doneBtn.setText(_translate("clamsCatch", "Done", None))
        self.editBtn.setText(_translate("clamsCatch", "Edit", None))
        self.commentBtn.setText(_translate("clamsCatch", "Comment", None))
        self.transBtn.setText(_translate("clamsCatch", "Transfer Weight", None))
        self.printBtn.setText(_translate("clamsCatch", "Print Label", None))
        self.addspcBtn.setText(_translate("clamsCatch", "Add Species", None))
        self.manualBtn.setText(_translate("clamsCatch", "Manual Weight", None))
        self.label_8.setText(_translate("clamsCatch", "Summary Table", None))
        item = self.speciesList.horizontalHeaderItem(0)
        item.setText(_translate("clamsCatch", "Species", None))
        item = self.speciesList.horizontalHeaderItem(1)
        item.setText(_translate("clamsCatch", "Parent", None))
