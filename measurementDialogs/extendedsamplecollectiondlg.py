
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_ExtendedSampleCollection

class ExtendedSampleCollectionDlg(QDialog, ui_ExtendedSampleCollection.Ui_extendedsamplecollectionDlg):
    def __init__(self,  parent=None):
        super(ExtendedSampleCollectionDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.db

        self.buttons = [self.Btn1,  self.Btn2,  self.Btn3,  self.Btn4,  self.Btn5,  self.Btn6,  self.Btn7,
                                    self.Btn8,  self.Btn9,  self.Btn10,  self.Btn11,  self.Btn12,  self.Btn13,  self.Btn14]
        for btn in self.buttons:
            self.connect(btn, SIGNAL("clicked()"), self.select)
            btn.setEnabled(False)
        self.connect(self.doneBtn, SIGNAL("clicked()"), self.Enter)
        self.connect(self.clearBtn, SIGNAL("clicked()"), self.Clear)


    def setup(self, parent):


        self.survey=parent.survey
        self.ship=parent.ship
        self.activeHaul=parent.activeHaul
        self.activeSample = parent.activeSample
        self.specimenKey = parent.specimenKey
        
        self.list = []
        self.label = []
        self.code = []
        query = QtSql.QSqlQuery("SELECT ex_sample_code, button_text, active FROM extended_sample_collections "+
                            "WHERE active = 1 ORDER BY ex_sample_code")
        while query.next():
            self.code.append(query.value(0).toString())
            self.label.append(query.value(1).toString())
        for i in range(len(self.label)):
            self.buttons[i].show()
            self.buttons[i].setText(self.label[i])
            self.buttons[i].setEnabled(True)
            self.buttons[i].setChecked(False)
        # check to see if there's already something in the DB
        if self.specimenKey != None:
            query = QtSql.QSqlQuery("Select measurement_value FROM measurements WHERE  ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeHaul+ "AND sample_id="+self.activeSample+
                " AND specimen_id = " +self.specimenKey + " AND measurement_type = 'ex_sample_collections'")
            query
            query.first()
            if query.first():
                currentList = query.value(0).toString().split(',')
                for i in range(len(self.code)):
                    if self.code[i] in currentList:
                        self.list.append(self.code[i])
                        self.buttons[i].setText('Collected')
                        self.buttons[i].setChecked(True)

    def select(self):
        ind = self.buttons.index(self.sender())
        if self.code[ind] in self.list:
            self.sender().setText(self.label[ind])
            self.list.remove(self.code[ind])
            self.buttons[i].setChecked(False)
        else:
            self.sender().setText('Collected')
            self.list.append(self.code[ind])
            self.buttons[i].setChecked(True)
        #

    def Clear(self):
        self.list = []
        self.label = []
        self.code = []
        query = QtSql.QSqlQuery("SELECT ex_sample_code, button_text, active FROM extended_sample_collections "+
                            "WHERE active = 1 ORDER BY ex_sample_code")
        while query.next():
            self.code.append(query.value(0).toString())
            self.label.append(query.value(1).toString())
        for i in range(len(self.label)):
            self.buttons[i].show()
            self.buttons[i].setText(self.label[i])
            self.buttons[i].setEnabled(True)
            self.buttons[i].setChecked(False)
            
    def Enter(self):
        listString = ''
        if self.list:
            self.list.sort()
            for code in self.list:
                listString = listString + code + ','
        else:
            listString = ' '

        self.result = (True, listString)
        if self.result[-1] != '':
            if self.result[-1][-1] == ',':
                self.result = (True, self.result[-1][0:-1])
            print self.result
            self.accept()

    def closeEvent(self, event):
 # query to clear and set new codes
        self.result = (False, '')
        self.reject()
