# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 12:07:55 2014

@author: rick.towler
"""

import logging
from PyQt4 import QtCore
from PyQt4 import QtSql


class SQLError(Exception):

    def __init__(self, query):

        self.QSqlQuery = query
        self.error = self.__stripErrorChars(query.lastError().text().toAscii())
        self.SqlText = str(query.lastQuery())

    def __str__(self):

        return repr(' ::: '.join([self.error, self.SqlText]))

    def __stripErrorChars(self, rawMsg):
        '''
        stripErrorChars is a simple method to extract the readable text from
        error messages returned by QSqlQuery.
        '''
        msg = []
        for s in rawMsg:
            if (s <> '\x00'):
                msg.append(s)
            else:
                break

        return ''.join(msg)


class DBError(Exception):

    def __init__(self, db):

        self.db = db
        self.error = self.__stripErrorChars(db.lastError().text().toAscii())

    def __str__(self):

        return repr(' ::: '.join([ str(self.db.databaseName()), self.error]))

    def __stripErrorChars(self, rawMsg):
        '''
        stripErrorChars is a simple method to extract the readable text from
        error messages returned by QSqlQuery.
        '''
        msg = []
        for s in rawMsg:
            if (s <> '\x00'):
                msg.append(s)
            else:
                break

        return ''.join(msg)


class dbQueryResults:
    '''
    The dbQueryResults class provides an iterator interface for the qSqlQuery
    object. This can be used to provide a more transparent method for iterating
    through results returned by SQL SELECT statements since the column values
    are returned in a list which can be unpacked in a for-in loop. For example:

        sql = ("SELECT device_id, device_name FROM clamsbase2.devices")
        results = self.db.dbQuery(sql)
        for dev_id, dev_name in results:
            print(dev_id)
            print(dev_name)

    Note that ALL values are returned as Python strings.

    The class has the following properties:

        columns     - a list of column names as lower case python strings ordered
                      the same as the data.
        columnTypes - A list of strings describing the data type of the columns.
                      Note that this *is not* the data type of the returned data
                      as all values are returned as strings but the type of the
                      database column.
        nColumns    - An integer denoting the number of columns in the returned
                      result.
        query       - The reference to the qSQLQuery object used to generate the
                      query results.

    '''

    def __init__(self, qSqlQuery, columns, types, dateFormatString=None):

        self.query = qSqlQuery
        self.columns = columns
        self.columnTypes = types
        self.nColumns = len(self.columns)

        if dateFormatString:
            self.dateFormat = dateFormatString
        else:
            self.dateFormat = 'MM/dd/yyyy hh:mm:ss'


    def __iter__(self):
        return self

    def next(self):

        if self.query.next():
            results = []
            #  build the list of items to return
            for i in range(self.nColumns):
                #  handle DateTime conversion explicitly
                if (self.columnTypes[i] == 'DateTime'):
                    val = str(self.query.value(i).toDateTime().toString(self.dateFormat))
                else:
                    val = str(self.query.value(i).toString())
                results.append(val)
            return results
        else:
            raise StopIteration

    def first(self):

        results = []
        if self.query.first():
            #  build the list of items to return
            for i in range(self.nColumns):
                #  handle DateTime conversion explicitly
                if (self.columnTypes[i] == 'DateTime'):
                    val = str(self.query.value(i).toDateTime().toString(self.dateFormat))
                else:
                    val = str(self.query.value(i).toString())
                results.append(val)
        else:
            #  nothing to return as the query is empty
            for i in range(self.nColumns):
                results.append(None)

        return results


    def last(self):

        results = []
        if self.query.last():
            #  build the list of items to return
            for i in range(self.nColumns):
                #  handle DateTime conversion explicitly
                if (self.columnTypes[i] == 'DateTime'):
                    val = str(self.query.value(i).toDateTime().toString(self.dateFormat))
                else:
                    val = str(self.query.value(i).toString())
                results.append(val)
        else:
            #  nothing to return as the query is empty
            for i in range(self.nColumns):
                results.append(None)

        return results


class dbConnection:
    '''
    The dbConnection class is a simple class that encapsulates much of the common
    code we've implemented for SQL interaction in CLAMS and MACEBASE.
    '''

    def __init__(self, source, username, password, label='db'):

        #  create an instance of QSqlDatabase - if None is passed as the label
        #  we'll create the Qt "default" connection.
        if (label == None):
            self.db = QtSql.QSqlDatabase.addDatabase("QODBC")
        else:
            self.db = QtSql.QSqlDatabase.addDatabase("QODBC", label)
        self.db.setDatabaseName(source)
        self.db.setUserName(username)
        self.db.setPassword(password)
        self.label = label
        self.lastError = ''
        self.NLS_DATE_FORMAT = 'MM/DD/YYYY HH24:MI:SS'
        self.NLS_TIMESTAMP_FORMAT = 'MM/DD/YYYY HH24:MI:SS.FF3'
        self.qtDateFormatString = None
        self.loggingEnabled = False
        self.logger = None
        self.handler = None


    def setDateFormat(self, formatString=None, QtFormatString=None):
        '''
        setDateFormat sets the Oracle NLS_DATE_FORMAT variable for the current session.
        The NLS_DATE_FORMAT specifies the format that dates are returned from or inserted
        into the database if the TO_CHAR() or TO_DATE() functions are called without a
        format string. The default format is:

           MM/DD/YYYY HH24:MI:SS

        You should rarely need to change this. IF YOU DO CHANGE THE DATE FORMAT
        YOU REALLY SHOULD CHANGE THE QT FORMAT STRING TO MATCH. If you fail to
        do this, you will either get bogus dates or errors from date conversion
        when using the dbQueryResults class since it converts dates to strings
        automagically. The format expressions are defined here:

        http://qt-project.org/doc/qt-4.8/qdatetime.html#toString
        '''

        #  use the default format string if none provided
        if formatString:
            self.NLS_DATE_FORMAT = formatString

        if QtFormatString:
            self.qtDateFormatString = QtFormatString

        if self.db.isOpen():
            #  set the date and time formats for our connections
            sql = "alter session set NLS_DATE_FORMAT = '" + self.NLS_DATE_FORMAT + "'"
            query = self.db.exec_(sql)
            error = query.lastError().isValid()
            if (error):
                #  there was a problem setting the date format - raise an error message
                self.db.close()
                err = DBError(self.db)
                self.lastError = err.error
                raise err


    def setTimestampFormat(self, formatString=None):
        '''
        setTimestampFormat sets the Oracle NLS_TIMESTAMP_FORMAT variable for the
        current session. The NLS_TIMESTAMP_FORMAT specifies the format that timestamps
        are returned/inserted from the database if the TO_CHAR() or TO_TIMESTAMP()
        functions are called without a format string. The default format is:

           MM/DD/YYYY HH24:MI:SS.FF3

        Since QtSql drops milliseconds from Timestamp columns, you *must* use the
        TO_CHAR() function to convert timestamps to strings on the database side
        to preserve them. You then must use the TO_TIMESTAMP() function when inserting
        these strings into the database.
        '''

        #  use the default format string if none provided
        if formatString:
            self.NLS_TIMESTAMP_FORMAT = formatString

        if self.db.isOpen():
            sql="alter session set NLS_TIMESTAMP_FORMAT='" + self.NLS_TIMESTAMP_FORMAT + "'"
            query = self.db.exec_(sql)
            error = query.lastError().isValid()
            if (error):
                #  there was a problem setting the timestamp format - raise an error message
                self.db.close()
                err = DBError(self.db)
                self.lastError = err.error
                raise err


    def enableLogging(self, logfile):
        '''
        enableLogging creates a log file and logs SQL INSERT, UPDATE, DELETE
        statements to that log file. This is primarily used to log changes to
        the CLAMS database serving as a 3rd line of defense against data loss.

        logfile is the full path to the file you wish to log to.
        '''
        self.logger = logging.getLogger(self.label)
        self.logger.setLevel(logging.INFO)

        self.handler = logging.handlers.FileHandler(logfile)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        self.handler.setFormatter(formatter)

        self.logger.addHandler(self.handler)
        self.loggingEnabled = True


    def disableLogging(self):
        '''
        disableLogging stops logging if it has been enabled.
        '''

        if self.logger:
            self.logger.removeHandler(self.handler)
            self.handler.close()

            self.logger = None
            self.handler = None
            self.loggingEnabled = False


    def dbOpen(self):

        #  do nothing if we're already open
        if self.db.isOpen():
            return

        #  open up database connection
        self.db.open()
        if (self.db.isOpenError()) or (not self.db.isValid()):
            err = DBError(self.db)
            self.lastError = err.error
            raise err

        #  set the Date and Timestamp formats
        self.setDateFormat()
        self.setTimestampFormat()


    def dbClose(self):
        if (self.db.isOpen()):
            self.db.close()
            #QtSql.QSqlDatabase.removeDatabase(self.db.connectionName())
            self.lastError = ''


    def dbQuery(self, sql):

        #  create the structures required for our dbSelectResults class
        columns = []
        types = []

        #  get a QSqlQuery object
        query = self.dbExec(sql)

        #  get a QSqlRecord from the query
        dbRecord = query.record()

        #  if the record is not empty, get the column details
        if (not dbRecord.isEmpty()):
            for i in range(dbRecord.count()):
                columns.append(str(dbRecord.fieldName(i)).lower())
                types.append(self.__getQVariantType(dbRecord.field(i)))

        #  return an instance of our dbSelectResults class
        return dbQueryResults(query, columns, types,
                    dateFormatString=self.qtDateFormatString)


    def dbExec(self, sql):
        '''
        dbExec is a simple wrapper function that checks if your sql statement executed
        successfully and raises an error if it didn't.

        it returns the qSqlQuery object used to execute the passed sql.
        '''

        #  define a query object
        query = QtSql.QSqlQuery(self.db)

        #  execute the sql
        ok = query.exec_(sql)

        #  check if we had a problem
        if (not ok):
            #  ooops, there was a problem - report the error
            raise SQLError(query)

        #  check if we're logging DML changes to the database and log if so
        if self.loggingEnabled:
            #  changes are defined here as INSERT, UPDATE and DELETE DML statements
            if (sql.split(' ')[0].lower() in ['insert', 'update', 'delete']):
                self.logger.info(sql)

        return query


    def __getQVariantType(self, field):

        f= field.type()
        if (f == QtCore.QVariant.Int):
            t = 'Int'
        elif (f == QtCore.QVariant.Double):
            t = 'Double'
        elif (f == QtCore.QVariant.LongLong):
            t = 'LongLong'
        elif (f == QtCore.QVariant.Char):
            t = 'Char'
        elif (f == QtCore.QVariant.Date):
            t = 'Date'
        elif (f == QtCore.QVariant.DateTime):
            t = 'DateTime'
        elif (f == QtCore.QVariant.String):
            t = 'String'
        elif (f == QtCore.QVariant.Time):
            t = 'Time'
        elif (f == QtCore.QVariant.UInt):
            t = 'UInt'
        elif (f == QtCore.QVariant.ULongLong):
            t = 'ULongLong'
        elif (f == QtCore.QVariant.List):
            t = 'List'
        elif (f == QtCore.QVariant.ByteArray):
            t = 'ByteArray'
        else:
            t = 'Unknown'

        return t

