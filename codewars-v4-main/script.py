
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
    
 #inputs such that x2>x1 and y2>y1
def moveAwayBounded(x,y,x1,x2,y1,y2,Pirate):
    position=Pirate.getPosition()
    list=[]
    d={1:-1,2:1,3:1,4:-1}
    if position[0]==x and position[1]==y:
        if(x==x1 and y>y1 and y<y2): return 2
        if(x==x2 and y>y1 and y<y2): return 4
        if(y==y1 and x>x1 and x<x2): return 3
        if(y==y2 and x>x1 and x<x2): return 1
        if(y-1>=y1): list.append(1)
        if(y+1<=y2): list.append(3)
        if(x-1>=x1): list.append(4)
        if(x+1<=x2): list.append(2)
        else: pass
    elif position[0]==x:
        k=(position[1]>y)*2+1
        if(x-1>=x1): list.append(4)
        if(x+1<=x2): list.append(2)
        if(position[1]+d[k]<=y2 and position[1]+d[k]>=y1): list.append(k)
    elif position[1]==y:
        k=(position[0]<x)*2+2
        if(y-1>=y1): list.append(1)
        if(y+1<=y2): list.append(3)
        if(position[0]+d[k]>=x1 and position[0]+d[k]<=x2): list.append(k)
    else :
        k1=(position[0]<x)*2+2
        k2=(position[1]>y)*2+1
        if(position[0]+d[k1]>=x1 and position[0]+d[k1]<=x2): list.append(k1)
        if(position[1]+d[k2]>=y1 and position[1]+d[k2]<=y2): list.append(k2)
    
    return random.choice(list)         
    
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

