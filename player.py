import pymysql
from baseObject import baseObject
class playerList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('players')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['pname']) == 0:
            self.errorList.append("Player name cannot be blank.")
        if len(self.data[n]['age']) == 0:
            self.errorList.append("Age cannot be blank.")    
        if len(self.data[n]['position']) == 0:
            self.errorList.append("Position cannot be blank.")
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True    
            
            
    
    
    
    
    
    
    
        