

class OvaryYesNoDlg():
    def __init__(self,  parent=None):
        pass

    def setup(self, parent):
        self.current_value = parent.values[parent.i]

    def getResponse(self):
        #  change the result
        if self.current_value == 'Yes':
            self.result =   (True, 'No')
        else:
            self.result =   (True, 'Yes')

    def exec_(self):
        self.getResponse()
 


