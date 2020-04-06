import pymysql
from baseObject import baseObject
class teamList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('teams')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['tname']) == 0:
            self.errorList.append("Team name cannot be blank.")
        if len(self.data[n]['country']) == 0:
            self.errorList.append("Country cannot be blank.")    
        if len(self.data[n]['groupnum']) == 0:
            self.errorList.append("Group cannot be blank.")
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True    
    
    
    
    
    
    
    
        