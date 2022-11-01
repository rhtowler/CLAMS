'''
    EventLauncher provides a GUI form that provides button to launch forms
    for the events configured in the CLAMS database.

    The events are queried from the application_events table and the gui is
    populated with buttons representing these events. Pressing a button
    executes a python module that collects the event data. An instance of
    the class identified in the application_events table is created with
    the database connection, schema, active ship and survey parameters passed
    to it.


'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from events import *
from ui.xga import ui_EventLauncher

class EventLauncher(QDialog, ui_EventLauncher.Ui_EventLauncher):

    def __init__(self, parent):
        super(EventLauncher, self).__init__(parent)
        self.setupUi(self)

        #  store our reference to our database connection
        self.db = parent.db

        self.parent = parent

        #  connect the cancel button signal
        self.connect(self.pbCancel, SIGNAL("clicked()"), self.cancelClicked)

        #  create a list of button references ordered from top to bottom
        self.eventButtons = [self.pbEvent1, self.pbEvent2, self.pbEvent3, self.pbEvent4,
                self.pbEvent5, self.pbEvent6, self.pbEvent7, self.pbEvent8]
        #  and connect their signals and initially hide all of them
        for button in self.eventButtons:
            self.connect(button, SIGNAL("clicked()"), self.eventButtonClicked)
            button.hide()

        #  now extract the events from the database and update the buttons
        #  application_events table with event name, file name, module name
        nEvents = 0
        query = QtSql.QSqlQuery("SELECT event_name, event_package, event_module, event_class, active FROM " +
                self.parent.schema + ".application_events ORDER BY event_name", self.db)
        self.eventInfo = {}
        while query.next():
            self.eventButtons[nEvents].setText(query.value(0).toString())
            active = query.value(4).toBool()
            if (active):
                self.eventButtons[nEvents].setEnabled(True)
                self.eventButtons[nEvents].show()
            else:
                self.eventButtons[nEvents].setEnabled(False)
            self.eventInfo[query.value(0).toString()] = [str(query.value(1).toString()),
                    str(query.value(2).toString()), str(query.value(3).toString())]
            nEvents = nEvents + 1


    def eventButtonClicked(self):

        #  get the event details
        eventDetails = self.eventInfo[QObject.sender(self).text()]

        #  import this module
        #exec('from events.' + eventDetails[0] + ' import ' + eventDetails[1])

        #  create a handle to its init function
        exec('eventFuncHandle=' + eventDetails[1] + '.' + eventDetails[2])

        #  hid the dialog
        self.hide()

        #  and use the handle to call the function
        eventFuncHandle(self.parent)

        #  close the dialog
        self.accept()


    def cancelClicked(self):
        self.reject()


    def closeEvent(self):
        self.reject()

