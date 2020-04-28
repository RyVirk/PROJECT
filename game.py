import pymysql
from baseObject import baseObject
class gameList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('games')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['gname']) == 0:
            self.errorList.append("Game name cannot be blank.")
        if len(self.data[n]['gdate']) == 0:
            self.errorList.append("Date cannot be blank.")    
            
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True    
    
    
    
    
    
    
    
        