# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\KeyPad.ui'
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

class Ui_keypad(object):
    def setupUi(self, keypad):
        keypad.setObjectName(_fromUtf8("keypad"))
        keypad.resize(940, 600)
        self.groupBox = QtGui.QGroupBox(keypad)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 911, 281))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.E_Btn = QtGui.QPushButton(self.groupBox)
        self.E_Btn.setGeometry(QtCore.QRect(190, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.E_Btn.setFont(font)
        self.E_Btn.setObjectName(_fromUtf8("E_Btn"))
        self.I_Btn = QtGui.QPushButton(self.groupBox)
        self.I_Btn.setGeometry(QtCore.QRect(590, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.I_Btn.setFont(font)
        self.I_Btn.setObjectName(_fromUtf8("I_Btn"))
        self.O_Btn = QtGui.QPushButton(self.groupBox)
        self.O_Btn.setGeometry(QtCore.QRect(670, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.O_Btn.setFont(font)
        self.O_Btn.setObjectName(_fromUtf8("O_Btn"))
        self.U_Btn = QtGui.QPushButton(self.groupBox)
        self.U_Btn.setGeometry(QtCore.QRect(510, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.U_Btn.setFont(font)
        self.U_Btn.setObjectName(_fromUtf8("U_Btn"))
        self.N_Btn = QtGui.QPushButton(self.groupBox)
        self.N_Btn.setGeometry(QtCore.QRect(480, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.N_Btn.setFont(font)
        self.N_Btn.setObjectName(_fromUtf8("N_Btn"))
        self.D_Btn = QtGui.QPushButton(self.groupBox)
        self.D_Btn.setGeometry(QtCore.QRect(210, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.D_Btn.setFont(font)
        self.D_Btn.setObjectName(_fromUtf8("D_Btn"))
        self.G_Btn = QtGui.QPushButton(self.groupBox)
        self.G_Btn.setGeometry(QtCore.QRect(370, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.G_Btn.setFont(font)
        self.G_Btn.setObjectName(_fromUtf8("G_Btn"))
        self.K_Btn = QtGui.QPushButton(self.groupBox)
        self.K_Btn.setGeometry(QtCore.QRect(610, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.K_Btn.setFont(font)
        self.K_Btn.setObjectName(_fromUtf8("K_Btn"))
        self.R_Btn = QtGui.QPushButton(self.groupBox)
        self.R_Btn.setGeometry(QtCore.QRect(270, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.R_Btn.setFont(font)
        self.R_Btn.setObjectName(_fromUtf8("R_Btn"))
        self.F_Btn = QtGui.QPushButton(self.groupBox)
        self.F_Btn.setGeometry(QtCore.QRect(290, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.F_Btn.setFont(font)
        self.F_Btn.setObjectName(_fromUtf8("F_Btn"))
        self.P_Btn = QtGui.QPushButton(self.groupBox)
        self.P_Btn.setGeometry(QtCore.QRect(750, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.P_Btn.setFont(font)
        self.P_Btn.setObjectName(_fromUtf8("P_Btn"))
        self.Q_Btn = QtGui.QPushButton(self.groupBox)
        self.Q_Btn.setGeometry(QtCore.QRect(30, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Q_Btn.setFont(font)
        self.Q_Btn.setObjectName(_fromUtf8("Q_Btn"))
        self.T_Btn = QtGui.QPushButton(self.groupBox)
        self.T_Btn.setGeometry(QtCore.QRect(350, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.T_Btn.setFont(font)
        self.T_Btn.setObjectName(_fromUtf8("T_Btn"))
        self.L_Btn = QtGui.QPushButton(self.groupBox)
        self.L_Btn.setGeometry(QtCore.QRect(690, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.L_Btn.setFont(font)
        self.L_Btn.setObjectName(_fromUtf8("L_Btn"))
        self.W_Btn = QtGui.QPushButton(self.groupBox)
        self.W_Btn.setGeometry(QtCore.QRect(110, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.W_Btn.setFont(font)
        self.W_Btn.setObjectName(_fromUtf8("W_Btn"))
        self.V_Btn = QtGui.QPushButton(self.groupBox)
        self.V_Btn.setGeometry(QtCore.QRect(320, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.V_Btn.setFont(font)
        self.V_Btn.setObjectName(_fromUtf8("V_Btn"))
        self.S_Btn = QtGui.QPushButton(self.groupBox)
        self.S_Btn.setGeometry(QtCore.QRect(130, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.S_Btn.setFont(font)
        self.S_Btn.setObjectName(_fromUtf8("S_Btn"))
        self.M_Btn = QtGui.QPushButton(self.groupBox)
        self.M_Btn.setGeometry(QtCore.QRect(560, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.M_Btn.setFont(font)
        self.M_Btn.setObjectName(_fromUtf8("M_Btn"))
        self.Y_Btn = QtGui.QPushButton(self.groupBox)
        self.Y_Btn.setGeometry(QtCore.QRect(430, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Y_Btn.setFont(font)
        self.Y_Btn.setObjectName(_fromUtf8("Y_Btn"))
        self.X_Btn = QtGui.QPushButton(self.groupBox)
        self.X_Btn.setGeometry(QtCore.QRect(160, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.X_Btn.setFont(font)
        self.X_Btn.setObjectName(_fromUtf8("X_Btn"))
        self.comma_Btn = QtGui.QPushButton(self.groupBox)
        self.comma_Btn.setGeometry(QtCore.QRect(640, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comma_Btn.setFont(font)
        self.comma_Btn.setObjectName(_fromUtf8("comma_Btn"))
        self.dot_Btn = QtGui.QPushButton(self.groupBox)
        self.dot_Btn.setGeometry(QtCore.QRect(720, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dot_Btn.setFont(font)
        self.dot_Btn.setObjectName(_fromUtf8("dot_Btn"))
        self.spaceBtn = QtGui.QPushButton(self.groupBox)
        self.spaceBtn.setGeometry(QtCore.QRect(120, 210, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spaceBtn.setFont(font)
        self.spaceBtn.setObjectName(_fromUtf8("spaceBtn"))
        self.A_Btn = QtGui.QPushButton(self.groupBox)
        self.A_Btn.setGeometry(QtCore.QRect(50, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.A_Btn.setFont(font)
        self.A_Btn.setObjectName(_fromUtf8("A_Btn"))
        self.H_Btn = QtGui.QPushButton(self.groupBox)
        self.H_Btn.setGeometry(QtCore.QRect(450, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.H_Btn.setFont(font)
        self.H_Btn.setObjectName(_fromUtf8("H_Btn"))
        self.J_Btn = QtGui.QPushButton(self.groupBox)
        self.J_Btn.setGeometry(QtCore.QRect(530, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.J_Btn.setFont(font)
        self.J_Btn.setObjectName(_fromUtf8("J_Btn"))
        self.Z_Btn = QtGui.QPushButton(self.groupBox)
        self.Z_Btn.setGeometry(QtCore.QRect(80, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Z_Btn.setFont(font)
        self.Z_Btn.setObjectName(_fromUtf8("Z_Btn"))
        self.C_Btn = QtGui.QPushButton(self.groupBox)
        self.C_Btn.setGeometry(QtCore.QRect(240, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.C_Btn.setFont(font)
        self.C_Btn.setObjectName(_fromUtf8("C_Btn"))
        self.B_Btn = QtGui.QPushButton(self.groupBox)
        self.B_Btn.setGeometry(QtCore.QRect(400, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.B_Btn.setFont(font)
        self.B_Btn.setObjectName(_fromUtf8("B_Btn"))
        self._1_Btn = QtGui.QPushButton(self.groupBox)
        self._1_Btn.setGeometry(QtCore.QRect(10, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._1_Btn.setFont(font)
        self._1_Btn.setObjectName(_fromUtf8("_1_Btn"))
        self._2_Btn = QtGui.QPushButton(self.groupBox)
        self._2_Btn.setGeometry(QtCore.QRect(90, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._2_Btn.setFont(font)
        self._2_Btn.setObjectName(_fromUtf8("_2_Btn"))
        self._3_Btn = QtGui.QPushButton(self.groupBox)
        self._3_Btn.setGeometry(QtCore.QRect(170, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._3_Btn.setFont(font)
        self._3_Btn.setObjectName(_fromUtf8("_3_Btn"))
        self._4_Btn = QtGui.QPushButton(self.groupBox)
        self._4_Btn.setGeometry(QtCore.QRect(250, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._4_Btn.setFont(font)
        self._4_Btn.setObjectName(_fromUtf8("_4_Btn"))
        self._5_Btn = QtGui.QPushButton(self.groupBox)
        self._5_Btn.setGeometry(QtCore.QRect(330, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._5_Btn.setFont(font)
        self._5_Btn.setObjectName(_fromUtf8("_5_Btn"))
        self._6_Btn = QtGui.QPushButton(self.groupBox)
        self._6_Btn.setGeometry(QtCore.QRect(410, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._6_Btn.setFont(font)
        self._6_Btn.setObjectName(_fromUtf8("_6_Btn"))
        self._7_Btn = QtGui.QPushButton(self.groupBox)
        self._7_Btn.setGeometry(QtCore.QRect(490, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._7_Btn.setFont(font)
        self._7_Btn.setObjectName(_fromUtf8("_7_Btn"))
        self._8_Btn = QtGui.QPushButton(self.groupBox)
        self._8_Btn.setGeometry(QtCore.QRect(570, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._8_Btn.setFont(font)
        self._8_Btn.setObjectName(_fromUtf8("_8_Btn"))
        self._9_Btn = QtGui.QPushButton(self.groupBox)
        self._9_Btn.setGeometry(QtCore.QRect(650, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._9_Btn.setFont(font)
        self._9_Btn.setObjectName(_fromUtf8("_9_Btn"))
        self._0_Btn = QtGui.QPushButton(self.groupBox)
        self._0_Btn.setGeometry(QtCore.QRect(730, 10, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self._0_Btn.setFont(font)
        self._0_Btn.setObjectName(_fromUtf8("_0_Btn"))
        self.quest_Btn = QtGui.QPushButton(self.groupBox)
        self.quest_Btn.setGeometry(QtCore.QRect(800, 160, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.quest_Btn.setFont(font)
        self.quest_Btn.setObjectName(_fromUtf8("quest_Btn"))
        self.colon_Btn = QtGui.QPushButton(self.groupBox)
        self.colon_Btn.setGeometry(QtCore.QRect(770, 110, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.colon_Btn.setFont(font)
        self.colon_Btn.setObjectName(_fromUtf8("colon_Btn"))
        self.backBtn = QtGui.QPushButton(self.groupBox)
        self.backBtn.setGeometry(QtCore.QRect(810, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.dash_Btn = QtGui.QPushButton(self.groupBox)
        self.dash_Btn.setGeometry(QtCore.QRect(830, 60, 77, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dash_Btn.setFont(font)
        self.dash_Btn.setObjectName(_fromUtf8("dash_Btn"))
        self.dispEdit = QtGui.QTextEdit(keypad)
        self.dispEdit.setGeometry(QtCore.QRect(10, 40, 561, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dispEdit.setFont(font)
        self.dispEdit.setObjectName(_fromUtf8("dispEdit"))
        self.okBtn = QtGui.QPushButton(keypad)
        self.okBtn.setGeometry(QtCore.QRect(670, 510, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.cancelBtn = QtGui.QPushButton(keypad)
        self.cancelBtn.setGeometry(QtCore.QRect(340, 510, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.infoLabel = QtGui.QLabel(keypad)
        self.infoLabel.setGeometry(QtCore.QRect(20, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.clearBtn = QtGui.QPushButton(keypad)
        self.clearBtn.setGeometry(QtCore.QRect(10, 510, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.groupBox_2 = QtGui.QGroupBox(keypad)
        self.groupBox_2.setGeometry(QtCore.QRect(580, 39, 341, 161))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.upBtn = QtGui.QPushButton(self.groupBox_2)
        self.upBtn.setGeometry(QtCore.QRect(118, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.upBtn.setFont(font)
        self.upBtn.setObjectName(_fromUtf8("upBtn"))
        self.leftBtn = QtGui.QPushButton(self.groupBox_2)
        self.leftBtn.setGeometry(QtCore.QRect(20, 60, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.leftBtn.setFont(font)
        self.leftBtn.setObjectName(_fromUtf8("leftBtn"))
        self.rightBtn = QtGui.QPushButton(self.groupBox_2)
        self.rightBtn.setGeometry(QtCore.QRect(216, 60, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rightBtn.setFont(font)
        self.rightBtn.setObjectName(_fromUtf8("rightBtn"))
        self.downBtn = QtGui.QPushButton(self.groupBox_2)
        self.downBtn.setGeometry(QtCore.QRect(118, 110, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.downBtn.setFont(font)
        self.downBtn.setObjectName(_fromUtf8("downBtn"))

        self.retranslateUi(keypad)
        QtCore.QMetaObject.connectSlotsByName(keypad)

    def retranslateUi(self, keypad):
        keypad.setWindowTitle(_translate("keypad", "Keyboard", None))
        self.E_Btn.setText(_translate("keypad", "E", None))
        self.I_Btn.setText(_translate("keypad", "I", None))
        self.O_Btn.setText(_translate("keypad", "O", None))
        self.U_Btn.setText(_translate("keypad", "U", None))
        self.N_Btn.setText(_translate("keypad", "N", None))
        self.D_Btn.setText(_translate("keypad", "D", None))
        self.G_Btn.setText(_translate("keypad", "G", None))
        self.K_Btn.setText(_translate("keypad", "K", None))
        self.R_Btn.setText(_translate("keypad", "R", None))
        self.F_Btn.setText(_translate("keypad", "F", None))
        self.P_Btn.setText(_translate("keypad", "P", None))
        self.Q_Btn.setText(_translate("keypad", "Q", None))
        self.T_Btn.setText(_translate("keypad", "T", None))
        self.L_Btn.setText(_translate("keypad", "L", None))
        self.W_Btn.setText(_translate("keypad", "W", None))
        self.V_Btn.setText(_translate("keypad", "V", None))
        self.S_Btn.setText(_translate("keypad", "S", None))
        self.M_Btn.setText(_translate("keypad", "M", None))
        self.Y_Btn.setText(_translate("keypad", "Y", None))
        self.X_Btn.setText(_translate("keypad", "X", None))
        self.comma_Btn.setText(_translate("keypad", ",", None))
        self.dot_Btn.setText(_translate("keypad", ".", None))
        self.spaceBtn.setText(_translate("keypad", "Space", None))
        self.A_Btn.setText(_translate("keypad", "A", None))
        self.H_Btn.setText(_translate("keypad", "H", None))
        self.J_Btn.setText(_translate("keypad", "J", None))
        self.Z_Btn.setText(_translate("keypad", "Z", None))
        self.C_Btn.setText(_translate("keypad", "C", None))
        self.B_Btn.setText(_translate("keypad", "B", None))
        self._1_Btn.setText(_translate("keypad", "1", None))
        self._2_Btn.setText(_translate("keypad", "2", None))
        self._3_Btn.setText(_translate("keypad", "3", None))
        self._4_Btn.setText(_translate("keypad", "4", None))
        self._5_Btn.setText(_translate("keypad", "5", None))
        self._6_Btn.setText(_translate("keypad", "6", None))
        self._7_Btn.setText(_translate("keypad", "7", None))
        self._8_Btn.setText(_translate("keypad", "8", None))
        self._9_Btn.setText(_translate("keypad", "9", None))
        self._0_Btn.setText(_translate("keypad", "0", None))
        self.quest_Btn.setText(_translate("keypad", "?", None))
        self.colon_Btn.setText(_translate("keypad", ":", None))
        self.backBtn.setText(_translate("keypad", "Backspace", None))
        self.dash_Btn.setText(_translate("keypad", "-", None))
        self.okBtn.setText(_translate("keypad", "OK", None))
        self.cancelBtn.setText(_translate("keypad", "Cancel", None))
        self.infoLabel.setText(_translate("keypad", "Type in your comment...", None))
        self.clearBtn.setText(_translate("keypad", "Clear", None))
        self.upBtn.setText(_translate("keypad", "^", None))
        self.leftBtn.setText(_translate("keypad", "<", None))
        self.rightBtn.setText(_translate("keypad", ">", None))
        self.downBtn.setText(_translate("keypad", "v", None))
