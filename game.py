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

    def verifyChange(self,n=0):
        self.errorList = [] 
        
        if len(self.data[n]['gname']) == 0:
            self.errorList.append("Game name cannot be blank.")
        if len(self.data[n]['gdate']) == 0:
            self.errorList.append("Date cannot be blank.")    
            
            
        
        
        if len(self.errorList) > 0:
            return False
        else:
            return True              
    
    
    
    def getByTeam(self):
        '''
        SELECT *, t.tname AS home, a.tname AS away FROM `teams` t, `teams` a, `games` g 
        WHERE `t`.`tid` = `g`.`team1` AND `a`.`tid` = `g`.`team2`;
        
        '''
        sql = 'SELECT *, t.tname AS home, a.tname AS away FROM `teams` t, `teams` a, `games` g WHERE `t`.`tid` = `g`.`team1` AND `a`.`tid` = `g`.`team2`' #add 
        tokens = ()
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)    
            
            
            
            
#Game Summary Function
    def getSummary(self, gid):
    
        '''
        SELECT *, t.tname as home, a.tname as away 
        FROM `players` p, `games` g, `matchEvents` e, `teams` t, `teams` a 
        WHERE `g`.`gid` = `e`.`gid` AND `g`.`team1` = `t`.`tid` AND `g`.`team2` = `a`.`tid` 
        AND `p`.`pid` = `e`.`pid` AND `g`.`gid` = %s;
        
        SELECT t.tname FROM `teams` t, `players` p WHERE `t`.`tid` = `p`.`tid`;
        
        '''   
        sql = 'SELECT *, t.tname as home, a.tname as away FROM `players` p, `games` g, `matchEvents` e, `teams` t, `teams` a WHERE `g`.`gid` = `e`.`gid` AND `g`.`team1` = `t`.`tid` AND `g`.`team2` = `a`.`tid` AND `p`.`pid` = `e`.`pid` AND `g`.`gid` = %s;' #add 
        
        tokens = (gid)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        