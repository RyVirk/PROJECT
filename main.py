from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 

from customer import customerList
from team import teamList
from game import gameList
from player import playerList
from matchEvent import matchEventList

import pymysql 
import json
import time

from flask_session import Session  #serverside sessions

app = Flask(__name__,static_url_path='')
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/set')
def set():
    session['time'] = time.time()
    return 'set'

@app.route('/get')
def get():
    return str(session['time'])
    
@app.route('/login',methods = ['GET','POST'])
def login():
    '''
    -check login
    -set session
    -redirect menu
    --check session on login page
    '''    
    if request.form.get('email') is not None and request.form.get('password') is not None:
        c = customerList()
        if c.tryLogin(request.form.get('email'),request.form.get('password')):
            print('login ok')
            session['user'] = c.data[0]
            session['active'] = time.time()
            
            return redirect('main')
        else:
            print('login failed')
            return render_template('login.html', title='Login', msg='Incorrect username or password')     
    else:
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your email and password to continue.'
        else: 
            m = session['msg']
            session['msg'] = None    
        return render_template('login.html', title='Login', msg=m)    

@app.route('/logout',methods = ['GET','POST'])
def logout():
    del session['user']
    del session['active'] 
    return render_template('login.html', title='Login', msg='You have logged out.') 

@app.route('/basichttp')
def basichttp():
    if request.args.get('myvar') is not None:
        return 'your var:' + request.args.get('myvar')
    else:
        return 'myvar not set' 

@app.route('/')
def home():
    return render_template('test.html', title='Test', msg='Welcome!')

@app.route('/index')
def index():
    user = {'username': 'Tyler'}
        
    
    items = [
        {'name':'Apple','price':2.34},
        {'name':'Orange','price':4.88},
        {'name':'Grape','price':2.44}
    ]
    return render_template('index.html', title='Home', user=user, items=items)

@app.route('/customers')
def customers():
    c = customerList()
    c.getAll()
    
    print(c.data)
    #return ''
    return render_template('customers.html', title='Customer List', customers=c.data)


@app.route('/customer')
def customer():
    c = customerList()
    if request.args.get(c.pk) is None:
       return render_template('error.html', msg='No customer id given')

    
    c.getById(request.args.get(c.pk))
    if len(c.data) <= 0:
        return render_template('error.html', msg='Customer not found')
            
    
    print(c.data)
    #return ''
    return render_template('customer.html', title='Customer', customer=c.data[0])

@app.route('/newcustomer',methods = ['GET','POST'])
def newcustomer():
    if request.form.get('fname') is None:
        c = customerList()
        c.set('fname','')
        c.set('lname','')
        c.set('email','')
        c.set('password','')
        c.set('subscribed','')
        c.add()      
        return render_template('newcustomer.html', title='New Customer', customer=c.data[0]) 
    else:
        c = customerList()
        c.set('fname',request.form.get('fname'))
        c.set('lname',request.form.get('lname'))
        c.set('email',request.form.get('email'))
        c.set('password',request.form.get('password'))
        c.set('subscribed',request.form.get('subscribed'))
        c.add()  
        if c.verifyNew():     
            c.insert()
            print(c.data)
            return render_template('savedcustomer.html', title='Customer Saved', 
            customer=c.data[0])
        else:    
            return render_template('newcustomer.html', title='Customer Not Saved', 
            customer=c.data[0],msg=c.errorList)
        
@app.route('/savecustomer',methods = ['GET','POST'])
def savecustomer():
        c = customerList()
        c.set('id',request.form.get('id'))
        c.set('fname',request.form.get('fname'))
        c.set('lname',request.form.get('lname'))
        c.set('email',request.form.get('email'))
        c.set('password',request.form.get('password'))
        c.set('subscribed',request.form.get('subscribed'))
        c.add()  
        c.update()
        print(c.data)
        #return ''
        return render_template('savedcustomer.html', title='Customer Saved', customer=c.data[0])        

'''
=======================================
START TEAM PAGES:
=======================================
'''
@app.route('/teams')
def teams():
    t = teamList()
    t.getAll()
    t.getOrder()
    
    #print(t.data)
    #return ''
    return render_template('team/teams.html', title='Team List', teams=t.data)


@app.route('/team')
def team():
    t = teamList()
    if request.args.get(t.pk) is None:
       return render_template('error.html', msg='No team id given')

    
    t.getById(request.args.get(t.pk))
    if len(t.data) <= 0:
        return render_template('error.html', msg='Team not found')
            
    
    print(t.data)
    #return ''
    return render_template('team/team.html', title='Team ', team=t.data[0])

