# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\ScaleCardDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_scalecardDlg(object):
    def setupUi(self, scalecardDlg):
        scalecardDlg.setObjectName("scalecardDlg")
        scalecardDlg.resize(265, 302)
        self.groupBox = QtWidgets.QGroupBox(scalecardDlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 241, 261))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.cardBtn = QtWidgets.QPushButton(self.groupBox)
        self.cardBtn.setGeometry(QtCore.QRect(10, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cardBtn.setFont(font)
        self.cardBtn.setObjectName("cardBtn")
        self.positionBtn = QtWidgets.QPushButton(self.groupBox)
        self.positionBtn.setGeometry(QtCore.QRect(10, 110, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.positionBtn.setFont(font)
        self.positionBtn.setObjectName("positionBtn")
        self.doneBtn = QtWidgets.QPushButton(self.groupBox)
        self.doneBtn.setGeometry(QtCore.QRect(10, 200, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(scalecardDlg)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(scalecardDlg)
        QtCore.QMetaObject.connectSlotsByName(scalecardDlg)

    def retranslateUi(self, scalecardDlg):
        _translate = QtCore.QCoreApplication.translate
        scalecardDlg.setWindowTitle(_translate("scalecardDlg", "Scale Location"))
        self.cardBtn.setText(_translate("scalecardDlg", "enter"))
        self.positionBtn.setText(_translate("scalecardDlg", "enter"))
        self.doneBtn.setText(_translate("scalecardDlg", "Done"))
        self.label.setText(_translate("scalecardDlg", "Card Number"))
        self.label_2.setText(_translate("scalecardDlg", "Card Position"))
        self.label_3.setText(_translate("scalecardDlg", "Fish Scale Location"))