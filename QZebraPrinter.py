
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from acquisition.serial import SerialMonitor
from ui.xga import ui_PrinterAdminDlg

class QZebraPrinter(QObject):

    def __init__(self, QSerMonObj, deviceName, labelWidth=75, dpi=203, parent=None):
        '''
            The QZebraPrinter class provides methods for printing sample labels
            using the Zebra brand label printers and the EPL2 printer command set.

                QSerMonObj: A reference to the QSerialMonitor object that is managing
                            the printer connection.
                deviceName: A string containing the QSerialMonitor device name of the
                            printer.
                labelWidth: The label width in millimeters (75 is default)
                       dpi: The printer's DPI setting (203 is the default)

        '''

        #  call the superclass init
        QObject.__init__(self, parent)

        #  I believe these are fairly constant so we'll not expose them now...
        self.margin = 24
        self.mmToDots = 8
        self.QSerMonObj = QSerMonObj
        self.name = deviceName
        self.dpi = dpi

        #  set the label width in printer units (dots)
        self.labelWidth = int(labelWidth * self.mmToDots)

        #  define the ELP2/Zebra standard font sizes (in dots)
        #    The widths for 203 dpi fonts are tweaked slightly as the values
        #    in the docs didn't quite work out. The 300 dpi widths may need
        #    to be adjusted too.
        self.fontWidths = {203:[10,12,14,16,34],  # original widths: [8,10,12,14,32]
                           300:[12,16,20,24,48]
                          }
        self.fontHeights = {203:[12,16,20,24,48],
                            300:[20,28,36,44,80]
                           }

        #  connect the QSerialMonitor signal
        self.connect(self.QSerMonObj, SIGNAL("SerialDataReceived"), self.__rxData)


       #  send the reset command
        self.__txCommand('')
        self.__txCommand('')
        cmd = '^@'
        self.__txCommand(cmd)

        #  set a timer for 2 seconds to allow the printer to reset before sending more commands
        timer = QTimer(self)
        timer.timeout.connect(self.configurePrinter)
        timer.setSingleShot(True)
        timer.start(2000)


    def configurePrinter(self):

        #  set the label width
        #cmd = '\r\nq' + str(self.labelWidth)
        #self.__txCommand(cmd)
        pass

    def autoSenseMedia(self):
        '''
            autoSenseMedia will send the autosense command which is recommended
            after loading media into the printer.
        '''

        #  Send the autosense command to the printer
        self.__txCommand('')
        cmd = 'xa'
        self.__txCommand(cmd)


    def printSpecialSampleLabel1(self, data):
        '''
            printSpecialSampleLabel1 prints a "Special Studies" sample label.

                data:   Data is a dictionary containing the information required
                        to create the lable:

                            data={'title':'NOAA/AFSC/RACE/MACE',
                                  'ship':'DY',
                                  'survey':'201007',
                                  'haul':13,
                                  'specimen_id':42,
                                  'species_code':1234567,
                                  'common_name':'benttooth bristlemouth',
                                  'length':123.4,
                                  'sex':'Female',
                                  'weight':123,
                                  'maturity_table':3,
                                  'maturity_key':1,
                                  'scientist':'Homer Jay Simpson',
                                  'otolith':12345678
                                 }

        '''

        #  define the single column width
        width = self.labelWidth - (2 * self.margin)

        #  define left points of a 3 column layout (non-uniform widths)
        l3Col1 = self.margin
        l3ColWidth = int(self.labelWidth / 3) - (2 * self.margin)
        l3Col2 = int(self.labelWidth * 0.28) + self.margin
        l3Col3 = (int(self.labelWidth * 0.66)) + self.margin

        #  define left points of a 2 column layout
        l2Col1 = self.margin
        l2ColWidth = int(self.labelWidth / 2) - (2 * self.margin)
        l2Col2 = int(self.labelWidth / 2) + self.margin

        #  initiate new label
        self.__txCommand('')
        cmd = 'N'
        self.__txCommand(cmd)

        #  add the label title
        xpos = self.__hCenter(str(data['title']), 4)
        cmd = 'A' + str(xpos) + ',15,0,4,1,1,N,"' +str(data['title']) + '"'
        self.__txCommand(cmd)

        #  add the ship, survey, and haul in 3 columns
        cmd = 'A' + str(l3Col1) + ',40,0,3,1,1,N,"Ship: ' + str(data['ship']) + '"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l3Col2) + ',40,0,3,1,1,N,"Survey: ' +str(data['survey']) + '"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l3Col3) + ',40,0,3,1,1,N,"Haul: ' + str(data['haul']) + '"'
        self.__txCommand(cmd)

        #  add the specimen ID
        cmd = 'A' + str(l3Col1) + ',65,0,3,1,1,N,"Specimen ID: ' + str(data['specimen_id']) + '"'
        self.__txCommand(cmd)

        #  add the species code
        cmd = 'A' + str(l2Col1) + ',90,0,3,1,1,N,"Species Code: ' + str(data['species_code']) + '"'
        self.__txCommand(cmd)

        # add the common name (trim common name to fit)
        comName = self.__trimText('Common Name: ' + str(data['common_name']), 3, width)
        cmd = 'A' + str(l2Col1) + ',120,0,3,1,1,N,"' + comName + '"'
        self.__txCommand(cmd)

        #  add the length, sex in 2 columns
        cmd = 'A' + str(l2Col1) + ',145,0,3,1,1,N,"Length: ' + str(data['length']) + ' cm"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l2Col2) + ',145,0,3,1,1,N,"Sex: ' + str(data['sex']) + '"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l2Col1) + ',175,0,3,1,1,N,"Weight: ' + str(data['weight']) + ' kg"'
        self.__txCommand(cmd)

        #  add the maturity and maturity table
        cmd = 'A' + str(l2Col1) + ',205,0,3,1,1,N,"Maturity Stage: ' + str(data['maturity_key']) + '"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l2Col1) + ',235,0,3,1,1,N,"Maturity Table: ' + str(data['maturity_table']) + '"'
        self.__txCommand(cmd)

        #  add the scientist
        cmd = 'A' + str(l2Col1) + ',265,0,3,1,1,N,"Scientist: ' + str(data['scientist']) + '"'
        self.__txCommand(cmd)

        #  add the otolith number
        if ('otolith' in data.keys()):
            if (data['otolith']):
                cmd = 'A' + str(l2Col1) + ',305,0,3,1,1,N,"Otolith: ' + str(data['otolith']) + '"'
                self.__txCommand(cmd)

        #  and finally the specimen bar code
        cmd = 'B' + str(l2Col1 * 2) + ',345,0,3,4,8,75,B,"' + str(data['specimen_id']) + '"'
        self.__txCommand(cmd)

        #  print 1 copy of the label
        cmd = 'P1'
        self.__txCommand(cmd)


    def printSpecialSampleLabel2(self, data):
        '''
            printSpecialSampleLabel2 prints a "Special Studies" sample label.

                data:   Data is a dictionary containing the information required
                        to create the lable:

                            data={'title':'NOAA/AFSC/RACE/MACE',
                                  'ship':'DY',
                                  'survey':'201007',
                                  'haul':13,
                                  'species_code':1234567,
                                  'common_name':'benttooth bristlemouth',
                                  'date':'10/10/10',
                                  'sample_type':'Whole Fish',
                                  'count':10,
                                  'scientist':'Homer Jay Simpson'
                                 }

        '''

        #  define the single column width
        width = self.labelWidth - (2 * self.margin)

        #  define left points of a 3 column layout (non-uniform widths)
        l3Col1 = self.margin
        l3ColWidth = int(self.labelWidth / 3) - (2 * self.margin)
        l3Col2 = int(self.labelWidth * 0.28) + self.margin
        l3Col3 = (int(self.labelWidth * 0.66)) + self.margin

        #  define left points of a 2 column layout
        l2Col1 = self.margin
        l2ColWidth = int(self.labelWidth / 2) - (2 * self.margin)
        l2Col2 = int(self.labelWidth / 2) + self.margin

        #  initiate new label
        self.__txCommand('')
        cmd = 'N'
        self.__txCommand(cmd)

        #  add the label title
        xpos = self.__hCenter(data['title'], 4)
        cmd = 'A' + str(xpos) + ',20,0,4,1,1,N,"' + str(data['title']) + '"'
        self.__txCommand(cmd)

        #  add the ship, survey, and haul in 3 columns
        cmd = 'A' + str(l3Col1) + ',60,0,3,1,1,N,"Ship: ' + str(data['ship']) + '"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l3Col2) + ',60,0,3,1,1,N,"Survey: ' + str(data['survey']) + '"'
        self.__txCommand(cmd)
        cmd = 'A' + str(l3Col3) + ',60,0,3,1,1,N,"Haul: ' + str(data['haul']) + '"'
        self.__txCommand(cmd)

        #  add the species code
        cmd = 'A' + str(l2Col1) + ',120,0,3,1,1,N,"Species Code: ' + str(data['species_code']) + '"'
        self.__txCommand(cmd)

        # add the common name (trim common name to fit)
        comName = self.__trimText('Common Name: ' + str(data['common_name']), 3, width)
        cmd = 'A' + str(l2Col1) + ',150,0,3,1,1,N,"' + comName + '"'
        self.__txCommand(cmd)

        #  add the lencollection date
        cmd = 'A' + str(l2Col1) + ',180,0,3,1,1,N,"Collection Date: ' + str(data['date']) + '"'
        self.__txCommand(cmd)

        #  add the sample type
        cmd = 'A' + str(l2Col1) + ',210,0,3,1,1,N,"Sample Type: ' + str(data['sample_type']) + '"'
        self.__txCommand(cmd)

        #  add the count
        cmd = 'A' + str(l2Col1) + ',240,0,3,1,1,N,"Count: ' + str(data['count']) + '"'
        self.__txCommand(cmd)

        #  add the scientist
        cmd = 'A' + str(l2Col1) + ',270,0,3,1,1,N,"Scientist: ' + str(data['scientist']) + '"'
        self.__txCommand(cmd)

        #  print 1 copy of the label
        cmd = 'P1'
        self.__txCommand(cmd)


    def __hCenter(self, text, fontSize):
        '''
            __hCenter calculates the horizontal starting position which will center
            the provided text string.

                text:   The text to be centered
            fontSize:   The font size of the text. Valid values are 1-5

        '''

        charWidth = self.fontWidths[self.dpi][fontSize - 1]
        totalWidth = len(text) * charWidth
        startPoint = (self.labelWidth - totalWidth) / 2
        if (startPoint < self.margin):
            startPoint = self.margin

        return startPoint


    def __trimText(self, text, fontSize, width):
        '''
            __trimText returns a string that has been trimmed to fit into a
            column of the specific width.

                text:   The text to be trimmed.
            fontSize:   The font size of the text. Valid values are 1-5
               width:   The width of the column in printer units.

        '''

        charWidth = self.fontWidths[self.dpi][fontSize - 1]
        maxChars = int(width / charWidth)

        return text[0:maxChars]


    def __txCommand(self, data):
        '''
            __txCommand sends the printer commands to the serial device.
        '''
        self.QSerMonObj.txData(self.name, data + '\n')


    def __rxData(self, device, data):
        '''
            __rxData is a private method that receivs data from the label printer.

            This method may be extended to process the configuration data that is
            sent from the printer after the print configuration command ("UQ" is sent.
            Some printers may return useful information. Our Zebra 2742 printers do
            not.

        '''

        if device == self.name:
            #  currently we just print out the data that is returned.
            print data