@app.route('/newteam',methods = ['GET','POST'])
def newteam():
    if request.form.get('tname') is None:
        t = teamList()
        t.set('tname','')
        t.set('country','')
        t.set('groupnum','')
        t.add()      
        return render_template('team/newteam.html', title='New Team', team=t.data[0]) 
    else:
        t = teamList()
        t.set('tname',request.form.get('tname'))
        t.set('country',request.form.get('country'))
        t.set('groupnum',request.form.get('groupnum'))
        t.add()  
        if t.verifyNew():     
            t.insert()
            print(t.data)
            return render_template('team/savedteam.html', title='Team Saved', 
            team=t.data[0])
        else:    
            return render_template('team/newteam.html', title='Team Not Saved', 
            team=t.data[0],msg=t.errorList)
        
@app.route('/saveteam',methods = ['GET','POST'])
def saveteam():
        t = teamList()
        t.set('tid',request.form.get('tid'))
        t.set('tname',request.form.get('tname'))
        t.set('country',request.form.get('country'))
        t.set('groupnum',request.form.get('groupnum'))
        t.add()  
        t.update()
        print(t.data)
        #return ''
        return render_template('team/savedteam.html', title='Team Saved', team=t.data[0])        
'''
=======================================
END TEAM PAGES:
=======================================
'''


'''
=======================================
START GAME PAGES:
=======================================
'''
@app.route('/games')
def games():
    g = gameList()
    g.getAll()
    g.getByTeam()

    
    print(g.data)
    #return ''
    return render_template('game/games.html', title='Game List', games=g.data)

@app.route('/game')
def game():
    g = gameList()
    allTeams = teamList()
    allTeams.getAll()    
    if request.args.get(g.pk) is None:
       return render_template('error.html', msg='No game id given')

    
    g.getById(request.args.get(g.pk))
    if len(g.data) <= 0:
        return render_template('error.html', msg='Game not found')
            
    
    print(g.data)
    #return ''
    return render_template('game/game.html', title='Game', game=g.data[0], tl= allTeams.data)

@app.route('/newgame',methods = ['GET','POST'])
def newgame():
    if request.form.get('gname') is None:
        g = gameList()
        g.set('gname','')
        g.set('gdate','')
        g.set('team1','')
        g.set('team2','')
        g.add()   
        allTeams = teamList()
        allTeams.getAll()        
        return render_template('game/newgame.html', title='New Game', game=g.data[0], tl= allTeams.data) 
    else:
        g = gameList()
        g.set('gname',request.form.get('gname'))
        g.set('gdate',request.form.get('gdate'))
        g.set('team1',request.form.get('team1'))
        g.set('team2',request.form.get('team2'))
        g.add()  
        if g.verifyNew():     
            g.insert()
            print(g.data)
            return render_template('game/savedgame.html', title='Game Saved', 
            game=g.data[0])
        else:    
            return render_template('game/newgame.html', title='Game Not Saved', 
            game=g.data[0],msg=g.errorList)
        
@app.route('/savegame',methods = ['GET','POST'])
def savegame():
        g = gameList()
        g.set('gid',request.form.get('gid'))
        g.set('gname',request.form.get('gname'))
        g.set('gdate',request.form.get('gdate'))
        g.set('team1',request.form.get('team1'))
        g.set('team2',request.form.get('team2'))
        g.add()  
        g.update()
        print(g.data)
        #return ''
        return render_template('game/savedgame.html', title='Game Saved', game=g.data[0])      
'''
=======================================
END GAME PAGES:
=======================================
'''



'''
=======================================
START PLAYER PAGES:
=======================================
'''
@app.route('/players')
def players():
    p = playerList()
    p.getAll()
    p.getByTeam()
    
    print(p.data)
    #return ''
    return render_template('player/players.html', title='Player List', players=p.data)


@app.route('/player')
def player():
    p = playerList()
    allTeams = teamList()
    allTeams.getAll()   
    if request.args.get(p.pk) is None:
       return render_template('error.html', msg='No player id given')

    
    p.getById(request.args.get(p.pk))
    if len(p.data) <= 0:
        return render_template('error.html', msg='Player not found')
            
   
    print(p.data)
    #return ''
    return render_template('player/player.html', title='Player', player=p.data[0],tl= allTeams.data)

@app.route('/newplayer',methods = ['GET','POST'])
def newplayer():
    if request.form.get('pname') is None:
        p = playerList()
        p.set('pname','')
        p.set('age','')
        p.set('position','')
        p.set('tid','')
        p.add()
        allTeams = teamList()
        allTeams.getAll()
            
        return render_template('player/newplayer.html', title='New Player', player=p.data[0],
        tl= allTeams.data) 
    else:
        p = playerList()
        p.set('pname',request.form.get('pname'))
        p.set('age',request.form.get('age'))
        p.set('position',request.form.get('position'))
        p.set('tid',request.form.get('tid')) #possible problem with naming
        p.add()  
        if p.verifyNew():     
            p.insert()
            print(p.data)
            return render_template('player/savedplayer.html', title='Player Saved', 
            player=p.data[0])
        else:    
            return render_template('player/newplayer.html', title='Player Not Saved', 
            player=p.data[0],msg=p.errorList)
        
