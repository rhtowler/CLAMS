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
import ui_QSCSTestSub
import QSCSClient


class QSCSTestSub(QMainWindow, ui_QSCSTestSub.Ui_QSCSTestSub):

    def __init__(self, host, port, sensorList, parent=None):
        super(QSCSTestSub, self).__init__(parent)
        self.setupUi(self)

        #  initialize variables
        self.host = host
        self.port = port
        self.sensorList = sensorList

        #  in this example we implement a simple reconnect mechanism that
        #  periodically attempts to reconnect to the server if our connection
        #  is interrupted for any reason. We create a timer and a couple of
        #  properties to do this.
        self.__reconnectTimer = QTimer(self)
        self.__reconnectTimer.setSingleShot(True)
        self.__reconnectTimer.connect(self.__reconnectTimer, SIGNAL("timeout()"), self.__reconnect)
        self.__retryInterval = 10
        self.__retrySecs = 0

        #  create an instance of the QSCSClient
        self.scsClient = QSCSClient.QSCSClient(host, port)

        #  connect the signals and slots. The SCS client emits 3 signals:
        #    SCSGetReceived - is emitted when a response to a "Get" request is received
        #    SCSSensorDescription - is emitted when a response to a "SensorDescription" request is received
        #    SCSError - is emitted when an error is encountered with an existing connection
        #
        #  In this example we don't request the sensor descriptions so we're not connecting that signal.
        self.connect(self.scsClient, SIGNAL("SCSGetReceived"), self.__receiveGet)
        self.connect(self.scsClient, SIGNAL("SCSError"), self.__scsError)

        #  create the subscription - To create a subscription you provide a list
        #  of sensor names and a polling rate in Hz. Note that it is not recommended
        #  to poll faster than 10Hz to limit load on the SCS server.
        self.scsSubscription = self.scsClient.subscribe(sensorList, 2)

        #  create a one shot timer to fire the connect method
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.start(100)
        self.connect(timer, SIGNAL("timeout()"), self.start)


    def start(self):
        """start initiates the connection to the SCS server
        """
        try:
            #  initiate connection with SCS server
            self.scsClient.connect()
            self.statusbar.showMessage('Connected to SCS server ' + self.host + ':' + self.port)

        except:
            #  there was a problem...
            self.statusbar.showMessage('Unable to connect to SCS server ' + self.host + ':' + self.port)


    def __receiveGet(self, data):
        #__receiveGet is called when Get request data is received by the SCS monitor.
        #This method simply extracts the wind speed, depth and COG data and updates
        #the appropriate GUI elements.

        #  iterate thru the data and update the GUI elements
        for sensor in data:
            try:
                #  determine which sensor this data is from. Note that we're
                #  assuming that the order of sensors in the list is:
                #  Wind speed, Depth, COG.

                #  get the index into the sensor list
                idx = self.sensorList.index(sensor)

                #  update the GUI elements
                if (idx == 0):
                    #  this is wind speed data
                    self.windspeed.display(data[sensor]['data_value'])
                    print data[sensor]['data_value']
                elif (idx == 1):
                    #  this is wind speed data
                    self.depth.display(data[sensor]['data_value'])
                elif (idx == 2):
                    #  this is wind speed data
                    self.cog.display(data[sensor]['data_value'])

            except:
                #  this sensor is not in our sensor list so just ignore it.
                #  This shouldn't ever happen though...
                pass


    def __scsError(self, scsError):
        #  this method is called if an error signal is emitted from the SCS client.
        #  Error signals are emitted when there is an error parsing the data
        #  received from the SCS server or when we lose our connection to the
        #  server.
        #
        #  In this example we're going to ignore parsing errors and implement a
        #  simple reconnect mechanism that will periodically try to reconnect
        #  to the server if we're disconnected.

        #  Check if this error is a disconnect error
        if (scsError.errCode == 1):
            #  error code 1 is a connection error - we've lost our connection
            self.statusbar.showMessage('Lost connection to SCS server. Retrying in ' +
                                       str(self.__retryInterval) + ' seconds.')

            #  start the reconnect timer
            self.__reconnectTimer.start(1000)


    def __reconnect(self):
        #  this method is called by the reconnect timer whenever we lose our connection
        #  to the SCS server. This is intended to be a simple example of how to
        #  handle connection errors.

        #  update the retry counter
        self.__retrySecs = self.__retrySecs + 1

        #  check if its time to try to reconnect
        if (self.__retrySecs == self.__retryInterval):

            #  reset the retry counter
            self.__retrySecs = 0

            #  update the GUI
            self.statusbar.showMessage('Connecting to SCS server at ' + self.host + ':' + self.port)

            try:
                #  try to establish a connection with the server
                self.scsClient.connect()
                self.statusbar.showMessage('Connected to SCS server ' + self.host + ':' + self.port)
            except:
                #  we failed to connect - update the GUI and start the timer
                self.statusbar.showMessage('Lost connection to SCS server. Retrying in ' +
                                       str(self.__retryInterval - self.__retrySecs) + ' seconds.')
                self.__reconnectTimer.start(1000)
        else:
            #  it's not time yet, just update the GUI and start the timer
            self.statusbar.showMessage('Lost connection to SCS server. Retrying in ' +
                                       str(self.__retryInterval - self.__retrySecs) + ' seconds.')
            self.__reconnectTimer.start(1000)


    def closeEvent(self, event=None):
        #  we're closing down - disconnect the SCS client from the SCS server
       self.scsClient.disconnect()


if __name__ == "__main__":

    #  specify the SCS server and port number
    scsHost = '10.48.17.223'
    scsPort = '505'

    #  This list contains the sensor names which will be polled. These
    #  are in the following order: Wind speed, Depth, COG
    #
    #  THE SENSOR NAMES NEED TO BE MODIFIED FOR YOUR PARTICULAR SCS CONFIGURATION!
    #
    sensorList = ['MX420-SOG']#,'MX420-Lon','MX420-Lat']

    #  start the application
    app = QApplication(sys.argv)
    form = QSCSTestSub(scsHost, scsPort, sensorList)
    form.show()
    app.exec_()
