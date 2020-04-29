import pymysql
from baseObject import baseObject
class matchEventList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('matchEvents')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        
        if len(self.data[n]['ename']) == 0:
            self.errorList.append("matchEvent name cannot be blank.")
        if len(self.data[n]['estat']) == 0:
            self.errorList.append("Stat cannot be blank.") 
        if len(self.data[n]['etime']) == 0:
            self.errorList.append("Date cannot be blank.")             
            
            
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True    
    
    
    
    
    
    
    
        