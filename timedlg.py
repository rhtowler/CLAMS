from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_TimeDlg

class TimeDlg(QDialog, ui_TimeDlg.Ui_timeDlg):

    def __init__(self, parent=None):
        super(TimeDlg, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.okBtn, SIGNAL("clicked()"), self.exit)
        self.connect(self.pbGetCurrentTime, SIGNAL("clicked()"), self.getCurrentTime)
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.cancel)
        self.timeEdit.setDisplayFormat('hh:mm:ss.zzz')

    def setTime(self, time):
        initTime = QDateTime().fromString(time, 'MMddyyyy hh:mm:ss.zzz')
        self.dateEdit.setDate(initTime.date())
        self.timeEdit.setTime(initTime.time())

    def getCurrentTime(self):
        self.dateEdit.setDate(QDate.currentDate())
        self.timeEdit.setTime(QTime.currentTime())

    def enableGetTimeButton(self, enable):
        if enable:
            self.pbGetCurrentTime.setEnabled(True)
        else:
            self.pbGetCurrentTime.setEnabled(False)

    def cancel(self):
        self.time=None
        self.reject()

    def exit(self):
        # get times
        self.qTime=QDateTime(self.dateEdit.date(), self.timeEdit.time(),  Qt.LocalTime)
        self.time=self.qTime.toString('MMddyyyy hh:mm:ss.zzz')
        self.accept()


