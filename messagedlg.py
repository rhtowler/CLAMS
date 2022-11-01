"""
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


class MessageDlg(QDialog, ui_MessageDlg.Ui_messageDlg):
    def __init__(self,  parent=None):
        super(MessageDlg, self).__init__(parent)
        self.setupUi(self)
        self.msgLabel.palette().setColor(self.msgLabel.backgroundRole(), QColor(255, 255, 255))
        self.connect(self.btn_2, SIGNAL("clicked()"), self.goNo)
        self.connect(self.btn_1, SIGNAL("clicked()"), self.goYes)
        self.connect(self.btn_3, SIGNAL("clicked()"), self.goYes)

    def setMessage(self, icon, sound, string, mode=''):
        sound.play()
        if mode.lower() == 'choice':
            self.btn_1.setText('Yes')
            self.btn_2.setText('No')
            self.btn_2.show()
            self.btn_3.hide()

        elif mode.lower() == 'specdel':
            self.btn_1.setText('Specimen')
            self.btn_2.setText('Cancel')
            self.btn_3.setText('Measurement')
            self.btn_2.show()
            self.btn_3.show()

        else:
            self.btn_1.setText('OK')
            self.btn_2.hide()
            self.btn_3.hide()

        self.msgLabel.setText(string)
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





