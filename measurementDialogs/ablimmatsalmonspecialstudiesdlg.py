
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_ABLImMatSalmonSpecialStudiesDlg

class ABLImMatSalmonSpecialStudiesDlg(QDialog, ui_ABLImMatSalmonSpecialStudiesDlg.Ui_ablimmatsalmonspeciesstudiesDlg):
    def __init__(self,  parent=None):
        super(ABLImMatSalmonSpecialStudiesDlg, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.otolithBtn, SIGNAL("clicked()"), self.getOtolith)
        self.connect(self.stomachBtn, SIGNAL("clicked()"), self.getStomach)
        self.connect(self.isotopeBtn, SIGNAL("clicked()"), self.getIsotope)
        self.connect(self.thiamineBtn, SIGNAL("clicked()"), self.getNutrition)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.Enter)
        self.connect(self.clearBtn, SIGNAL("clicked()"), self.Clear)


    def setup(self, parent):
        self.stomachBtn.setText('Stomach')
        self.otolithBtn.setText('Otolith')
        self.thiamineBtn.setText('Nutrition')
        self.isotopeBtn.setText('Isotope')

        self.stomach = ''
        self.isotope = ''
        self.thiamine = ''
        self.otolith = ''
        self.sp_st = ''
        self.sp_ot = ''
        self.sp_th = ''
        self.sp_is = ''

        self.stomachBtn.setChecked(False)
        self.otolithBtn.setChecked(False)
        self.thiamineBtn.setChecked(False)
        self.isotopeBtn.setChecked(False)

    def getStomach(self):
        self.stomach = 'STOM'
        self.stomachBtn.setText('Collected')
        self.sp_st = ','

    def getIsotope(self):
        self.isotope = 'ISO'
        self.isotopeBtn.setText('Collected')
        self.sp_is = ','

    def getNutrition(self):
        self.thiamine = 'NUT'
        self.thiamineBtn.setText('Collected')
        self.sp_th = ','

    def getOtolith(self):
        self.otolith = 'OTO'
        self.otolithBtn.setText('Collected')
        self.sp_ot = ','

    def Clear(self):

        self.stomach = ''
        self.isotope = ''
        self.thiamine = ''
        self.otolith = ''
        self.sp_st = ''
        self.sp_ot = ''
        self.sp_is = ''
        self.sp_th = ''
        self.isotopeBtn.setText('Isotope')
        self.thiamineBtn.setText('Nutrition')
        self.stomachBtn.setText('Stomach')
        self.otolithBtn.setText('Otolith')

        self.stomachBtn.setChecked(False)
        self.otolithBtn.setChecked(False)
        self.isotopeBtn.setChecked(False)
        self.thiamineBtn.setChecked(False)

    def Enter(self):

        self.result = (True, self.stomach+self.sp_st+self.otolith+self.sp_ot+self.thiamine+self.sp_th+self.isotope)


        if self.result[-1] != '':
            if self.result[-1][-1] == ',':
                self.result = (True, self.result[-1][0:-1])
            self.accept()

    def closeEvent(self, event):

        self.result = (False, '')
        self.reject()
