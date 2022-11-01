from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_ProcessDlg
import eventseldlg


class ProcessDlg(QDialog, ui_ProcessDlg.Ui_processDlg):

    def __init__(self, haul, time, parent=None):
        super(ProcessDlg, self).__init__(parent)
        self.setupUi(self)

        self.parent = parent

        self.connect(self.procBtn, SIGNAL("clicked()"), self.exit)
        self.connect(self.editBtn, SIGNAL("clicked()"), self.edit)
        self.connect(self.cancelBtn, SIGNAL("clicked()"), self.cancel)
        self.haulLabel.setText(haul)
        self.timeLabel.setText(time)
        if haul=='0':
            self.procBtn.setEnabled(False)
        
    def edit(self):
        hlDialog = eventseldlg.EventSelDlg(self.parent)
        hlDialog.newEventBtn.setEnabled(False)
        if hlDialog.exec_():
            self.activeEvent=hlDialog.activeEvent
            self.accept()
        
    def cancel(self):
        self.reject()
        
    def exit(self):
        # get times
        self.activeEvent=self.haulLabel.text()
        self.accept()


