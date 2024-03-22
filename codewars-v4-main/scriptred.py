#includes additional phase from 200 to 300 tf in which the pirates moveTo an allocated point and returns random thereafter
import random
import math
name="updatedCobra"
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
                    pirate.setSignal(str(a-p-1)+","+str(v-r))
                else:
                    pirate.setSignal(str(a-p-1)+","+str(v+r))
            else:
                if(p==0):
                    pirate.setSignal(str(u-r)+","+str(b-q-1))
                else:
                    pirate.setSignal(str(u+r)+","+str(b-q-1))
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
    elif t=="Refresh2":
        pirate.setSignal(str(p)+","+str(q))
        return random.randint(1, 4)
    elif t=="Expand":
        if ((x==p)and(y==q)):
            pirate.setSignal(str(p)+","+str(q))
            return random.randint(1, 4)
        s=pirate.getSignal()
        l=s.split(",")
        m,n=int(l[0]),int(l[1])
        if ((m==p)and(n==q)):
            d=random.randint(1, 5)
            g=random.randint(1, 5)
            pirate.setSignal(str(d*a//6)+","+str(g*b//6))
        elif ((x==m)and(y==n)):
            pirate.setSignal("-1,-1")
            print("Reached")
        if s=="-1,-1":
            return random.randint(1, 4)
        else:
            return moveTo(m,n,pirate)
    elif t[0:7]=="Capture":
        f=(int(pirate.getID()))%4
        if f==0 and len(k)>4:
            if not(x==int(k[2]) and y==int(k[3])):
                t=t[0:7]+"0"+t[8:]
                k[0]=t
                z=','.join(k)
                pirate.setTeamSignal(z)
            return moveTo(int(k[2]),int(k[3]),pirate)
        elif f==1 and len(k)>8:
            if not(x==int(k[6])and y==(int(k[7]))):
                t=t[0:8]+"0"+t[9]
                k[0]=t
                z=','.join(k)
                pirate.setTeamSignal(z)
            return moveTo(int(k[6]),int(k[7]),pirate)
        elif f==2 and len(k)>12:
            if not(x==int(k[10]) and y==int(k[11])):
                t=t[0:9]+"0"
                k[0]=t
                z=','.join(k)
                pirate.setTeamSignal(z)
            return moveTo(int(k[10]),int(k[11]),pirate)
        else:
            return random.randint(1,4)

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
        k[0]="Refresh2"
        z=','.join(k)
        team.setTeamSignal(z)
    elif (t=="Refresh2"):
        k[0]="Expand"
        z=','.join(k)
        team.setTeamSignal(z)
    elif((t=="Expand")and(time>300)):
        k[0]="Capture111"
        z=','.join(k)
        team.setTeamSignal(z)
    elif time>300:
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





# from random import randint 

# name = 'sample4'

# def moveTo(x , y , Pirate):
#     position = Pirate.getPosition()
#     if position[0] == x and position[1] == y:
#         return 0
#     if position[0] == x:
#         return (position[1] < y) * 2 + 1
#     if position[1] == y:
#         return (position[0] > x) * 2 + 2
#     if randint(1, 2) == 1:
#         return (position[0] > x) * 2 + 2
#     else:
#         return (position[1] < y) * 2 + 1
    
# def checkfriends(pirate , quad ):
#     sum = 0 
#     up = pirate.investigate_up()[1]
#     print(up)
#     down = pirate.investigate_down()[1]
#     left = pirate.investigate_left()[1]
#     right = pirate.investigate_right()[1]
#     ne = pirate.investigate_ne()[1]
#     nw = pirate.investigate_nw()[1]
#     se = pirate.investigate_se()[1]
#     sw = pirate.investigate_sw()[1]
    
#     if(quad=='ne'):
#         if(up == 'friend'):
#             sum +=1 
#         if(ne== 'friend'):
#             sum +=1 
#         if(right == 'friend'):
#             sum +=1 
#     if(quad=='se'):
#         if(down == 'friend'):
#             sum +=1 
#         if(right== 'friend'):
#             sum +=1 
#         if(se == 'friend'):
#             sum +=1 
#     if(quad=='sw'):
#         if(down == 'friend'):
#             sum +=1 
#         if(sw== 'friend'): 
#             sum +=1 
#         if(left == 'friend'):
#             sum +=1 
#     if(quad=='nw'):
#         if(up == 'friend'):
#             sum +=1 
#         if(nw == 'friend'):
#             sum +=1 
#         if(left == 'friend'):
#             sum +=1 

#     return sum
    
# def spread(pirate):
#     sw = checkfriends(pirate ,'sw' )
#     se = checkfriends(pirate ,'se' )
#     ne = checkfriends(pirate ,'ne' )
#     nw = checkfriends(pirate ,'nw' )
   
#     my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

#     x, y = pirate.getPosition()
    
#     if( x == 0 , y == 0):
#         return randint(1,4)
    
#     if(sorted_dict[list(sorted_dict())[3]] == 0 ):
#         return randint(1,4)
    
#     if(list(sorted_dict())[0] == 'sw'):
#         return moveTo(x-1 , y+1 , pirate)
#     elif(list(sorted_dict())[0] == 'se'):
#         return moveTo(x+1 , y+1 , pirate)
#     elif(list(sorted_dict())[0] == 'ne'):
#         return moveTo(x+1 , y-1 , pirate)
#     elif(list(sorted_dict())[0] == 'nw'):
#         return moveTo(x-1 , y-1 , pirate)

# def ActPirate(pirate):
#     up = pirate.investigate_up()[0]
#     down = pirate.investigate_down()[0]
#     left = pirate.investigate_left()[0]
#     right = pirate.investigate_right()[0]
#     x, y = pirate.getPosition()
#     pirate.setSignal("")
#     s = pirate.trackPlayers()
    
#     if (
#         (up == "island1" and s[0] != "myCaptured")
#         or (up == "island2" and s[1] != "myCaptured")
#         or (up == "island3" and s[2] != "myCaptured")
#     ):
#         s = up[-1] + str(x) + "," + str(y - 1)
#         pirate.setTeamSignal(s)

#     if (
#         (down == "island1" and s[0] != "myCaptured")
#         or (down == "island2" and s[1] != "myCaptured")
#         or (down == "island3" and s[2] != "myCaptured")
#     ):
#         s = down[-1] + str(x) + "," + str(y + 1)
#         pirate.setTeamSignal(s)

#     if (
#         (left == "island1" and s[0] != "myCaptured")
#         or (left == "island2" and s[1] != "myCaptured")
#         or (left == "island3" and s[2] != "myCaptured")
#     ):
#         s = left[-1] + str(x - 1) + "," + str(y)
#         pirate.setTeamSignal(s)

#     if (
#         (right == "island1" and s[0] != "myCaptured")
#         or (right == "island2" and s[1] != "myCaptured")
#         or (right == "island3" and s[2] != "myCaptured")
#     ):
#         s = right[-1] + str(x + 1) + "," + str(y)
#         pirate.setTeamSignal(s)

    
#     if pirate.getTeamSignal() != "":
#         s = pirate.getTeamSignal()
#         l = s.split(",")
#         x = int(l[0][1:])
#         y = int(l[1])
    
#         return moveTo(x, y, pirate)

#     else:
#         return spread(pirate)


# def ActTeam(team):
#     l = team.trackPlayers()
#     s = team.getTeamSignal()

#     team.buildWalls(1)
#     team.buildWalls(2)
#     team.buildWalls(3)

#     if s:
#         island_no = int(s[0])
#         signal = l[island_no - 1]
#         if signal == "myCaptured":
#             team.setTeamSignal("")
