'''
startABLTrawlEvent is a helper function used to launch the ABL trawl event.
This helper function was needed to implement the new event launcher system.
New event forms should be written such that they do not need a helper function.
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ctdEvent
import mooringEvent
import seabirdEvent
import eventseldlg
import interactioncheckdlg

class startCtdEvent():

    def __init__(self, parent):

        self.parent = parent

        #  create an instance of the event selection dialog
        hlDialog = eventseldlg.EventSelDlg(self.parent, 'CTD_Station')

        #  display the event select dialog
        if hlDialog.exec_():

            #  set the initial mammal and bird interaction checks to No
            self.parent.mammalStatus='N'
            self.parent.birdStatus='N'

            #  check if a event number was selected - exit if not
            if hlDialog.activeEvent==None:
                return

            #  set the active event
            self.parent.activeEvent = hlDialog.activeEvent
            self.parent.reloaded = hlDialog.reloaded

            # create an instance of the trawl event dialog and display
            Event = ctdEvent.ctdEvent(self.parent)
            Event.exec_()

class startSeabirdEvent():

    def __init__(self, parent):

        self.parent = parent

        #  create an instance of the event selection dialog
        hlDialog = eventseldlg.EventSelDlg(self.parent, 'Seabird_Station')

        #  display the event select dialog
        if hlDialog.exec_():

            #  set the initial mammal and bird interaction checks to No
            self.parent.mammalStatus='N'
            self.parent.birdStatus='N'

            #  check if a event number was selected - exit if not
            if hlDialog.activeEvent==None:
                return

            #  set the active event
            self.parent.activeEvent = hlDialog.activeEvent
            self.parent.reloaded = hlDialog.reloaded

            # create an instance of the trawl event dialog and display
            Event = seabirdEvent.seabirdEvent(self.parent)
            Event.exec_()
            
class startMooringEvent():

    def __init__(self, parent):

        self.parent = parent

        #  create an instance of the event selection dialog
        hlDialog = eventseldlg.EventSelDlg(self.parent, 'Mooring_Station')

        #  display the event select dialog
        if hlDialog.exec_():

            #  set the initial mammal and bird interaction checks to No
            self.parent.mammalStatus='N'
            self.parent.birdStatus='N'

            #  check if a event number was selected - exit if not
            if hlDialog.activeEvent==None:
                return

            #  set the active event
            self.parent.activeEvent = hlDialog.activeEvent
            self.parent.reloaded = hlDialog.reloaded

            # create an instance of the trawl event dialog and display
            Event = mooringEvent.mooringEvent(self.parent)
            Event.exec_()
