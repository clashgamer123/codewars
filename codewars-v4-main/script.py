
import random
import math
name="Cobra"
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

def ActPirate(pirate):
    n= pirate.investigate_up()[0]
    s = pirate.investigate_down()[0]
    w = pirate.investigate_left()[0]
    e = pirate.investigate_right()[0]
    ne= pirate.investigate_ne()[0]
    se= pirate.investigate_se()[0]
    nw= pirate.investigate_nw()[0]
    sw= pirate.investigate_sw()[0]
    p,q=pirate.getDeployPoint()
    x,y = pirate.getPosition()
    a=pirate.getDimensionX()
    b=pirate.getDimensionY()
    signal=pirate.getTeamSignal()
    st=pirate.trackPlayers()

    if signal != "":
        k = signal.split(",")
        if len(k)==5:
            z = [k[1],k[2],k[3],k[4],"0","0","0","0","0","0","0","0"]
        elif len(k)==9:
            z = [k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],"0","0","0","0"]
        elif len(k)==13:
            z= [k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],k[9],k[10],k[11],k[12]]
        else:
            z = ["0","0","0","0","0","0","0","0","0","0","0","0"]
    else:
        z = ["0","0","0","0","0","0","0","0","0","0","0","0"]
    
    if (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
        and
        ((se=='blank'))
    ):
        sig=e[-1]+","+str(x+2)+","+str(y-1)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
        and
        ((ne=='blank'))
    ):
        sig=e[-1]+","+str(x+2)+","+str(y+1)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
                
    elif (
        ((e == "island1" and st[0] != "myCaptured")
        or (e == "island2" and st[1] != "myCaptured")
        or (e == "island3" and st[2] != "myCaptured"))
    ):
        sig=e[-1]+","+str(x+2)+","+str(y)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif (
        ((se == "island1" and st[0] != "myCaptured")
        or (se == "island2" and st[1] != "myCaptured")
        or (se == "island3" and st[2] != "myCaptured"))
    ):
        sig=se[-1]+","+str(x+2)+","+str(y+2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif (
        ((ne == "island1" and st[0] != "myCaptured")
        or (ne == "island2" and st[1] != "myCaptured")
        or (ne == "island3" and st[2] != "myCaptured"))
    ):
        sig=ne[-1]+","+str(x+2)+","+str(y-2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
        and
        nw=="blank"
    ):
        sig=w[-1]+","+str(x-2)+","+str(y+1)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
        and
        sw=="blank"
    ):
        sig=w[-1]+","+str(x-2)+","+str(y-1)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif (
        ((w== "island1" and st[0] != "myCaptured")
        or (w == "island2" and st[1] != "myCaptured")
        or (w == "island3" and st[2] != "myCaptured"))
    ):
        sig=w[-1]+","+str(x-2)+","+str(y)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif(
         ((sw == "island1" and st[0] != "myCaptured")
        or (sw == "island2" and st[1] != "myCaptured")
        or (sw == "island3" and st[2] != "myCaptured"))
    ):
        sig=sw[-1]+","+str(x-2)+","+str(y+2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif(
        ((nw == "island1" and st[0] != "myCaptured")
        or (nw == "island2" and st[1] != "myCaptured")
        or (nw == "island3" and st[2] != "myCaptured"))
    ):
        sig=nw[-1]+","+str(x-2)+","+str(y-2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
        and
        sw=="blank"
    ):
        sig=s[-1]+","+str(x+1)+","+str(y+2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
        and
        se=="blank"
    ):
        sig=s[-1]+","+str(x-1)+","+str(y+2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif(
        ((s == "island1" and st[0] != "myCaptured")
        or (s == "island2" and st[1] != "myCaptured")
        or (s == "island3" and st[2] != "myCaptured"))
    ):
        sig=s[-1]+","+str(x)+","+str(y+2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
             
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
        and
        nw=="blank"
    ):
        sig=n[-1]+","+str(x+1)+","+str(y-2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
       
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
        and
        ne=="blank"
    ):
        sig=n[-1]+","+str(x-1)+","+str(y-2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
        
    elif(
        ((n == "island1" and st[0] != "myCaptured")
        or (n == "island2" and st[1] != "myCaptured")
        or (n == "island3" and st[2] != "myCaptured"))
    ):
        sig=n[-1]+","+str(x)+","+str(y-2)+","+str(pirate.getCurrentFrame())
        if (z[-12] != sig[0] and z[-8]!= sig[0] and z[-4] != sig[0] ):
            pirate.setTeamSignal(signal +","+ sig)
    else:
        pass
    k=pirate.getTeamSignal().split(",")
    t=k[0]
    if t=="":
        u,v=int(a/2),int(b/2)
        if ((x==p)and(y==q)):
            i=int(pirate.getID())
            r=i%u
            if random.randint(1, 2) == 1:
                if(q==0):
                    pirate.setSignal(str(a-p)+","+str(v-r))
                else:
                    pirate.setSignal(str(a-p)+","+str(v+r))
            else:
                if(p==0):
                    pirate.setSignal(str(u-r)+","+str(b-q))
                else:
                    pirate.setSignal(str(u+r)+","+str(b-q))
        s=pirate.getSignal()
        l=s.split(",")
        m,n=int(l[0]),int(l[1])
        return moveTo(m,n,pirate)
    elif t=="Refresh1":
        pirate.setSignal(str(p)+","+str(q))
        return random.randint(1, 4)
    elif t=="Attack":
        if ((x==p)and(y==q)):
            pirate.setSignal(str(p)+","+str(q))
        elif((x==0)and(y==0)):
            pirate.setSignal(str(0)+","+str(0))
        elif((x==a-1)and(y==0)):
            pirate.setSignal(str(a-1)+","+str(0))
        elif((x==0)and(y==b-1)):
            pirate.setSignal(str(0)+","+str(b-1))
        elif((x==a-1)and(y==b-1)):
            pirate.setSignal(str(a-1)+","+str(b-1))
        elif((x==a-1)or(x==0)or(y==0)or(y==b-1)):
            pirate.setSignal(str(x)+","+str(y))
        s=pirate.getSignal()
        l=s.split(",")
        m,n=int(l[0]),int(l[1])
        return moveAway(m,n,pirate)
    
    elif t[0:7]=="Capture":
        f=(int(pirate.getID()))%3
        if f==0:
            if not(x==int(k[2]) and y==int(k[3])):
                t=t[0:7]+"0"+t[8:]
                k[0]=t
                z=','.join(k)
                pirate.setTeamSignal(z)
            return moveTo(int(k[2]),int(k[3]),pirate)
        elif f==1:
            if not(x==int(k[6])and y==(int(k[7]))):
                t=t[0:8]+"0"+t[9]
                k[0]=t
                z=','.join(k)
                pirate.setTeamSignal(z)
            return moveTo(int(k[6]),int(k[7]),pirate)
        elif f==2:
            if not(x==int(k[10]) and y==int(k[11])):
                t=t[0:9]+"0"
                k[0]=t
                z=','.join(k)
                pirate.setTeamSignal(z)
            return moveTo(int(k[10]),int(k[11]),pirate)

def ActTeam(team):
    time=team.getCurrentFrame()
    ts=team.getTeamSignal()
    k=ts.split(",")
    t=k[0]
    if((t=="")and(time>70)):
        k[0]="Refresh1"
        z=','.join(k)
        team.setTeamSignal(z)
    if(t=="Refresh1"):
        k[0]="Attack"
        z=','.join(k)
        team.setTeamSignal(z)
    elif((t=="Attack")and(time>200)):
        k[0]="Capture111"
        z=','.join(k)
        team.setTeamSignal(z)
    elif time>200:
        if(int(t[7])==1):
            team.buildWalls(int(k[1]))
        if(int(t[8])==1):
            team.buildWalls(int(k[5]))
        if(int(t[9])==1):
            team.buildWalls(int(k[9]))
        k[0]="Capture111"
        z=','.join(k)
        team.setTeamSignal(z)

    return 0
