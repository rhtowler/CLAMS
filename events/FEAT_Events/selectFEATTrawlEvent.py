"""
selectFEATTrawlEvent is a helper function used to launch the FEAT select trawl event.
This helper function was needed to implement the new event launcher system.
New event forms should be written such that they do not need a helper function.
"""

import FEATTrawlEvent


class SelectFEATTrawlEvent():

    def __init__(self, parent):

        self.parent = parent
        # create an instance of the trawl event dialog and display
        trawl_event = FEATTrawlEvent.FEATTrawlEvent(self.parent)
        trawl_event.exec_()
        if trawl_event.result() == 1:
            self.parent.activeEvent = trawl_event.activeEvent
