'''
QSCSServer is a very limited implementation of an SCS server. It only
implements a tiny subset of the SCS telnet based server suitable for use
with CLAMS in situations where running the full SCS application is too
much.

'''
import datetime
import re
from xml.etree import ElementTree as ETree
from PyQt4 import QtCore, QtNetwork

class QSCSServer(QtCore.QObject):

    #  define constants
    VERSION = 0.5

    #  define signals
    clientConnected = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal()


    def __init__(self, datasource, ip="0.0.0.0", port=5000, parent=None):

        super(QSCSServer, self).__init__(parent)

        self.listening = False
        self.sensors = {}
        self.devices = []
        self.dataTimeout = 30
        self.port = int(port)
        if (ip == "0.0.0.0"):
            self.ip = QtNetwork.QHostAddress(QtNetwork.QHostAddress.LocalHost)
        else:
            self.ip = QtNetwork.QHostAddress(ip)

        self.tcpServer = QtNetwork.QTcpServer(self)
        self.tcpServer.newConnection.connect(self.addConnection)

        self.dataSource = datasource
        self.connect(self.dataSource, QtCore.SIGNAL("SerialDataReceived"), self.receiveDeviceData)


    @QtCore.pyqtSlot(str, list, str)
    def receiveDeviceData(self, device, data, err):
        '''

        '''
        if (not self.listening):
            return

        rxTime = datetime.datetime.now()
        if (device in self.devices):
            for sensor in self.sensors:
                if (self.sensors[sensor]['device'] == device):
                    if (self.sensors[sensor]['prefix'] in data):
                        self.sensors[sensor]['data'] = self.parseSensor(data,
                                self.sensors[sensor]['type'], self.sensors[sensor]['expression'],
                                self.sensors[sensor]['index'])
                        self.sensors[sensor]['time'] = rxTime


    def addNMEASensor(self, name, device, prefix, parseType, parseExpression, parseIndex):
        '''

        name - the sensor name. This is the name published by the server and used
               for requests.
        device - the device name as specified when adding the device to serialMonitor
        prefix - the string that defines the NMEA talker-id prefix. Typically this inculdes
                 the "$", for example "$GPGGA" or "$INGGA" etc. This is used in a literal
                 match to the messages received from the specified device.

        parseType - 'delimited' = parsed by a delimiter
                    'regex' = parsed by regular expression
                    'none' = No parsing (index is ignored)

        parseExpression - If type is delimted, the expression is a string representing
                          the delimiter. If regex it is the regular expression and this
                          argument is ignored for type none.
        parseIndex - a list of indices that represent the parsed elements that are
                     concatenated together to yield the sensor output
        '''

        if (name in self.sensors.keys()):
            return False

        if (not device in self.devices):
            self.devices.append(device)

        self.sensors[name] = {'device':device, 'prefix':prefix,
                'type':parseType, 'expression':parseExpression,
                'index':parseIndex, 'data':None, 'time':None}
        return True


    def parseSensor(self, data, type, expression, index):

        #  parse a sensor value
        try:
            if type.lower() == 'regex':
                #  use regular expression to parse
                pe = re.compile(expression)
                parts = pe.findall(data)
                if (len(index) > 1):
                    data = ''
                    for i in index:
                        data = data + parts[i]
                else:
                    data = parts[index[0]]
            elif type.lower() == 'delimited':
                #  use a delimiter to parse
                parts = data.split(expression)
                if (len(index) > 1):
                    data = ''
                    for i in index:
                        data = data + parts[i]
                else:
                    data = parts[index[0]]
            else:
                # do not parse - pass whole line
                data = data
        except:
            data = None

        return data


    def startServer(self):

        #  create a TCP server
        if (self.tcpServer.listen(self.ip, self.port)):
            self.listening = True
        else:
            self.listening = False
            self.error_string = self.tcpServer.errorString()

        return self.listening


    def addConnection(self):

        clientConnection = self.tcpServer.nextPendingConnection()
        clientConnection.readyRead.connect(self.receiveMessage)
        clientConnection.disconnected.connect(self.removeConnection)
        clientConnection.error.connect(self.socketError)

        #  send the SCS "Hello" - The MACE acquistion.scs client only needs
        #  to receive the text "SCS" to consider itself connected
        self.writeDatagram(clientConnection, "Fake SCS Server v" + str(self.VERSION))


    def receiveMessage(self):

        #  get the client connection
        connection = self.sender()

        if (connection.canReadLine()):
            command = connection.readLine()

            eTree = ETree.XML(command)
            if (len(eTree) > 0):

                if (eTree[0].tag == 'request_command'):
                    command = eTree[0].text[1:].lower()
                    if (command == 'sensordescription'):
                        #  this is a request for the sensor list
                        response = self.createSensorList()
                        self.writeDatagram(connection, response)

                    elif (command == 'get'):
                        #  this is a data request - parse the request for the sensors
                        sensors = []
                        for sensor in eTree[1]:
                            sensors.append(sensor.text)

                        response = self.createGetResponse(sensors)
                        self.writeDatagram(connection, response)

                    else:
                        #  unknown command - ignore
                        pass

                else:
                    #  unknown request - ignore
                    pass


    def writeDatagram(self, client, data):
        '''
        write a \n terminated string to the provided client
        '''

        if (data[-1] != "\n"):
            data = data + "\n"

        block = QtCore.QByteArray()
        out = QtCore.QDataStream(block, QtCore.QIODevice.WriteOnly)
        out.setVersion(QtCore.QDataStream.Qt_4_0)
        out.writeString(data)
        client.write(block)


    def createGetResponse(self, requestedSensors):

        #  get the current time
        requestTime = datetime.datetime.now()

        #  create the base response string
        responseXML = '<?xml version="1.0"?><!DOCTYPE SensorData[]><!--Created by SCS Faker-v' + str(self.VERSION) + '--><SensorList>'

        #  build the response based on the list of sensors
        for sensor in requestedSensors:
            try:
                #  try to get the data for this sensor
                timeDelta = requestTime - self.sensors[sensor]['time']
                if (timeDelta.total_seconds() < self.dataTimeout):
                    data = self.sensors[sensor]['data']
                else:
                    data = ''
            except:
                #  we failed - return an empty string
                data = ''

            #  append this sensor to the sensor list
            responseXML = (responseXML + '<SensorData><sensor_name>' + sensor + '</sensor_name><data_value>' +
                data + '</data_value></SensorData>')

        #  close the sensor list
        responseXML = responseXML + '</SensorList>'

        return responseXML


    def createSensorList(self):

        sensorNumber = 0
        sensorListXML = '<?xml version="1.0"?><!DOCTYPE SensorList[]><!--Created by SCS Faker-v' + str(self.VERSION) + '--><SensorList>'
        for sensor in self.sensors.keys():
            sensorListXML = (sensorListXML + '<Sensor><SensorId>' + str(sensorNumber) + '</SensorId><SensorName>' +
                sensor + '</SensorName></Sensor>')
            sensorNumber = sensorNumber + 1

        sensorListXML = sensorListXML + '</SensorList>'

        return sensorListXML


    def removeConnection(self):
        pass


    def socketError(self):
        pass


