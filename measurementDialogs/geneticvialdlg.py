
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import ui_NumPad


class GeneticVialDlg(QDialog, ui_NumPad.Ui_numpad):
    def __init__(self,  parent=None):
        super(GeneticVialDlg, self).__init__(parent)
        self.setupUi(self)

        self.msgLabel.setText("Punch in the genetic vial number")
        self.value = None

        #  create the enter key filter
        enterEater = enterFilter(self.Enter, parent=self)

        #  set the background color of the textbox
        self.dispBox.palette().setColor(self.dispBox.backgroundRole(), QColor(255, 255, 255))

        #  connect the signals and install the event filters on the digit keys
        self.connect(self.pBtn1, SIGNAL("clicked()"), self.getDigit)
        self.pBtn1.installEventFilter(enterEater)
        self.connect(self.pBtn2, SIGNAL("clicked()"), self.getDigit)
        self.pBtn2.installEventFilter(enterEater)
        self.connect(self.pBtn3, SIGNAL("clicked()"), self.getDigit)
        self.pBtn3.installEventFilter(enterEater)
        self.connect(self.pBtn4, SIGNAL("clicked()"), self.getDigit)
        self.pBtn4.installEventFilter(enterEater)
        self.connect(self.pBtn5, SIGNAL("clicked()"), self.getDigit)
        self.pBtn5.installEventFilter(enterEater)
        self.connect(self.pBtn6, SIGNAL("clicked()"), self.getDigit)
        self.pBtn6.installEventFilter(enterEater)
        self.connect(self.pBtn7, SIGNAL("clicked()"), self.getDigit)
        self.pBtn7.installEventFilter(enterEater)
        self.connect(self.pBtn8, SIGNAL("clicked()"), self.getDigit)
        self.pBtn8.installEventFilter(enterEater)
        self.connect(self.pBtn9, SIGNAL("clicked()"), self.getDigit)
        self.pBtn9.installEventFilter(enterEater)
        self.connect(self.pBtn0, SIGNAL("clicked()"), self.getDigit)
        self.pBtn0.installEventFilter(enterEater)
        self.connect(self.pBtnd, SIGNAL("clicked()"), self.getDigit)
        self.pBtnd.installEventFilter(enterEater)
        self.connect(self.pBtnClr, SIGNAL("clicked()"), self.Clear)
        self.pBtnClr.installEventFilter(enterEater)
        self.connect(self.pBtnEnt, SIGNAL("clicked()"), self.Enter)


    def setup(self, parent):
        pass

    def getDigit(self, keyVal=None):
        
        if (keyVal == None):
            button = self.sender()
            s = button.text()
        else:
            s = QString(keyVal)
            
        x = s.toLong()
        p = self.dispBox.text()
        y = p.toLong()
        if x[1] :
            d=str(x[0])
            self.dispBox.setText(p+d)
        elif y[1] or p=="":
            d='.'
            self.dispBox.setText(p+d)


    def Clear(self):
        self.dispBox.setText("")


    def Enter(self):
        self.vial=self.dispBox.text()
        self.dispBox.setText("")
        self.result = (True, self.vial)
        self.accept()


    def closeEvent(self, event=None):
        self.result = (False, '')
        self.reject()



    def event(self, event):
        '''
        event reimplements QDialog.event() and captures key presses so the user
        can use the keyboard keypad to enter values in. This greatly speeds input
        on stattions that have keyboards (for example editing stations)
        '''

        if (event.type() == QEvent.KeyPress):

            if (event.key()==Qt.Key_0):
                self.getDigit(keyVal='0')
            if (event.key()==Qt.Key_1):
                self.getDigit(keyVal='1')
            if (event.key()==Qt.Key_2):
                self.getDigit(keyVal='2')
            if (event.key()==Qt.Key_3):
                self.getDigit(keyVal='3')
            if (event.key()==Qt.Key_4):
                self.getDigit(keyVal='4')
            if (event.key()==Qt.Key_5):
                self.getDigit(keyVal='5')
            if (event.key()==Qt.Key_6):
                self.getDigit(keyVal='6')
            if (event.key()==Qt.Key_7):
                self.getDigit(keyVal='7')
            if (event.key()==Qt.Key_8):
                self.getDigit(keyVal='8')
            if (event.key()==Qt.Key_9):
                self.getDigit(keyVal='9')
            if (event.key()==Qt.Key_Period):
                self.getDigit(keyVal='.')
            if (event.key()==Qt.Key_Enter):
                self.Enter()
            return True
        else:
            return QDialog.event(self, event)

class enterFilter(QObject):
    '''
    enterFilter is a simple Qt Event filter that eats Enter key presses allowing the
    numpad dialog to receive these events instead of the dialog button that has focus.
    '''
    def __init__(self, enterAction, parent=None):
        super(enterFilter, self).__init__(parent)
        self.enterAction = enterAction

    def eventFilter(self, obj, event):
        if (event.type() == QEvent.KeyPress) and (event.key()==Qt.Key_Enter):
            #  eat the enter key press
            self.enterAction()
            return True
        else:
            # not an enter key press - pass along
            return QObject.eventFilter(self, obj, event)
