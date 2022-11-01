'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''
from PyQt4.QtCore import *
from PyQt4 import QtSql

class BarcodeDuplicate(QObject):

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

        barcode = currentValue

        query=QtSql.QSqlQuery("SELECT device_id FROM measurements WHERE measurement_type ='barcode' AND measurement_value ='"+barcode+"'")
        if query.first():
            #  weight check failed - weight is outside valid range
            result = (False, 'This barcode number already exists in the database.  Do you want to rescan?')

        else:
            #  weight check succeeded - weight is o.k.
            result = (True, '')

        return result

