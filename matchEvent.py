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

    def verifyChange(self,n=0):
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
    
    
    def getByTeam(self):
        '''
        SELECT * 
        FROM `teams` t, `matchEvents` e 
        WHERE `t`.`tid` = `e`.`tid`;
        '''

        sql = 'SELECT * FROM `teams` t, `matchEvents` e, `players` p, `games` g WHERE `t`.`tid` = `e`.`tid` AND `p`.`pid` = `e`.`pid` AND `g`.`gid` = `e`.`gid`;' #add 
        tokens = ()
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)

            
'''
    def getByPlayer(self):
        
        SELECT * FROM `players` p, `matchEvents` e 
        WHERE `p`.`pid` = `e`.`pid`;
        
        
        sql = 'SELECT * FROM `players` p, `matchEvents` e WHERE `p`.`pid` = `e`.`pid`;' #add 
        tokens = ()
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)                
'''    
    
    
    
    
    
        