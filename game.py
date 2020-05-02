import pymysql
from baseObject import baseObject
class gameList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('games')
        
    def verifyNew(self,n=0):
        self.errorList = []
        '''
        team1= self.data[n]['team1']
        team2= self.data[n]['team2']        
        t = teamList()
        t.getByID(tid)
        team1 = t.data[0]['tname']
        
        t2 = teamList2()
        t2.getByID(tid)
        team2 = t2.data[0]['tname']
        '''
        
        
        
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
    
    
    
        