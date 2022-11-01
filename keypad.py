#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_KeyPad


class KeyPad(QDialog, ui_KeyPad.Ui_keypad):

    def __init__(self, message,  parent=None):
        super(KeyPad,  self).__init__(parent)
        self.setupUi(self)
        self.dispEdit.setText(message)
#        buttons=['self._1_Btn', 'self._2_Btn', 'self._3_Btn', 'self._4_Btn', 'self._5_Btn', 'self._6_Btn',
#        'self._7_Btn', 'self._8_Btn', 'self._9_Btn', 'self._0_Btn']

        self.connect(self._1_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._2_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._3_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._4_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._5_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._6_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._7_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._8_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._9_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self._0_Btn, SIGNAL("clicked()"),self.getDigit)

        self.connect(self.A_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.B_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.C_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.D_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.E_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.F_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.G_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.H_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.J_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.K_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.I_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.L_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.M_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.N_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.O_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.P_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.Q_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.R_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.S_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.T_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.U_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.V_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.W_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.X_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.Y_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.Z_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.colon_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.comma_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.dot_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.quest_Btn, SIGNAL("clicked()"),self.getDigit)
        self.connect(self.dash_Btn, SIGNAL("clicked()"),self.getDigit)

        self.connect(self.spaceBtn, SIGNAL("clicked()"),self.getSpace)
        self.connect(self.backBtn, SIGNAL("clicked()"),self.getSpace)

        self.connect(self.cancelBtn, SIGNAL("clicked()"),self.Cancel)
        self.connect(self.clearBtn, SIGNAL("clicked()"),self.Clear)
        self.connect(self.okBtn, SIGNAL("clicked()"),self.Enter)
        self.okFlag=False



    def getDigit(self):
        self.dispEdit.insertPlainText(self.sender().text())

    def getSpace(self):
        button = self.sender().text()
        existing = self.dispEdit.toPlainText ()
        if button=='Space':
            self.dispEdit.insertPlainText(' ')
        else:# backspace
            self.dispEdit.setText(existing[:-1])
            p=self.dispEdit.textCursor()
            p.setPosition(len(existing)-1)
            self.dispEdit.setTextCursor(p)


    def Clear(self):
        self.dispEdit.clear()

    def Cancel(self):
        self.okFlag=False
        self.done(1)


    def Enter(self):
        self.okFlag=True
        self.done(1)





