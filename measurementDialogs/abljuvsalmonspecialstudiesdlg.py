
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_ABLJuvSalmonSpecialStudiesDlg

class ABLJuvSalmonSpecialStudiesDlg(QDialog, ui_ABLJuvSalmonSpecialStudiesDlg.Ui_abljuvsalmonspeciesstudiesDlg):
    def __init__(self,  parent=None):
        super(ABLJuvSalmonSpecialStudiesDlg, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.wfBtn, SIGNAL("clicked()"), self.getWF)
        self.connect(self.stomachBtn, SIGNAL("clicked()"), self.getStomach)
        self.connect(self.isotopeBtn, SIGNAL("clicked()"), self.getIsotope)
        self.connect(self.fhBtn, SIGNAL("clicked()"), self.getFH)
        self.connect(self.biaBtn, SIGNAL("clicked()"), self.getBIA)
        self.connect(self.igfBtn, SIGNAL("clicked()"), self.getIGF)
        self.connect(self.thiamineBtn, SIGNAL("clicked()"), self.getNutrition)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.Enter)
        self.connect(self.clearBtn, SIGNAL("clicked()"), self.Clear)


    def setup(self, parent):
        self.stomachBtn.setText('Stomach')
        self.wfBtn.setText('Whole Fish')
        self.fhBtn.setText('Fish Head')
        self.isotopeBtn.setText('Isotope')
        self.biaBtn.setText('BIA')
        self.igfBtn.setText('IGF')
        self.thiamineBtn.setText('Nutrition')

        self.stomach = ''
        self.isotope= ''
        self.wf = ''
        self.fh = ''
        self.bia = ''
        self.igf = ''
        self.thiamine = ''
        self.sp_st = ''
        self.sp_wf = ''
        self.sp_fh = ''
        self.sp_is = ''
        self.sp_igf = ''
        self.sp_bia = ''
        self.sp_th = ''

        self.stomachBtn.setChecked(False)
        self.wfBtn.setChecked(False)
        self.fhBtn.setChecked(False)
        self.isotopeBtn.setChecked(False)
        self.igfBtn.setChecked(False)
        self.biaBtn.setChecked(False)
        self.thiamineBtn.setChecked(False)

    def getStomach(self):
        self.stomach = 'STOM'
        self.stomachBtn.setText('Collected')
        self.sp_st = ','

    def getIsotope(self):
        self.isotope = 'ISO'
        self.isotopeBtn.setText('Collected')
        self.sp_is = ','

    def getWF(self):
        self.wf = 'WF'
        self.wfBtn.setText('Collected')
        self.sp_wf = ','

    def getFH(self):
        self.fh = 'FH'
        self.fhBtn.setText('Collected')
        self.sp_fh = ','

    def getIGF(self):
        self.igf = 'IGF'
        self.igfBtn.setText('Collected')
        self.sp_igf = ','

    def getBIA(self):
        self.bia = 'BIA'
        self.biaBtn.setText('Collected')
        self.sp_bia = ','

    def getNutrition(self):
        self.thiamine = 'NUT'
        self.thiamineBtn.setText('Collected')
        self.sp_th = ','

    def Clear(self):

        self.stomach = ''
        self.isotope = ''
        self.wf = ''
        self.fh = ''
        self.bia = ''
        self.igf = ''
        self.thiamine = ''
        self.sp_st = ''
        self.sp_wf = ''
        self.sp_fh = ''
        self.sp_is = ''
        self.sp_igf = ''
        self.sp_bia = ''
        self.sp_th = ''
        self.isotopeBtn.setText('Isotope')
        self.wfBtn.setText('Whole Fish')
        self.stomachBtn.setText('Stomach')
        self.fhBtn.setText('Fish Head')
        self.biaBtn.setText('BIA')
        self.igfBtn.setText('IGF')
        self.thiamineBtn.setText('Nutrition')

        self.stomachBtn.setChecked(False)
        self.wfBtn.setChecked(False)
        self.fhBtn.setChecked(False)
        self.biaBtn.setChecked(False)
        self.isotopeBtn.setChecked(False)
        self.igfBtn.setChecked(False)
        self.thiamineBtn.setChecked(False)


    def Enter(self):

        self.result = (True, self.thiamine+self.sp_th+self.stomach+self.sp_st+self.wf+self.sp_wf+self.fh+self.sp_fh+self.bia+self.sp_bia+self.igf+self.sp_igf+self.isotope)


        if self.result[-1] != '':
            if self.result[-1][-1] == ',':
                self.result = (True, self.result[-1][0:-1])
            self.accept()

    def closeEvent(self, event):

        self.result = (False, '')
        self.reject()
