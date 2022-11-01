'''
startTrawlEvent is a helper function used to launch the MACE trawl event.
This helper function was needed to implement the new event launcher system.
New event forms should be written such that they do not need a helper function.
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MACETrawlEvent
import eventseldlg
import interactioncheckdlg

class startMACETrawlEvent():

    def __init__(self, parent):
        '''
            trawlEvent is a replacement for the SCS trawl event and the net config form
        '''

        self.parent = parent

        if not self.parent.testing:
            #  create an instance of the whale/bird interaction dialog and insert pictures
            intDlg = interactioncheckdlg.InteractionCheckDlg(self)
            pic = QImage()
            if pic.load(self.parent.settings[QString('ImageDir')] + '/backgrounds/mm.jpg'):
                pic = pic.scaledToHeight(intDlg.pic1.height(), Qt.SmoothTransformation)
                intDlg.pic1.setPixmap(QPixmap.fromImage(pic))
            pic = QImage()
            if pic.load(self.parent.settings[QString('ImageDir')] + '/backgrounds/es.jpg'):
                pic = pic.scaledToHeight(intDlg.pic2.height(), Qt.SmoothTransformation)
                intDlg.pic2.setPixmap(QPixmap.fromImage(pic))


        #  create an instance of the event selection dialog
        hlDialog = eventseldlg.EventSelDlg(self.parent)

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

            # 1-9-22 RHT: Disabled the old protected spp dialog since we added
            # a PS observation time prior to a trawl in the trawl event.

            #  if this is the first time we've run the event selection dialog
#            if not self.parent.testing:
#                #  display the interaction dialog.
#                if not hlDialog.reloaded:
#                    if intDlg.exec_():
#                        if intDlg.yesBtn1.isChecked():
#                            self.parent.mammalStatus='Y'
#                        if intDlg.yesBtn2.isChecked():
#                            self.parent.birdStatus='Y'
#                    if intDlg.returnFlag:
#                        return

            # create an instance of the trawl event dialog and display
            trawlEvent = MACETrawlEvent.MACETrawlEvent(self.parent)
            trawlEvent.exec_()
