# Form implementation generated from reading ui file 'NumPad.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_numpad(object):
    def setupUi(self, numpad):
        numpad.setObjectName("numpad")
        numpad.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        numpad.resize(401, 518)
        self.groupBox = QtWidgets.QGroupBox(numpad)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 381, 311))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pBtn1 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn1.setGeometry(QtCore.QRect(10, 10, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn1.setFont(font)
        self.pBtn1.setObjectName("pBtn1")
        self.pBtn2 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn2.setGeometry(QtCore.QRect(130, 10, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn2.setFont(font)
        self.pBtn2.setObjectName("pBtn2")
        self.pBtn3 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn3.setGeometry(QtCore.QRect(250, 10, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn3.setFont(font)
        self.pBtn3.setObjectName("pBtn3")
        self.pBtn6 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn6.setGeometry(QtCore.QRect(250, 80, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn6.setFont(font)
        self.pBtn6.setObjectName("pBtn6")
        self.pBtn5 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn5.setGeometry(QtCore.QRect(130, 80, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn5.setFont(font)
        self.pBtn5.setObjectName("pBtn5")
        self.pBtn4 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn4.setGeometry(QtCore.QRect(10, 80, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn4.setFont(font)
        self.pBtn4.setObjectName("pBtn4")
        self.pBtn9 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn9.setGeometry(QtCore.QRect(250, 150, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn9.setFont(font)
        self.pBtn9.setObjectName("pBtn9")
        self.pBtn7 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn7.setGeometry(QtCore.QRect(10, 150, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn7.setFont(font)
        self.pBtn7.setObjectName("pBtn7")
        self.pBtn8 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn8.setGeometry(QtCore.QRect(130, 150, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn8.setFont(font)
        self.pBtn8.setObjectName("pBtn8")
        self.pBtnClr = QtWidgets.QPushButton(self.groupBox)
        self.pBtnClr.setGeometry(QtCore.QRect(10, 220, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pBtnClr.setFont(font)
        self.pBtnClr.setObjectName("pBtnClr")
        self.pBtnd = QtWidgets.QPushButton(self.groupBox)
        self.pBtnd.setGeometry(QtCore.QRect(250, 220, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnd.setFont(font)
        self.pBtnd.setObjectName("pBtnd")
        self.pBtn0 = QtWidgets.QPushButton(self.groupBox)
        self.pBtn0.setGeometry(QtCore.QRect(130, 220, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn0.setFont(font)
        self.pBtn0.setObjectName("pBtn0")
        self.pBtnEnt = QtWidgets.QPushButton(numpad)
        self.pBtnEnt.setGeometry(QtCore.QRect(20, 440, 361, 70))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pBtnEnt.setFont(font)
        self.pBtnEnt.setObjectName("pBtnEnt")
        self.dispBox = QtWidgets.QLabel(numpad)
        self.dispBox.setGeometry(QtCore.QRect(10, 50, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.dispBox.setFont(font)
        self.dispBox.setAutoFillBackground(True)
        self.dispBox.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.dispBox.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.dispBox.setText("")
        self.dispBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dispBox.setObjectName("dispBox")
        self.msgLabel = QtWidgets.QLabel(numpad)
        self.msgLabel.setGeometry(QtCore.QRect(20, 13, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.msgLabel.setFont(font)
        self.msgLabel.setText("")
        self.msgLabel.setObjectName("msgLabel")

        self.retranslateUi(numpad)
        QtCore.QMetaObject.connectSlotsByName(numpad)

    def retranslateUi(self, numpad):
        _translate = QtCore.QCoreApplication.translate
        numpad.setWindowTitle(_translate("numpad", "NumPad"))
        self.pBtn1.setText(_translate("numpad", "1"))
        self.pBtn2.setText(_translate("numpad", "2"))
        self.pBtn3.setText(_translate("numpad", "3"))
        self.pBtn6.setText(_translate("numpad", "6"))
        self.pBtn5.setText(_translate("numpad", "5"))
        self.pBtn4.setText(_translate("numpad", "4"))
        self.pBtn9.setText(_translate("numpad", "9"))
        self.pBtn7.setText(_translate("numpad", "7"))
        self.pBtn8.setText(_translate("numpad", "8"))
        self.pBtnClr.setText(_translate("numpad", "Clear"))
        self.pBtnd.setText(_translate("numpad", "."))
        self.pBtn0.setText(_translate("numpad", "0"))
        self.pBtnEnt.setText(_translate("numpad", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    numpad = QtWidgets.QDialog()
    ui = Ui_numpad()
    ui.setupUi(numpad)
    numpad.show()
    sys.exit(app.exec())
