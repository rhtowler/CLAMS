'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''

from PyQt4.QtCore import *
from PyQt4 import QtSql

class TakingOvaryRockfish(QObject):

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


    def evaluate(self,   measurements,  values,  result):
        '''
            The evaluate method is called when measuremets are taken to see what changes in the protocol
        '''

        # figure out the rule
        if values[measurements.index('sex')]<>None:
            sex=str(values[measurements.index('sex')])
            if (sex.lower() == 'male'):
                try:
                    result[measurements.index('ovary_taken')]=False
                    result[measurements.index('barcode')]=False
                except:
                    pass


        return result