def enemy_kill(x,y,Pirate):
    n1= Pirate.investigate_up()[1]
    s1= Pirate.investigate_down()[1]
    w1= Pirate.investigate_left()[1]
    e1= Pirate.investigate_right()[1]
    ne1=Pirate.investigate_ne()[1]
    se1=Pirate.investigate_se()[1]
    nw1=Pirate.investigate_nw()[1]
    sw1=Pirate.investigate_sw()[1]
    r=Pirate.getPosition()
    p=Pirate.getDeployPoint()
    if r[0]==x and r[1]==y :
        if (n1=="enemy" or n1=="both"):
            Pirate.setSignal(str(x)+","+str(y-1))
        elif (e1=="enemy" or e1=="both"):
            Pirate.setSignal(str(x+1)+","+str(y))
        elif (s1=="enemy" or s1=="both"):
            Pirate.setSignal(str(x)+","+str(y+1))
        elif (w1=="enemy" or w1=="both"):
            Pirate.setSignal(str(x-1)+","+str(y))
        elif (ne1=="enemy" or ne1=="both"):
            Pirate.setSignal(str(x+1)+","+str(y-1))
        elif (nw1=="enemy" or nw1=="both"):
            Pirate.setSignal(str(x-1)+","+str(y-1))
        elif (se1=="enemy" or se1=="both"):
            Pirate.setSignal(str(x+1)+","+str(y+1))
        elif (sw1=="enemy" or sw1=="both"):
            Pirate.setSignal(str(x-1)+","+str(y+1))
        else : pass
    s=Pirate.getSignal()
    if (s==f"{p[0]},{p[1]}" or s==str(x)+","+str(y)) : return 0
    l=s.split(",")
    m,n=int(l[0]),int(l[1])
    if(r[0]==m and r[1]==n):
        Pirate.setSignal(str(x)+","+str(y))
    s=Pirate.getSignal()
    l=s.split(",")
    m,n=int(l[0]),int(l[1])
    return moveTo(m,n,Pirate)
 
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
    time=pirate.getCurrentFrame()
    
    u,v=int(a/2),int(b/2)

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
            i=int(pirate.getID())-1
            if i%2==0:
                r=int((i/2)%u)
                if(q==0):
                    pirate.setSignal(str(a-p-1)+","+str(r))
                else:
                    pirate.setSignal(str(a-p-1)+","+str(b-1-r))
            else:
                r=int(((i-1)/2)%u)
                if(p==0):
                    pirate.setSignal(str(r)+","+str(b-q-1))
                else:
                    pirate.setSignal(str(a-1-r)+","+str(b-q-1))
        
        s=pirate.getSignal()
        l=s.split(",")
        m,n=int(l[0]),int(l[1])
        return moveTo(m,n,pirate)
    
    
    elif t=="Refresh1":
        pirate.setSignal(str(p)+","+str(q))
        return random.randint(1, 4)
    
    
    elif t=="Attack":    
        if ((x==a-1) or (x==0) or (y==0) or (y==b-1)):
            pirate.setSignal(str(x)+","+str(y))
        else : pass
        
        s=pirate.getSignal()
        l=s.split(",")
        m,n=int(l[0]),int(l[1])
        return moveAway(m,n,pirate)
    
    elif t=="Refresh2":
        pirate.setSignal(str(p)+","+str(q))
        return random.randint(1, 4)
        
    elif t[0:7]=="Capture":
        f=(int(pirate.getID()))%4
        if (len(k)==5):
            if (f==0):
                s=pirate.getSignal()
                if not(x==int(k[2]) and y==int(k[3])) and s==f"{p},{q}":
                    t=t[0:7]+"0"+t[8:]
                    k[0]=t
                    z=','.join(k)
                    pirate.setTeamSignal(z)
                    return moveTo(int(k[2]),int(k[3]),pirate)
                else:
                    return enemy_kill(int(k[2]),int(k[3]),pirate)    
            elif (f==1 or f==2):
                if (time==6*a+1):
                    pirate.setSignal(str(a-1-p)+","+str(b-1-q))
                else:
                    d=q<v
                    c=p<u
                    if(x==a-1-p or y==b-1-q or (x==c+u-1 and y>=(v(1-d)) and y<=(v(2-d)-1 )) or (x==p and y>=d*v and y<=v*(d+1)-1) or (y==d+v-1 and x>=(u(1-c)) and x<=(u(2-c)-1)) or (y==q and x>=c*u and x<=(u*(c+1)-1))):
                        pirate.setSignal(str(x)+","+str(y))
                s=pirate.getSignal()
                l=s.split(",")
                m,n=int(l[0]),int(l[1])
                return moveAway(m,n,pirate)
            else :
                o=(int(pirate.getID())-3)/4
                if(o%4==0):
                    if(time<=6.5*a):
                        return moveTo(3*(u//2),(v)//2,pirate)
                    elif(time==6.5*a+1):
                        pirate.setSignal(str(3*(u//2))+","+str(v//2))
                    else:
                        if(x==u or x==a-1 or y==0 or y==v-1):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,u,a-1,0,v-1,pirate)
                elif(o%4==1):
                    if(time<=7.5*a):
                        return moveTo(u//2,v//2,pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(u//2)+","+str(v//2))
                    else:
                        if(x==u-1 or x==0 or y==0 or y==v-1):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,0,u-1,0,v-1,pirate)
                elif(o%4==2):
                    if(time<=7.5*a):
                        return moveTo(u//2,3*(v//2),pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(u//2)+","+str(3*(v//2)))
                    else:
                        if(x==u-1 or x==0 or y==b-1 or y==v):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,0,u-1,v,b-1,pirate)
                else:
                    if(time<=7.5*a):
                        return moveTo(3*(u//2),3*(v//2),pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(3*(u//2))+","+str(3*(v//2)))
                    else:
                        if(x==u or x==a-1 or y==b-1 or y==v):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,u,a-1,v,b-1,pirate)
                
                    
        elif(len(k)==9):
            time_new=k[8]
            if (f==0):
                s=pirate.getSignal()
                if not(x==int(k[2]) and y==int(k[3])) and s==f"{p},{q}":
                    t=t[0:7]+"0"+t[8:]
                    k[0]=t
                    z=','.join(k)
                    pirate.setTeamSignal(z)
                    return moveTo(int(k[2]),int(k[3]),pirate)
                else:
                    return enemy_kill(int(k[2]),int(k[3]),pirate)
            elif (f==1):
                if(time==k[8]): pirate.setSignal(f"{p},{q}")
                s=pirate.getSignal()
                if not(x==int(k[6]) and y==int(k[7])) and s==f"{p},{q}":
                    t=t[0:8]+"0"+t[9]
                    k[0]=t
                    z=','.join(k)
                    pirate.setTeamSignal(z)
                    return moveTo(int(k[6]),int(k[7]),pirate)
                else:
                    return enemy_kill(int(k[6]),int(k[7]),pirate)
            elif (f==2):
                if (time<=time_new+1):
                    pirate.setSignal(str(a-1-p)+","+str(b-1-q))
                else:
                    d=q<v
                    c=p<u
                    if(x==a-1-p or y==b-1-q or (x==c+u-1 and y>=(v(1-d)) and y<=(v(2-d)-1 )) or (x==p and y>=d*v and y<=v*(d+1)-1) or (y==d+v-1 and x>=(u(1-c)) and x<=(u(2-c)-1)) or (y==q and x>=c*u and x<=(u*(c+1)-1))):
                        pirate.setSignal(str(x)+","+str(y))
                s=pirate.getSignal()
                l=s.split(",")
                m,n=int(l[0]),int(l[1])
                return moveAway(m,n,pirate)
            else:
                o=(int(pirate.getID())-3)/4
                if(o%4==0):
                    if(time<=6.5*a):
                        return moveTo(3*(u//2),(v)//2,pirate)
                    elif(time==6.5*a+1):
                        pirate.setSignal(str(3*(u//2))+","+str(v//2))
                    else:
                        if(x==u or x==a-1 or y==0 or y==v-1):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,u,a-1,0,v-1,pirate)
                elif(o%4==1):
                    if(time<=7.5*a):
                        return moveTo(u//2,v//2,pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(u//2)+","+str(v//2))
                    else:
                        if(x==u-1 or x==0 or y==0 or y==v-1):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,0,u-1,0,v-1,pirate)
                elif(o%4==2):
                    if(time<=7.5*a):
                        return moveTo(u//2,3*(v//2),pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(u//2)+","+str(3*(v//2)))
                    else:
                        if(x==u-1 or x==0 or y==b-1 or y==v):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,0,u-1,v,b-1,pirate)
                else:
                    if(time<=7.5*a):
                        return moveTo(3*(u//2),3*(v//2),pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(3*(u//2))+","+str(3*(v//2)))
                    else:
                        if(x==u or x==a-1 or y==b-1 or y==v):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,u,a-1,v,b-1,pirate)
                
                
        
        elif (len(k)==13):
            if(f==0):
                s=pirate.getSignal()
                print(s)
                if not(x==int(k[2]) and y==int(k[3])) and s==f"{p},{q}":
                    t=t[0:7]+"0"+t[8:]
                    k[0]=t
                    z=','.join(k)
                    pirate.setTeamSignal(z)
                    return moveTo(int(k[2]),int(k[3]),pirate)
                else:
                    return enemy_kill(int(k[2]),int(k[3]),pirate) 
            elif(f==1):
                s=pirate.getSignal()
                if not(x==int(k[6]) and y==int(k[7])) and s==f"{p},{q}":
                    t=t[0:8]+"0"+t[9]
                    k[0]=t
                    z=','.join(k)
                    pirate.setTeamSignal(z)
                    return moveTo(int(k[6]),int(k[7]),pirate)
                else:
                    return enemy_kill(int(k[6]),int(k[7]),pirate)
            elif (f==2):
                if(time==k[12]): pirate.setSignal(f"{p},{q}")
                s=pirate.getSignal()
                if not(x==int(k[10]) and y==int(k[11])) and s==f"{p},{q}":
                    t=t[0:9]+"0"
                    k[0]=t
                    z=','.join(k)
                    pirate.setTeamSignal(z)
                    return moveTo(int(k[10]),int(k[11]),pirate)
                else:
                    return enemy_kill(int(k[10]),int(k[11]),pirate) 
            else:
                o=(int(pirate.getID())-3)/4
                if(o%4==0):
                    if(time<=6.5*a):
                        return moveTo(3*(u//2),(v)//2,pirate)
                    elif(time==6.5*a+1):
                        pirate.setSignal(str(3*(u//2))+","+str(v//2))
                    else:
                        if(x==u or x==a-1 or y==0 or y==v-1):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,u,a-1,0,v-1,pirate)
                elif(o%4==1):
                    if(time<=7.5*a):
                        return moveTo(u//2,v//2,pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(u//2)+","+str(v//2))
                    else:
                        if(x==u-1 or x==0 or y==0 or y==v-1):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,0,u-1,0,v-1,pirate)
                elif(o%4==2):
                    if(time<=7.5*a):
                        return moveTo(u//2,3*(v//2),pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(u//2)+","+str(3*(v//2)))
                    else:
                        if(x==u-1 or x==0 or y==b-1 or y==v):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,0,u-1,v,b-1,pirate)
                else:
                    if(time<=7.5*a):
                        return moveTo(3*(u//2),3*(v//2),pirate)
                    elif(time==7.5*a+1):
                        pirate.setSignal(str(3*(u//2))+","+str(3*(v//2)))
                    else:
                        if(x==u or x==a-1 or y==b-1 or y==v):
                            pirate.setSignal(str(x)+","+str(y))
                    s=pirate.getSignal()
                    l=s.split(",")
                    m,n=int(l[0]),int(l[1])
                    return moveAwayBounded(m,n,u,a-1,v,b-1,pirate)
                
        else:
            pass
        
        
def ActTeam(team):
    time=team.getCurrentFrame()
    a=team.getDimensionX()
    b=team.getDimensionY()
    ts=team.getTeamSignal()
    k=ts.split(",")
    t=k[0]
    if((t=="")and(time>(2*a))):
        k[0]="Refresh1"
        z=','.join(k)
        team.setTeamSignal(z)
        
    if(t=="Refresh1"):
        k[0]="Attack"
        z=','.join(k)
        team.setTeamSignal(z)
    
    elif((t=="Attack")and(time==6*a)):
        k[0]="Refresh2"
        z=','.join(k)
        team.setTeamSignal(z)
    
    elif((t=="Refresh2")and(time>6*a)):
        k[0]="Capture111"
        z=','.join(k)
        team.setTeamSignal(z)
         
    elif time>6*a:
        if(len(k)==5):
            if(int(t[7])==1):
                team.buildWalls(int(k[1]))
        elif(len(k)==9):
            if(int(t[7])==1):
                team.buildWalls(int(k[1]))
            if(int(t[8])==1):
                team.buildWalls(int(k[5]))
        elif(len(k)==13):
            if(int(t[7])==1):
                team.buildWalls(int(k[1]))
            if(int(t[8])==1):
                team.buildWalls(int(k[5]))
            if(int(t[9])==1):
                team.buildWalls(int(k[9]))
        else: pass
        
        k[0]="Capture111"
        z=','.join(k)
        team.setTeamSignal(z)
    
    else: 
        pass

    return 0
