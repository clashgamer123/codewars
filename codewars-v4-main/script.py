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
island_order=[]
i=0
deploy_p=[20,20]
j=0
k=0
pirate_divider_1=0
pirate_divider_2=0
island_pirates_1=[]
island_pirates_2=[]

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
    global deploy_p
    global i
    global j,k
    global pirate_divider_1
    global pirate_divider_2
    global island_pirates_1
    global island_pirates_2
    global island_order
    
    def verify(list_pirates,pirate):
        if pirate.getID() not in list_pirates: return False
        else: return True
    
    if i==1 :
        deploy_p=[x,y]
    else: pass
    
    
    if (
        ((e == "island1" and st[0] != "myCaptured") 
        or (e == "island2" and st[1] != "myCaptured") 
        or (e == "island3" and st[2] != "myCaptured"))
        and
        ((se=='blank'))
    ):
        if (j==0): 
            j=i
        sig=e[-1]
        pirate.setTeamSignal(sig)
        island_c[int(e[-1])*2-2]=x+2
        island_c[int(e[-1])*2-1]=y-1 
        if int(e[-1]) not in island_order:
            island_order.append(int(e[-1])) 
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
        and
        ((ne=='blank'))
    ):
        if (j==0):
            j=i
        sig=e[-1]
        pirate.setTeamSignal(sig)
        island_c[int(e[-1])*2-2]=x+2
        island_c[int(e[-1])*2-1]=y+1
        if int(e[-1]) not in island_order:
            island_order.append(int(e[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=e[-1]
        pirate.setTeamSignal(sig)
        island_c[int(e[-1])*2-2]=x+2
        island_c[int(e[-1])*2-1]=y
        if int(e[-1]) not in island_order:
            island_order.append(int(e[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((se == "island1" and st[0] != "myCaptured")
        or (se == "island2" and st[1] != "myCaptured")
        or (se == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=se[-1]
        pirate.setTeamSignal(sig)
        island_c[int(se[-1])*2-2]=x+2
        island_c[int(se[-1])*2-1]=y+2
        if int(se[-1]) not in island_order:
            island_order.append(int(se[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((ne == "island1" and st[0] != "myCaptured")
        or (ne == "island2" and st[1] != "myCaptured")
        or (ne == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=ne[-1]
        pirate.setTeamSignal(sig)
        island_c[int(ne[-1])*2-2]=x+2
        island_c[int(ne[-1])*2-1]=y-2
        if int(ne[-1]) not in island_order:
            island_order.append(int(ne[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
        and
        nw=="blank"
    ):
        if (j==0): 
            j=i
        sig=w[-1]
        pirate.setTeamSignal(sig)
        island_c[int(w[-1])*2-2]=x-2
        island_c[int(w[-1])*2-1]=y+1
        if int(w[-1]) not in island_order:
            island_order.append(int(w[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
        and
        sw=="blank"
    ):
        if (j==0): 
            j=i
        sig=w[-1]
        pirate.setTeamSignal(sig)
        island_c[int(w[-1])*2-2]=x-2
        island_c[int(w[-1])*2-1]=y-1
        if int(w[-1]) not in island_order:
            island_order.append(int(w[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=w[-1]
        pirate.setTeamSignal(sig)
        island_c[int(w[-1])*2-2]=x-2
        island_c[int(w[-1])*2-1]=y
        if int(w[-1]) not in island_order:
            island_order.append(int(w[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif(
         ((sw == "island1" and st[0] != "myCaptured")
        or (sw == "island2" and st[1] != "myCaptured")
        or (sw == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=sw[-1]
        pirate.setTeamSignal(sig)
        island_c[int(sw[-1])*2-2]=x-2
        island_c[int(sw[-1])*2-1]=y+2
        if int(sw[-1]) not in island_order:
            island_order.append(int(sw[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif(
        ((nw == "island1" and st[0] != "myCaptured")
        or (nw == "island2" and st[1] != "myCaptured")
        or (nw == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=nw[-1]
        pirate.setTeamSignal(sig)
        island_c[int(nw[-1])*2-2]=x-2
        island_c[int(nw[-1])*2-1]=y-2
        if int(nw[-1]) not in island_order:
            island_order.append(int(nw[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
        and
        sw=="blank"
    ):
        if (j==0): 
            j=i
        sig=s[-1]
        pirate.setTeamSignal(sig)
        island_c[int(s[-1])*2-2]=x+1
        island_c[int(s[-1])*2-1]=y+2
        if int(s[-1]) not in island_order:
            island_order.append(int(s[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
        and
        se=="blank"
    ):
        if (j==0): 
            j=i
        sig=s[-1]
        pirate.setTeamSignal(sig)
        island_c[int(s[-1])*2-2]=x-1
        island_c[int(s[-1])*2-1]=y+2
        if int(s[-1]) not in island_order:
            island_order.append(int(s[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=s[-1]
        pirate.setTeamSignal(sig)
        island_c[int(s[-1])*2-2]=x
        island_c[int(s[-1])*2-1]=y+2
        if int(s[-1]) not in island_order:
            island_order.append(int(s[-1]))
        if len(island_order)==2 and k==0: k=i
             
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
        and
        nw=="blank"
    ):
        if (j==0): 
            j=i
        sig=n[-1]
        pirate.setTeamSignal(sig)
        island_c[int(n[-1])*2-2]=x+1
        island_c[int(n[-1])*2-1]=y-2
        if int(n[-1]) not in island_order:
            island_order.append(int(n[-1]))
        if len(island_order)==2 and k==0: k=i
       
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
        and
        ne=="blank"
    ):
        if (j==0): 
            j=i
        sig=n[-1]
        pirate.setTeamSignal(sig)
        island_c[int(n[-1])*2-2]=x-1
        island_c[int(n[-1])*2-1]=y-2
        if int(n[-1]) not in island_order:
            island_order.append(int(n[-1]))
        if len(island_order)==2 and k==0: k=i
        
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
    ):
        if (j==0): 
            j=i
        sig=n[-1]
        pirate.setTeamSignal(sig)
        island_c[int(n[-1])*2-2]=x
        island_c[int(n[-1])*2-1]=y-2
        if int(n[-1]) not in island_order:
            island_order.append(int(n[-1]))
        if len(island_order)==2 and k==0: k=i
        
    else: 
        pass 

    if len(island_order)==0:
        return moveAway(deploy_p[0],deploy_p[1],pirate)
    
    elif len(island_order)==1:
        m=island_order[0]
        if(i<j+10):
            if sig!="":
                if not(verify(island_pirates_1,pirate)):
                    island_pirates_1.append(pirate.getID())
            return moveTo(island_c[2*m-2],island_c[2*m-1],pirate)
        elif i>j+10:
            if verify(island_pirates_1,pirate) and st[m-1]!="myCaptured" :
                return moveTo(island_c[2*m-2],island_c[2*m-1],pirate)
            else:
                pirate_divider_1+=1
                if (pirate_divider_1%2==0) :
                    return moveAway(island_c[2*m-2],island_c[2*m-1],pirate)
                else:
                    return moveAway(deploy_p[0],deploy_p[1],pirate)
                
    elif len(island_order)==2 :
        m=island_order[1]
        if verify(island_pirates_1,pirate):
            if st[island_order[0]-1]!="myCaptured":
                return 0
            else:
                pass
        else:
            if i<=k+20:
                if sig==f"{m}":
                    if not(verify(island_pirates_2,pirate)) :
                        island_pirates_2.append(pirate.getID())
                return moveTo(island_c[2*m-2],island_c[2*m-1],pirate)
            
            elif i>k+20:
                if verify(island_pirates_2,pirate) and st[m-1]!="myCaptured":
                    return moveTo(island_c[2*m-2],island_c[2*m-1],pirate)
                else:
                    pirate_divider_2+=1
                    if pirate_divider_2%2==0:
                        return moveAway((island_c[island_order[0]*2-2]),(island_c[2*island_order[0]-1]),pirate)
                    else:
                        return moveAway(island_c[2*m-2],island_c[2*m-1],pirate)
    
    elif len(island_order)==3:
        m=island_order[2]
        if verify(island_pirates_1,pirate) :
            if st[island_order[0]-1]!="myCaptured":
                return 0
            else: pass    
        elif verify(island_pirates_2,pirate) : 
            if st[island_order[1]-1]!="myCaptured":
                return 0
            else : pass
        else:
            if st[m-1]!="myCaptured":
                moveTo(island_c[2*m-2],island_c[2*m-1],pirate)
            else :
                return random.randint(1,4)
            
    pass


def ActTeam(team):
    global dimX,dimY
    dimX=team.getDimensionX()
    dimY=team.getDimensionY()
    l = team.trackPlayers()
    s = team.getTeamSignal()
    
    global i
    i+=1
    
    team.buildWalls(1)
    team.buildWalls(2)   
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    team.setTeamSignal("")
    pass