class AdministrationDialog(QDialog, ui_PrinterAdminDlg.Ui_printerAdminDlg):

    def __init__(self, comPort, parent=None):

        super(AdministrationDialog, self).__init__(parent)
        self.setupUi(self)

        self.smonitor = SerialMonitor.SerialMonitor()
        self.smonitor.addDevice('Printer', comPort, 9600, 'None','', '')
        self.printer = QZebraPrinter(self.smonitor, 'Printer')

        self.connect(self.detectMediaBtn, SIGNAL("clicked()"),self.detectMedia)
        self.connect(self.testFormat1Btn, SIGNAL("clicked()"),self.testLabel1)
        self.connect(self.testFormat2Btn, SIGNAL("clicked()"),self.testLabel2)

        timer = QTimer(self)
        timer.timeout.connect(self.openComPort)
        timer.setSingleShot(True)
        timer.start(0)


    def openComPort(self):
        '''
        '''

        try:
            self.smonitor.startMonitoring()
        except Exception, e:
            QMessageBox.critical(self, 'Error', e.errText)
            self.close()
            return


    def detectMedia(self):
        self.printer.autoSenseMedia()


    def testLabel1(self):

        data1={'title':'NOAA/AFSC/RACE/MACE',
              'ship':'DY',
              'survey':'201007',
              'haul':13,
              'specimen_id':42,
              'species_code':1234567,
              'common_name':'benttooth bristlemouth',
              'length':123.4,
              'sex':'Female',
              'weight':123,
              'maturity_table':3,
              'maturity_key':1,
              'scientist':'Homer Jay Simpson',
              'otolith':12345678
         }

        self.printer.printSpecialSampleLabel1(data1)


    def testLabel2(self):

        data2={'title':'NOAA/AFSC/RACE/MACE',
              'ship':'DY',
              'survey':'201007',
              'haul':13,
              'species_code':1234567,
              'common_name':'benttooth bristlemouth',
              'date':'10/10/10',
              'sample_type':'Whole Fish',
              'count':10,
              'scientist':'Homer Jay Simpson'
         }

        self.printer.printSpecialSampleLabel2(data2)


if __name__ == "__main__":
    import sys

    comPort = 'COM5'

    app = QApplication(sys.argv)
    form = AdministrationDialog(comPort)
    form.show()
    app.exec_()

