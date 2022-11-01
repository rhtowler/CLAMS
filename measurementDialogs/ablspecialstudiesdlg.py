
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_ABLSpecialStudiesDlg

class ABLSpecialStudiesDlg(QDialog, ui_ABLSpecialStudiesDlg.Ui_ablspeciesstudiesDlg):
    def __init__(self,  parent=None):
        super(ABLSpecialStudiesDlg, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.otolithBtn, SIGNAL("clicked()"), self.getOtolith)
        self.connect(self.stomachBtn, SIGNAL("clicked()"), self.getStomach)
        self.connect(self.isotopeMarshBtn, SIGNAL("clicked()"), self.getIsotopeM)
        self.connect(self.isotopeAndrewsBtn, SIGNAL("clicked()"), self.getIsotopeA)
        self.connect(self.geneticsBtn, SIGNAL("clicked()"), self.getGenetics)
        self.connect(self.energeticBtn, SIGNAL("clicked()"), self.getEnergetic)
        self.connect(self.tsmriBtn, SIGNAL("clicked()"), self.getTSMRI)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.Enter)
        self.connect(self.clearBtn, SIGNAL("clicked()"), self.Clear)


    def setup(self, parent):
        self.stomachBtn.setText('Stomach')
        self.otolithBtn.setText('Otolith')
        self.geneticsBtn.setText('Genetics')
        self.isotopeMarshBtn.setText('Honeyfield')
        self.isotopeAndrewsBtn.setText('Isotope_Andrews')
        self.energeticBtn.setText('Energetics')
        self.tsmriBtn.setText('TSMRI')

        self.stomach = ''
        self.isotopeMarsh = ''
        self.isotopeAndrews = ''
        self.genetics = ''
        self.otolith = ''
        self.energetic = ''
        self.tsmri = ''
        self.sp_st = ''
        self.sp_ot = ''
        self.sp_ge = ''
        self.sp_isM = ''
        self.sp_isA = ''
        self.sp_en = ''
        self.sp_ts = ''

        self.stomachBtn.setChecked(False)
        self.otolithBtn.setChecked(False)
        self.geneticsBtn.setChecked(False)
        self.isotopeMarshBtn.setChecked(False)
        self.isotopeAndrewsBtn.setChecked(False)
        self.energeticBtn.setChecked(False)
        self.tsmriBtn.setChecked(False)

    def getStomach(self):
        self.stomach = 'STOM'
        self.stomachBtn.setText('Collected')
        self.sp_st = ','

    def getIsotopeM(self):
        self.isotopeMarsh = 'Honeyfield'
        self.isotopeMarshBtn.setText('Collected')
        self.sp_isM = ','

    def getIsotopeA(self):
        self.isotopeAndrews = 'ISO_Andrews'
        self.isotopeAndrewsBtn.setText('Collected')
        self.sp_isA = ','

    def getOtolith(self):
        self.otolith = 'OTO'
        self.otolithBtn.setText('Collected')
        self.sp_ot = ','

    def getGenetics(self):
        self.genetics = 'GEN'
        self.geneticsBtn.setText('Collected')
        self.sp_ge = ','

    def getTSMRI(self):
        self.tsmri = 'TSMRI'
        self.tsmriBtn.setText('Collected')
        self.sp_ts = ','

    def getEnergetic(self):
        self.energetic = 'ENRG'
        self.energeticBtn.setText('Collected')
        self.sp_en = ','

    def Clear(self):

        self.stomach = ''
        self.isotopeMarsh = ''
        self.isotopeAndrews = ''
        self.genetics = ''
        self.energetic = ''
        self.otolith = ''
        self.tsmri = ''
        self.sp_st = ''
        self.sp_ot = ''
        self.sp_ge = ''
        self.sp_isM = ''
        self.sp_isA = ''
        self.sp_en = ''
        self.sp_ts = ''
        self.isotopeMarshBtn.setText('Honeyfield')
        self.isotopeAndrewsBtn.setText('Isotope_Andrews')
        self.stomachBtn.setText('Stomach')
        self.otolithBtn.setText('Otolith')
        self.geneticsBtn.setText('Genetics')
        self.energeticBtn.setText('Energetics')
        self.tsmriBtn.setText('TSMRI')

        self.stomachBtn.setChecked(False)
        self.otolithBtn.setChecked(False)
        self.geneticsBtn.setChecked(False)
        self.energeticBtn.setChecked(False)
        self.isotopeMarshBtn.setChecked(False)
        self.isotopeAndrewsBtn.setChecked(False)
        self.tsmriBtn.setChecked(False)


    def Enter(self):

        self.result = (True, self.tsmri+self.sp_ts+self.stomach+self.sp_st+self.otolith+self.sp_ot+self.genetics+self.sp_ge+self.energetic+self.sp_en+self.isotopeMarsh+self.sp_isM+self.isotopeAndrews)


        if self.result[-1] != '':
            if self.result[-1][-1] == ',':
                self.result = (True, self.result[-1][0:-1])
            self.accept()

    def closeEvent(self, event):

        self.result = (False, '')
        self.reject()
