'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''
from PyQt4.QtCore import *
from PyQt4 import QtSql

class BarcodeNumeric(QObject):

    def __init__(self, db, speciesCode,  subcategory='None'):
        '''
            The init methods of CLAMS validations are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            validation requires should be done here. The two input arguments are:

                db - a reference to the CLAMS QtSQLDatabase object
                speciesCode - the

        '''

        #  call the superclass init
        QObject.__init__(self, None)


    def validate(self,  currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        try:
            int(currentValue)
        except:
            #  barcode failed - not a number
            result = (False, 'The barcode scan was not a number. Please re-scan.')

        else:
            #  barcode is o.k.
            result = (True, '')

        return result

