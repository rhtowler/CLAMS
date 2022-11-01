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
import ui_QSCSTestPoll
import QSCSClient


class QSCSTestPoll(QMainWindow, ui_QSCSTestPoll.Ui_QSCSTestPoll):

    def __init__(self, host, port, parent=None):
        super(QSCSTestPoll, self).__init__(parent)
        self.setupUi(self)

        #  initialize variables
        self.__dataText = []
        self.__maxDataTextLines = 500
        self.host = host
        self.port = port

        #  create an instance of the QSCSClient
        self.scsClient = QSCSClient.QSCSClient(host, port)

        #  connect the signals and slots
        self.connect(self.sendButton, SIGNAL("clicked()"), self.__sendRequest)

        #  the SCS client emits 3 signals:
        #    SCSGetReceived - is emitted when a response to a "Get" request is received
        #    SCSSensorDescription - is emitted when a response to a "SensorDescription" request is received
        #    SCSError - is emitted when an error is encountered with an existing connection
        #  In this example we ignore the error signal...
        self.connect(self.scsClient, SIGNAL("SCSGetReceived"), self.__receiveGet)
        self.connect(self.scsClient, SIGNAL("SCSSensorDescription"), self.__receiveDescriptions)
        self.connect(self.scsClient, SIGNAL("SCSError"), self.__serverError)


        #  desensitize GUI elements
        self.sensorComboBox.setEnabled(False)
        self.sendButton.setEnabled(False)

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


    def __sendRequest(self):

        #  the user pressed the "send requenst" button - send the request
        #  for the currently selected sensor.
        #self.scsClient.getSensorDescriptions()

        sensor = self.sensorComboBox.currentText()
        if (sensor <> ''):
            self.scsClient.pollSensor([sensor])




    def __receiveGet(self, data):
        #  we've received sensor data, extract it and display
        for sensor in data:
            if (data[sensor]['data_value']):
                text = sensor + ': ' + data[sensor]['data_value']
            else:
                text = sensor + ': '
            self. __updateTextBox(text)


    def __receiveDescriptions(self, data):
        #  we've received the Sensor Description data - get the keys from
        #  the dictionary and populate the combo-box
        keys = data.keys()
        self.listosensors = []
        keys.sort()
        for k in keys:
            print k
            self.listosensors.append(k)
        self.sensorComboBox.clear()
        self.sensorComboBox.addItems(keys)

        #  enable the GUI elements
        self.sensorComboBox.setEnabled(True)
        self.sendButton.setEnabled(True)

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
