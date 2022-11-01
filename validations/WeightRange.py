'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''
from PyQt4.QtCore import *
from PyQt4 import QtSql

class WeightRange(QObject):

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

        #  Get the valid weight range for this species from the species table
        query=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+" AND subcategory='"+subcategory+"' AND lower(species_parameter)='min_weight'", db)
        if query.first():
            self.minWeight=float(query.value(0).toString())
        else:
            self.minWeight=0
        query=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE species_code="+speciesCode+" AND subcategory='"+subcategory+"' AND lower(species_parameter)='max_weight'", db)
        if query.first():
            self.maxWeight=float(query.value(0).toString())
        else:
            self.maxWeight=999



    def validate(self,  currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        thisWeight = float(currentValue)

        if (thisWeight < self.minWeight) or (thisWeight > self.maxWeight):
            #  weight check failed - weight is outside valid range
            result = (False, 'The weight is out of range for this species. Do you want to re-enter weight?')

        else:
            #  weight check succeeded - weight is o.k.
            result = (True, '')

        return result

