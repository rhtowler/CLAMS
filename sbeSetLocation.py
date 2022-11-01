
#  add the UI files to the python path
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import ui_sbeSetLocation


class sbeSetLocation(QDialog, ui_sbeSetLocation.Ui_sbeSetLocation):

    def __init__(self, parent=None):
        #  initialize the parents
        super(sbeSetLocation, self).__init__(parent)
        self.setupUi(self)

        #  self.location stores the mounting location
        self.location = None

        #  since there is not a good way to identify specific SBE mounting
        #  location event_parameters, we will hard-code them here. Note that
        #  the values here are used for the combo-box item names and we will
        #  append "SBE" to them to use as the event_parameter value. For example,
        #  'Headrope' will be inserted in event_data as "HeadropeSBE"
        #  If you need to add a new location, it must first be added to the
        #  event_parameters table
        self.locations = ['Headrope', 'Footrope', 'Camtrawl', 'DropTS', 'Dropcam', 'Other']
        self.cbLocation.addItems(self.locations)

        #  set the combobox initial value - WE WANT IT TO DEFAULT TO HEADROPE
        self.cbLocation.setCurrentIndex(0)

        #  set up signals
        self.connect(self.pbOK, SIGNAL("clicked()"), self.okClicked)
        self.connect(self.pbCancel, SIGNAL("clicked()"), self.cancelClicked)


    def okClicked(self):

        self.location = str(self.cbLocation.currentText ()) + 'SBE'
        self.accept()


    def cancelClicked(self):
        self.location = None
        self.accept()


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    form = sbeSetLocation()
    form.show()
    app.exec_()
