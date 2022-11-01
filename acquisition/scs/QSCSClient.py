
from PyQt4.QtCore import *
import QSCSTelnetThread

class QSCSClient(QObject):
    """A class for acquiring data from the NOAA Scientific Computer System.

    What is SCS? From the manual:

    "The Scientific Computer System (SCS) is a data acquisition and display
    system designed for Oceanographic, Atmospheric, and Fisheries research
    applications. It acquires sensor data from shipboard oceanographic,
    atmospheric, and fisheries sensors and provides this information to
    scientists in real time via text and graphic displays, while simultaneously
    logging the data to disk for later analysis.  SCS also performs quality
    checks by monitoring I/O, providing delta/range checks and plotting data
    after acquisition."

    This client provides methods to query data from an existing SCS server.
    You can perform ad-hoc sensor queries, or create subscriptions that poll
    the server at a specified rate.

    **Public Methods**

    **connect** -- connect to the SCS server. This method establishes the
    connection to the SCS server. If the connection cannot be established
    an error will be raised.

    **disconnect** -- Disconnect from the SCS server. This method will close
    the connection to the SCS server.

    **getSensorDescriptions** -- Request information about the configured
    sensors from the SCS server

    **pollSensor** -- pollSensor performs a one time query on a sensor or
    group of sensors.

    **subscribe** -- create a subscription which periodically polls the SCS server
    requesting data for a sensor or group of sensors.

    **unsubscribe** -- delete an existing subscription.

    Signals

    **SCSGetReceived** -- This signal is emitted when an SCS "Get" request is
    received. Get requests return data from

        @rtype: dictionary
        @returns: A dictionary keyed by sensor name. The values associated with
        the dictionary keys themselves are dictionaries containing the data associated
        with the sensor.

    **SCSSensorDescription** -- This signal is emitted when an SCS "SensorDescription"
    request is received. A sensor description request response contains the
    sensor names and all sorts of data about the individual sensors configured on
    the SCS server.

        @rtype: dictionary
        @returns: A dictionary keyed by sensor name. The values associated with
        the dictionary keys themselves are dictionaries containing the data associated
        with the sensor.

    **SCSError** -- This signal is emitted when there is a problem with the SCS client.

        @rtype: int
        @returns: A integer value representing the error. Values are:
        1 - Network error. The connection to the SCS server has been lost.
        2 - Parse error. The SCS client was unable to parse the data returned
        from the server. Usually this means that some data was corrupted upon
        delivery from the server to the client.

        @rtype: QSCSError
        @returns: A exception object containing a bit more information about the
        error.
    """

    def __init__(self, host, port, timeout=10, parent=None):
        """Initialize this SSCSMonitor instance."""
        QObject.__init__(self, parent)
        self.__subscriptions = dict()

        #  set the SCS server access method. For now we only support connections
        #  using telnet. Future versions will support the new web services interface
        #  that is being implemented in SCS and at that time this property will
        #  be exposed.
        self.__accessMethod = 'telnet'

        if (self.__accessMethod == 'telnet'):
            self.__scsMonitor = QSCSTelnetThread.QSCSTelnetThread(host, port,
                                    timeout=timeout, parent=self)
        elif (self.__accessMethod == 'wsdl'):
            #  WSDL interface is not implemented at this time
            pass

        #  connect the monitor signal
        QObject.connect(self.__scsMonitor, SIGNAL("_SCSDataReceived"), self.__rxData)


    def subscribe(self, sensorList, pollRate):
        """Subscriptions periodically poll the SCS server requesting data for a sensor or
        group of sensors. You provide a sensor list and a polling rate. Note that it is
        most efficient to group your sensors into as few subscriptions as possible to limit
        the number of requests to the SCS server. For example, if you have 5 sensors that
        you wish to poll once per second, create a single subscription containing those
        5 sensors instead of 5 separate subscriptions.

        *SensorList* is a list of strings containing the SCS sensor names you wish
        to include in this subscription.

        *pollRate* a number specifying the rate (in Hz) that the SCS server is polled.

        @rtype: QTimer
        @returns: A reference to the QTimer object which controls the polling of
        the SCS server.
        """

        #  create the XML request string for this subscription
        sensorNameList = self.__getSensorNameList(sensorList)
        data = '<SCSXMLTemplate><request_command>$Get</request_command>' + sensorNameList + '</SCSXMLTemplate>\n'

        #  create the timer for this subscription
        subTimer = QTimer(self)
        QObject.connect(subTimer, SIGNAL("timeout()"), self.__pollSubscriptions)
        subTimer.setInterval(int(1000 / pollRate))
        #  set the timer to singleShot so we can use the isActive property to
        #  determine when the timer has expired.
        subTimer.setSingleShot(True)
        if self.__scsMonitor.isRunning():
            subTimer.start()

        #  add this subscription to the subscription dictionary - we key the
        #  dictionary by the timer object and we also return a reference to the
        #  timer object as a subscription identifier.
        self.__subscriptions[subTimer] = data

        return subTimer


    def unsubscribe(self, subscriptionID):
        """unsubscribe stops the periodic polling of the SCS server for the given
        subscription. The timer assoiciated with the subscription is stopped and
        the subscription data is deleted from the client's list of subscriptions.

        *subscriptionID* is the subscription ID returned by the subscribe method.
        """

        if (subscriptionID in self.__subscriptions):
            #  stop the timer
            subscriptionID.stop()

            #  remove the subscription from the subscription dictionary
            del self.__subscriptions[subscriptionID]


    def __pollSubscriptions(self):
        #  __pollSubscriptions is called when a subscription timer expires.
        #  It determines which timer(s) expired and places their request on
        #  the Tx queue.

        for timer in self.__subscriptions:
            #  check which timer(s) have expired and poll their sensors
            if (not timer.isActive()):
                self.emit(SIGNAL("_txSCSData"), 'Get',  self.__subscriptions[timer])
                #  restart the timer
                timer.start()


    def getSensorDescriptions(self):
        """Queries the SCS server for the sensor configuration data and returns it
        in a dictionary. The dictionary keys are the SCS sensor names. The values
        associated with the keys are themselves dictionaries containing the
        individual sensor configuration parameters.
        """

        #  create the XML request string
        data = '<SCSXMLTemplate><request_command>$SensorDescription</request_command></SCSXMLTemplate>\n'

        #  add this request to the Tx queue
        self.emit(SIGNAL("_txSCSData"), 'SensorDescription', data)


    def pollSensor(self, sensorList):
        """ pollSensor performs a one time query on a sensor or group of sensors.

        *SensorList* is a list of strings containing the SCS sensor names you wish
        to include in this subscription.
        """

        #  create the XML request string
        sensorNameList = self.__getSensorNameList(sensorList)
        data = '<SCSXMLTemplate><request_command>$Get</request_command>' + sensorNameList + '</SCSXMLTemplate>\n'

        #  add this request to the Tx queue
        self.emit(SIGNAL("_txSCSData"), 'Get', data)


    def connect(self):
        """connect initiates a connection to the SCS server. If we are unable
        to connect to the server, an error is raised.
        """

        if (not self.__scsMonitor.isRunning()):

            #  open the connection to the SCS server
            self.__scsMonitor.startMonitor()

            #  start any subscription timers
            self.__startSubscriptionTimers()


    def disconnect(self,):
        """disconnect disconnects from the SCS server.
        """

        if (self.__scsMonitor.isRunning()):
            #  stop any subscription timers
            self.__stopSubscriptionTimers()

            #  stop the SCS monitor
            self.__scsMonitor.stopMonitor()


    def __del__(self):
        #Clean up the QSCSThread object if required.

        if self.__scsMonitor.isRunning():
            #  stop any subscription timers
            self.__stopSubscriptionTimers()

            #  stop the SCS monitor
            self.__scsMonitor.stopMonitor()


    def __rxData(self, type, data):
        #  re-emit monitor signals based on the type of data they contain
        if (type.lower() == 'get'):
            #  emit signal for "Get" requests
            self.emit(SIGNAL("SCSGetReceived"), data)
        elif (type.lower() == 'sensordescription'):
            #  emit signal for "SensorDescription" requests
            self.emit(SIGNAL("SCSSensorDescription"), data)
        else:
            #  this is an error signal

            #  for connection errors we stop any subscription timers
            #if (data.errCode == 1):
            self.__stopSubscriptionTimers()

            #  emit the SCS error signal
            self.emit(SIGNAL("SCSError"), data)


    def __getSensorNameList(self, sensorList):
        #  creates the XML sensor name list from a list of sensor names. Note
        #  that we must convert QStrings to standard python strings lest they
        #  cause problems.

        xml = '<SensorNameList>'
        for sensor in sensorList:
            xml = xml + '<sensor_name>' + str(sensor) + '</sensor_name>'
        xml = xml + '</SensorNameList>'

        return xml


    def __stopSubscriptionTimers(self):
        #  stop all subscription timers
        for subscriptionID in self.__subscriptions:
            subscriptionID.stop()


    def __startSubscriptionTimers(self):
        #  start all subscription timers
        for subscriptionID in self.__subscriptions:
            subscriptionID.start()
