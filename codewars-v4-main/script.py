import random
import math

name = "script"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )
    
def checkIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False

island_c=[0,0,0,0,0,0]

def ActPirate(pirate):
    n= pirate.investigate_up()[0]
    s = pirate.investigate_down()[0]
    w = pirate.investigate_left()[0]
    e = pirate.investigate_right()[0]
    ne= pirate.investigate_ne()[0]
    se= pirate.investigate_se()[0]
    nw= pirate.investigate_nw()[0]
    sw= pirate.investigate_sw()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    st = pirate.trackPlayers()
    sig=""
    global island_c
    
    if (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
        and
        ((se=='blank'))
    ):
        sig=e[-1]+str(x+2)+","+str(y-1)
        pirate.setTeamSignal(sig) 
        island_c[int(e[-1])*2-2]=x+2
        island_c[int(e[-1])*2-1]=y-1
        
    elif (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
        and
        ((ne=='blank'))
    ):
        sig=e[-1]+str(x+2)+","+str(y+1)
        pirate.setTeamSignal(sig)
        island_c[int(e[-1])*2-2]=x+2
        island_c[int(e[-1])*2-1]=y+1
        
    elif (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
    ):
        sig=e[-1]+str(x+2)+","+str(y)
        pirate.setTeamSignal(sig)
        island_c[int(e[-1])*2-2]=x+2
        island_c[int(e[-1])*2-1]=y
        
    elif (
        ((se == "island1" and st[0] != "myCaptured")
        or (se == "island2" and st[1] != "myCaptured")
        or (se == "island3" and st[2] != "myCaptured"))
    ):
        sig=se[-1]+str(x+2)+","+str(y+2)
        pirate.setTeamSignal(sig)
        island_c[int(se[-1])*2-2]=x+2
        island_c[int(se[-1])*2-1]=y+2
        
    elif (
        ((ne == "island1" and st[0] != "myCaptured")
        or (ne == "island2" and st[1] != "myCaptured")
        or (ne == "island3" and st[2] != "myCaptured"))
    ):
        sig=ne[-1]+str(x+2)+","+str(y-2)
        pirate.setTeamSignal(sig)
        island_c[int(ne[-1])*2-2]=x+2
        island_c[int(ne[-1])*2-1]=y-2
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
        and
        nw=="blank"
    ):
        sig=w[-1]+str(x-2)+","+str(y+1)
        pirate.setTeamSignal(sig)
        island_c[int(w[-1])*2-2]=x-2
        island_c[int(w[-1])*2-1]=y+1
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
        and
        sw=="blank"
    ):
        sig=w[-1]+str(x-2)+","+str(y-1)
        pirate.setTeamSignal(sig)
        island_c[int(w[-1])*2-2]=x-2
        island_c[int(w[-1])*2-1]=y-1
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
    ):
        sig=w[-1]+str(x-2)+","+str(y)
        pirate.setTeamSignal(sig)
        island_c[int(w[-1])*2-2]=x-2
        island_c[int(w[-1])*2-1]=y
        
    elif(
         ((sw == "island1" and st[0] != "myCaptured")
        or (sw == "island2" and st[1] != "myCaptured")
        or (sw == "island3" and st[2] != "myCaptured"))
    ):
        sig=sw[-1]+str(x-2)+","+str(y+2)
        pirate.setTeamSignal(sig)
        island_c[int(sw[-1])*2-2]=x-2
        island_c[int(sw[-1])*2-1]=y+2
        
    elif(
        ((nw == "island1" and st[0] != "myCaptured")
        or (nw == "island2" and st[1] != "myCaptured")
        or (nw == "island3" and st[2] != "myCaptured"))
    ):
        sig=nw[-1]+str(x-2)+","+str(y-2)
        pirate.setTeamSignal(sig)
        island_c[int(nw[-1])*2-2]=x-2
        island_c[int(nw[-1])*2-1]=y-2
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
        and
        sw=="blank"
    ):
        sig=s[-1]+str(x+1)+","+str(y+2)
        pirate.setTeamSignal(sig)
        island_c[int(s[-1])*2-2]=x+1
        island_c[int(s[-1])*2-1]=y+2
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
        and
        se=="blank"
    ):
        sig=s[-1]+str(x-1)+","+str(y+2)
        pirate.setTeamSignal(sig)
        island_c[int(s[-1])*2-2]=x-1
        island_c[int(s[-1])*2-1]=y+2
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
    ):
        sig=s[-1]+str(x)+","+str(y+2)
        pirate.setTeamSignal(sig)
        island_c[int(s[-1])*2-2]=x
        island_c[int(s[-1])*2-1]=y+2
             
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
        and
        nw=="blank"
    ):
        sig=n[-1]+str(x+1)+","+str(y-2)
        pirate.setTeamSignal(sig)
        island_c[int(n[-1])*2-2]=x+1
        island_c[int(n[-1])*2-1]=y-2
       
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
        and
        ne=="blank"
    ):
        sig=n[-1]+str(x-1)+","+str(y-2)
        pirate.setTeamSignal(sig)
        island_c[int(n[-1])*2-2]=x-1
        island_c[int(n[-1])*2-1]=y-2
        
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
    ):
        sig=n[-1]+str(x)+","+str(y-2)
        pirate.setTeamSignal(sig)
        island_c[int(n[-1])*2-2]=x
        island_c[int(n[-1])*2-1]=y-2
        
    else: 
        pass   
    
    
    if pirate.getTeamSignal() != "":
        sig = pirate.getTeamSignal()
        l = sig.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return random.randint(1, 4)

    pass


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)   
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")

    pass
