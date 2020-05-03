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
        if len(self.data[n]['groupnum']) == 0 or len(self.data[n]['groupnum']) > 1:
            self.errorList.append("Group cannot be blank or greater than one number.")
        #if(self.data[n]['groupnum'])     
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True   
            
            
    def verifyChange(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['tname']) == 0:
            self.errorList.append("Team name cannot be blank.")
        if len(self.data[n]['country']) == 0:
            self.errorList.append("Country cannot be blank.")    
        if len(self.data[n]['groupnum']) == 0 or len(self.data[n]['groupnum']) > 1:
            self.errorList.append("Group cannot be blank or greater than one number.")
        #if(self.data[n]['groupnum'])     
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True             

    def getOrder(self):
        sql = 'SELECT * FROM teams ORDER BY groupnum;'
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql)
        self.data = []
        for row in cur:
            self.data.append(row)            
    
    
    
    
    
    
    
        