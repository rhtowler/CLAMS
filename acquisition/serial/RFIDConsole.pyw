#!/usr/bin/env python

#  add the UI files to the python path
import sys
import os
pyPath = reduce(lambda l,r: l + os.path.sep + r, os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
sys.path.append(os.path.join(pyPath, 'ui'))


#  import dependent modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_SerialConsole
from acquisition.serial import SerialMonitor


class SerialConsole(QMainWindow, ui_SerialConsole.Ui_SerialConsole):

    def __init__(self, parent=None):
        super(SerialConsole, self).__init__(parent)
        self.setupUi(self)
        self.__dataText = []                 #  display log data
        self.__maxDataTextLines = 200        #  max number of lines displayed in the log window

        #  create the device dictionary
        devices = dict()

        #  DEVICE CONFIGURATION - THIS IS WHERE YOU DEFINE THE PORT SETTINGS
        #
        #  When specifying COM ports as integers, you start at 0. Thus 'COM1'
        #  is 0, 'COM5' is 4, etc.
        #
        #  The configuration dictionary is keyed by label. Typically the labels
        #  are set to the device that is attached to the port but this isn't required.
        #  The labels are simply labels and are used to identify which the ports. In
        #  this application the label is printed before the value that is received
        #  on the associated COM port. The dictionary value is a list
        #  in the form [COM port, Baud, Parse Type, Parse Expression, Parse Index]

        #  Set up the RFID reader - In this case we specify the RFID FDX-B format
        devices['RFID'] = [25, 9600, 'RFIDFDXB', '', 8]

        #  create an instance of the serial monitor
        self.smonitor = SerialMonitor.SerialMonitor()

        #  connect to the serial monitor's "SerialDataReceived" signal
        self.connect(self.smonitor, SIGNAL("SerialDataReceived"), self.showDisplay)

        #  add the devices to the serial monitor
        for device in devices.iteritems():
            self.smonitor.addDevice(device[0], device[1][0],device[1][1],device[1][2],device[1][3], device[1][4])

        try:
            self.smonitor.startMonitoring()
        except Exception, e:
            msgBox = QMessageBox.critical(self, 'Error', e.errText)
            #  set up a timer to close the application - need to do this via
            #  timer since we need to exit the init method before we can close
            #  the application window.
            self.__exitTimer = QTimer(self)
            self.__exitTimer.setSingleShot(True)
            self.__exitTimer.start(10)
            self.connect(self.__exitTimer, SIGNAL("timeout()"), SLOT('close()'))


    def showDisplay(self, name, val, err):

        if val:

            if (type(val).__name__ == 'list'):
                #  join the list into a single string
                val = ','.join(val)

            #  update the display with this new line of text
            text = '<text style="color:black">' + name + ' - ' + val + '<br />'
            self.__dataText.append(text)
            if len(self.__dataText) > self.__maxDataTextLines:
                self.__dataText.pop(0)
            text = ''.join(self.__dataText)
            text = QString('<html><body><p>' + text + '</p></body></html>')
            self.dataText.setHtml(text)

            #  ensure that the window is scrolled to see the new line of text.
            self.dataText.verticalScrollBar().setValue(self.dataText.verticalScrollBar().maximum())

        if err:
            # there was an error - update the error text
            text = err.errText
        else:
            text = ''

        text = QString('<html><body><p>' + text + '</p></body></html>')
        self.errText.setHtml(text)


    def closeEvent(self, event=None):
       self.smonitor.stopMonitoring()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = SerialConsole()
    form.show()
    app.exec_()
