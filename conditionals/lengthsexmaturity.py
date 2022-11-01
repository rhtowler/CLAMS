'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''

from PyQt4.QtCore import *
from PyQt4 import QtSql

class LengthSexMaturity(QObject):

    def __init__(self, db):
        '''
            The init methods of CLAMS conditionals are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            validation requires should be done here. The two input arguments are:

                db - a reference to the CLAMS QtSQLDatabase object
                speciesCode - the

        '''
        #  call the superclass init
        QObject.__init__(self, None)

        #  Get the valid weight range for this species from the species table
        query = QtSql.QSqlQuery("SELECT parameter_value FROM application_configuration WHERE "+
                "parameter='Age1Definition'", db)

        #  extract returned results
        query.first()
        self.age1Length=float(query.value(0).toString())

    def evaluate(self,   measurements,  values,  result):
        '''
            The evaluate method is called when measuremets are taken to see what changes in the protocol
        '''

        # figure out the rule
        if values[measurements.index('length')]<>None:
            length=float(values[measurements.index('length')])
            if length<=self.age1Length:# this is an age 1 fish
                try:
                    result[measurements.index('sex')]=False
                    result[measurements.index('maturity')]=False
                    result[measurements.index('gonad_weight')]=False
                except:
                    pass


        return result

