
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import loadcelldialog
import bindialog
import numpad
from ui.xga import ui_HaulWtSelDlg


class HaulWtSelDlg(QDialog, ui_HaulWtSelDlg.Ui_haulwtselDlg):
    def __init__(self,  parent=None):
        super(HaulWtSelDlg, self).__init__(parent)
        self.setupUi(self)
        self.ok=False
        self.settings=parent.settings
        self.errorSounds=parent.errorSounds
        self.errorIcons=parent.errorIcons
        self.message=parent.message
        self.numpad=numpad.NumPad(self)

        self.btn_0.setText("Not Subsampled")
        self.btn_1.setText("Bin Volumetric")
        self.btn_2.setText("Load Cell")
        self.btn_3.setText("Guesstimate")

        # hook up slots
        self.connect(self.btn_0, SIGNAL("clicked()"), self.noSubsample)
        self.connect(self.btn_1, SIGNAL("clicked()"), self.binVolumetric)
        self.connect(self.btn_2, SIGNAL("clicked()"), self.loadCell)
        self.connect(self.btn_3, SIGNAL("clicked()"), self.getGuess)


    def noSubsample(self):

        self.weightType = "not_subsampled"
        self.weight = 'TBD'
        self.ok=True
        self.close()


    def binVolumetric(self):
        '''
            getBinVolumetric displays the modal bin dialog so the user
            can enter the value.  If the user clicks ok the weight
            label is updated.
        '''

        BinDlg = bindialog.BinDialog(self)
        if BinDlg.exec_():
            self.weight = BinDlg.haulWT
            self.weightType = "bin_volumetric"
            self.ok=True
            self.close()


    def loadCell(self):
        '''
            getLoadCell displays the modal load cell dialog so the user
            can enter the load cell value.  If the user clicks ok the weight
            label is updated.
        '''

        LCellDlg = loadcelldialog.LoadCellDialog(self)
        if LCellDlg.exec_():
            self.weight = LCellDlg.haulWt
            self.weightType = "load_cell"
            self.ok=True
            self.close()


    def getGuess(self):
        '''
            getGuess displays the number pad so the user can enter their
            visual estimate. If the user clicks ok the weight label is
            updated.
        '''
        self.numpad.msgLabel.setText("Enter your visual estimate" )
        if self.numpad.exec_():
            self.weight = self.numpad.value
            self.weightType = "visual_estimate"
            self.ok=True
            self.close()



