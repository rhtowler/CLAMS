# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\NumPad.ui'
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
        numpad.resize(522, 562)
        self.verticalLayout = QtWidgets.QVBoxLayout(numpad)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msgLabel = QtWidgets.QLabel(numpad)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.msgLabel.setFont(font)
        self.msgLabel.setText("")
        self.msgLabel.setObjectName("msgLabel")
        self.verticalLayout.addWidget(self.msgLabel)
        self.dispBox = QtWidgets.QLabel(numpad)
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
        self.verticalLayout.addWidget(self.dispBox)
        self.groupBox = QtWidgets.QGroupBox(numpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.pBtn1 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn1.sizePolicy().hasHeightForWidth())
        self.pBtn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn1.setFont(font)
        self.pBtn1.setObjectName("pBtn1")
        self.gridLayout.addWidget(self.pBtn1, 0, 0, 1, 1)
        self.pBtn2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn2.sizePolicy().hasHeightForWidth())
        self.pBtn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn2.setFont(font)
        self.pBtn2.setObjectName("pBtn2")
        self.gridLayout.addWidget(self.pBtn2, 0, 1, 1, 1)
        self.pBtn3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn3.sizePolicy().hasHeightForWidth())
        self.pBtn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn3.setFont(font)
        self.pBtn3.setObjectName("pBtn3")
        self.gridLayout.addWidget(self.pBtn3, 0, 2, 1, 1)
        self.pBtn4 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn4.sizePolicy().hasHeightForWidth())
        self.pBtn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn4.setFont(font)
        self.pBtn4.setObjectName("pBtn4")
        self.gridLayout.addWidget(self.pBtn4, 1, 0, 1, 1)
        self.pBtn5 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn5.sizePolicy().hasHeightForWidth())
        self.pBtn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn5.setFont(font)
        self.pBtn5.setObjectName("pBtn5")
        self.gridLayout.addWidget(self.pBtn5, 1, 1, 1, 1)
        self.pBtn6 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn6.sizePolicy().hasHeightForWidth())
        self.pBtn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn6.setFont(font)
        self.pBtn6.setObjectName("pBtn6")
        self.gridLayout.addWidget(self.pBtn6, 1, 2, 1, 1)
        self.pBtn7 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn7.sizePolicy().hasHeightForWidth())
        self.pBtn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn7.setFont(font)
        self.pBtn7.setObjectName("pBtn7")
        self.gridLayout.addWidget(self.pBtn7, 2, 0, 1, 1)
        self.pBtn8 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn8.sizePolicy().hasHeightForWidth())
        self.pBtn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn8.setFont(font)
        self.pBtn8.setObjectName("pBtn8")
        self.gridLayout.addWidget(self.pBtn8, 2, 1, 1, 1)
        self.pBtn9 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn9.sizePolicy().hasHeightForWidth())
        self.pBtn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn9.setFont(font)
        self.pBtn9.setObjectName("pBtn9")
        self.gridLayout.addWidget(self.pBtn9, 2, 2, 1, 1)
        self.pBtnClr = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtnClr.sizePolicy().hasHeightForWidth())
        self.pBtnClr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pBtnClr.setFont(font)
        self.pBtnClr.setObjectName("pBtnClr")
        self.gridLayout.addWidget(self.pBtnClr, 3, 0, 1, 1)
        self.pBtn0 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn0.sizePolicy().hasHeightForWidth())
        self.pBtn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtn0.setFont(font)
        self.pBtn0.setObjectName("pBtn0")
        self.gridLayout.addWidget(self.pBtn0, 3, 1, 1, 1)
        self.pBtnd = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtnd.sizePolicy().hasHeightForWidth())
        self.pBtnd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.pBtnd.setFont(font)
        self.pBtnd.setObjectName("pBtnd")
        self.gridLayout.addWidget(self.pBtnd, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.pBtnEnt = QtWidgets.QPushButton(numpad)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pBtnEnt.setFont(font)
        self.pBtnEnt.setObjectName("pBtnEnt")
        self.verticalLayout.addWidget(self.pBtnEnt)

        self.retranslateUi(numpad)
        QtCore.QMetaObject.connectSlotsByName(numpad)

    def retranslateUi(self, numpad):
        _translate = QtCore.QCoreApplication.translate
        numpad.setWindowTitle(_translate("numpad", "NumPad"))
        self.pBtn1.setText(_translate("numpad", "1"))
        self.pBtn2.setText(_translate("numpad", "2"))
        self.pBtn3.setText(_translate("numpad", "3"))
        self.pBtn4.setText(_translate("numpad", "4"))
        self.pBtn5.setText(_translate("numpad", "5"))
        self.pBtn6.setText(_translate("numpad", "6"))
        self.pBtn7.setText(_translate("numpad", "7"))
        self.pBtn8.setText(_translate("numpad", "8"))
        self.pBtn9.setText(_translate("numpad", "9"))
        self.pBtnClr.setText(_translate("numpad", "Clear"))
        self.pBtn0.setText(_translate("numpad", "0"))
        self.pBtnd.setText(_translate("numpad", "."))
        self.pBtnEnt.setText(_translate("numpad", "Enter"))
