"""
addspecedlg is a modified version of messagedlg used for confirming the active
species for the CLAMS catch dlg.

messagedlg is a generic message dialog that presents an icon, text, and
a set of buttons. The buttons presented depend on the 'mode' that is
passed when setMessage is called. The dialog returns the text of the button
that was selected by the user.

For example, the choice dialog presents "yes" and "no" buttons. In the example
below, the variable yesNo will contain either the string "Yes" or "No" depending
on what the user selects:

mDialog.setMessage(errorIcon, errorSounds, "Do you want to do this?", 'choice')
yesNo = self.message.exec_()

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_MessageDlg


class addspecedlg(QDialog, ui_MessageDlg.Ui_messageDlg):
    def __init__(self,  parent=None):
        super(addspecedlg, self).__init__(parent)
        self.setupUi(self)
        self.msgLabel.palette().setColor(self.msgLabel.backgroundRole(), QColor(255, 255, 255))
        self.connect(self.btn_2, SIGNAL("clicked()"), self.goNo)
        self.connect(self.btn_1, SIGNAL("clicked()"), self.goYes)
        self.connect(self.btn_3, SIGNAL("clicked()"), self.goYes)

    def setMessage(self, icon, sound, string, mode=''):
        sound.play()


        self.btn_1.setText('OK')
        self.btn_2.hide()
        self.btn_3.hide()

        self.msgLabel.setText(string)
        font = QFont()
        font.setBold(True)
        font.setPointSize(25)
        self.msgLabel.setFont(font)
        try:
            self.iconLabel.setMovie(icon)
            icon.start()
        except:
            self.iconLabel.setPixmap(icon)

    def goYes(self):
        self.response = self.sender().text()
        self.accept()

    def goNo(self):
        self.reject()