@app.route('/saveplayer',methods = ['GET','POST'])
def saveplayer():
        p = playerList()
        p.set('pid',request.form.get('pid'))
        p.set('pname',request.form.get('pname'))
        p.set('age',request.form.get('age'))
        p.set('position',request.form.get('position'))
        p.set('tid',request.form.get('tid'))
        p.add()  
        p.update()
        print(p.data)
        #return ''
        return render_template('player/savedplayer.html', title='Player Saved', player=p.data[0])      
'''
=======================================
END PLAYER PAGES:
=======================================
'''


'''
=======================================
START matchEvent PAGES:
=======================================
'''
@app.route('/matchEvents')
def matchEvents():
    e = matchEventList()
    e.getAll()
    e.getByTeam()
    
    print(e.data)
    #return ''
    return render_template('matchEvent/matchEvents.html', title='matchEvent List', matchEvents=e.data)


@app.route('/matchEvent')
def matchEvent():
    e = matchEventList()
    
    allPlayers = playerList()
    allPlayers.getByTeam() 
    
    allGames = gameList()
    allGames.getByTeam() 
    
    allTeams = teamList()
    allTeams.getAll()     
    
    if request.args.get(e.pk) is None:
       return render_template('error.html', msg='No matchEvent id given')

    
    e.getById(request.args.get(e.pk))
    if len(e.data) <= 0:
        return render_template('error.html', msg='matchEvent not found')
            
    
    print(e.data)
    #return ''
    return render_template('matchEvent/matchEvent.html', title='matchEvent', matchEvent=e.data[0],
    pl= allPlayers.data, gl= allGames.data, tl= allTeams.data)

@app.route('/newMatchEvent',methods = ['GET','POST'])
def newMatchEvent():
    if request.form.get('ename') is None:
        e = matchEventList()
        e.set('ename','')
        e.set('estat','')
        e.set('etime','')
        e.set('pid','')
        e.set('gid','')
        e.set('tid','')
        e.set('id','')        
        e.add()

        allPlayers = playerList()
        allPlayers.getByTeam() 
        
        allGames = gameList()
        allGames.getByTeam() 
        
        allTeams = teamList()
        allTeams.getAll() 
    
        return render_template('matchEvent/newMatchEvent.html', title='New matchEvent', matchEvent=e.data[0],
        pl= allPlayers.data, gl= allGames.data, tl= allTeams.data) 
    else:
        e = matchEventList()
        e.set('ename',request.form.get('ename'))
        e.set('estat',request.form.get('estat'))
        e.set('etime',request.form.get('etime'))
        e.set('pid',request.form.get('pid')) #possible problem with naming
        e.set('gid',request.form.get('gid'))
        e.set('tid',request.form.get('tid'))
        e.set('id',request.form.get('id'))        
        e.add()  
        if e.verifyNew():     
            e.insert()
            print(e.data)
            return render_template('matchEvent/savedMatchEvent.html', title='matchEvent Saved', 
            matchEvent=e.data[0])
        else:    
            return render_template('matchEvent/newMatchEvent.html', title='matchEvent Not Saved', 
            matchEvent=e.data[0],msg=e.errorList)
        
@app.route('/saveMatchEvent',methods = ['GET','POST'])
def saveMatchEvent():
        e = matchEventList()
        e.set('eid',request.form.get('eid'))
        e.set('ename',request.form.get('ename'))
        e.set('estat',request.form.get('estat'))
        e.set('etime',request.form.get('etime'))
        e.set('pid',request.form.get('pid'))
        e.set('gid',request.form.get('gid'))
        e.set('tid',request.form.get('tid'))
        e.set('id',request.form.get('id'))        
        e.add()  
        e.update()
        print(e.data)
        #return ''
        return render_template('matchEvent/savedMatchEvent.html', title='matchEvent Saved', matchEvent=e.data[0])      
'''
=======================================
END matchEvent PAGES:
=======================================
'''



@app.route('/main')
def main():
    if checkSession() == False: #check to make sure the user is logged in
        return redirect('login')
    userinfo = 'Hello, ' + session['user']['fname']
    return render_template('main.html', title='Main Menu',msg = userinfo)
    
def checkSession():
    if 'active' in session.keys():    
        timeSinceActivity = time.time() - session['active']
        print(timeSinceActivity)
        if timeSinceActivity > 500:
            session['msg'] = 'Your session has timed out.'
            return False
        else:    
            session['active'] = time.time()
            return True
    else:
        return False

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.secret_key = '1234'
   app.run(host='127.0.0.1',debug=True)