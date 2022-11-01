# Checks devices available from SCS stream with devices in the devices table
# Will show which sensors match and which sensors are different from SCS.

#!/usr/bin/env python

#  add the UI files to the python path
import sys
import os
pyPath = reduce(lambda l,r: l + os.path.sep + r, os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
sys.path.append(os.path.join(pyPath, 'ui'))

#  import dependent modules
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from acquisition.scs import QSCSClient
from ui.xga import ui_QSCSTestPollCompare
import dbConnection


class QSCSTestPoll(QMainWindow, ui_QSCSTestPollCompare.Ui_QSCSTestPollCompare):

    def __init__(self, host, port, parent=None):
        super(QSCSTestPoll, self).__init__(parent)
        self.setupUi(self)
                
        self.odbc = 'afsc-64'
        self.dbUser = 'macebase2'
        self.dbPassword = 'pollock'
        self.bioSchema = 'clamsbase2'
        
        self.db = dbConnection.dbConnection(self.odbc, self.dbUser, self.dbPassword, 'TestPoll')
        self.db.dbOpen()
        
        self.connect(self.compareButton, SIGNAL("clicked()"), self.findDiffs)
        
        #  initialize variables
        self.__dataText = []
        self.__maxDataTextLines = 500
        self.host = host
        self.port = port

        #  create an instance of the QSCSClient
        self.scsClient = QSCSClient.QSCSClient(host, port)

        #  the SCS client emits 3 signals:
        #    SCSGetReceived - is emitted when a response to a "Get" request is received
        #    SCSSensorDescription - is emitted when a response to a "SensorDescription" request is received
        #    SCSError - is emitted when an error is encountered with an existing connection
        #  In this example we ignore the error signal...
        self.connect(self.scsClient, SIGNAL("SCSSensorDescription"), self.__receiveDescriptions)
        self.connect(self.scsClient, SIGNAL("SCSError"), self.__serverError)

        #  create a one shot timer to fire the connect method
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.start(100)
        self.connect(timer, SIGNAL("timeout()"), self.start)


    def start(self):
        """start initiates the connection to the SCS server and if successfull
        requests the sensor configuration information.
        """
        try:
            #  initiate connection with SCS server
            self.scsClient.connect()
            self.statusbar.showMessage('Connected to SCS server ' + self.host + ':' + self.port)

            #  request the sensor descriptions
            self.scsClient.getSensorDescriptions()

        except:
            #  there was a problem...
            self.statusbar.showMessage('Unable to connect to SCS server ' + self.host + ':' + self.port)


    def __receiveDescriptions(self, data):
        #  we've received the Sensor Description data - get the keys from
        #  the dictionary and populate the combo-box
        keys = data.keys()
        self.listosensors = []
        keys.sort()
        for k in keys:
            print k
            self.listosensors.append(k)
        
        
    def findDiffs(self):
        query = self.db.dbQuery("SELECT device_name FROM "+self.bioSchema+".devices WHERE DEVICE_ID>99 and DEVICE_ID<201")
        for device in query:
            if device[0] in self.listosensors:
                self.__updateTextBox('Looks good- '+device[0]+' in SCS')
            else:
                self.__updateTextBox('Warning! '+device[0]+' not in SCS')
                
        
    def __updateTextBox(self, data):

        #  update the display with this new line of text
        text = '<text style="color:black">' + data + '<br />'
        self.__dataText.append(text)
        if len(self.__dataText) > self.__maxDataTextLines:
            self.__dataText.pop(0)
        text = ''.join(self.__dataText)
        text = QString('<html><body><p>' + text + '</p></body></html>')
        self.scsText.setHtml(text)

        #  ensure that the window is scrolled to see the new line of text.
        self.scsText.verticalScrollBar().setValue(self.scsText.verticalScrollBar().maximum())

    def __serverError(self, data):
        print(data)

    def closeEvent(self, event=None):
        #  we're closing down - disconnect the SCS client from the SCS server
       self.scsClient.disconnect()


if __name__ == "__main__":

    scsHost = '10.48.17.223'
    scsPort = '505'

    app = QApplication(sys.argv)
    form = QSCSTestPoll(scsHost, scsPort)
    form.show()
    app.exec_()
