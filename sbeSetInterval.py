
#  add the UI files to the python path
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import ui_sbeSetInterval


class sbeSetInterval(QDialog, ui_sbeSetInterval.Ui_sbeSetInterval):

    def __init__(self, parent=None):
        #  initialize the parents
        super(sbeSetInterval, self).__init__(parent)
        self.setupUi(self)

        self.lastVal = 0

        #  set up signals
        self.connect(self.spinInterval, SIGNAL("valueChanged(int)"), self.spinChanged)
        self.connect(self.pbOK, SIGNAL("clicked()"), self.okClicked)
        self.connect(self.pbCancel, SIGNAL("clicked()"), self.cancelClicked)


    def setInterval(self, interval, rto):

        self.spinInterval.setValue(int(interval))
        self.lastVal = self.spinInterval.value()
        self.cbRTO.setChecked(rto)


    def spinChanged(self, val):
        #  if the interval is set to 1 or 2, change it to 0
        if (val < 3) and (self.lastVal > 2):
            self.spinInterval.setValue(0)
        elif (val < 3) and (self.lastVal == 0):
            self.spinInterval.setValue(3)

        self.lastVal = self.spinInterval.value()


    def okClicked(self):

        self.emit(SIGNAL("sbeSetInterval"), self.spinInterval.value(), self.cbRTO.isChecked())
        self.accept()


    def cancelClicked(self):
        self.accept()


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    form = sbeSetInterval(34,True)
    form.show()
    app.exec_()
