from graphics import *
from time import *
from button import *
from random import *
from copy import *
from threading import *
class CNUM:
    def __init__(self,win,point,radius,num):
        self.center=point
        self.radius=radius
        self.cir=Circle(point,radius)
        self.num=num
        self.tex=Text(point,num)
        self.tex.setSize(33)
        self.tex.setStyle('bold')
        self.tex.setFace('times roman')
        self.cir.setWidth(5)
        self.tex.setOutline('gray')
        self.tex.draw(win)
        self.cir.setOutline('gray')
        self.cir.draw(win)
    def setColor(self,color):
        self.cir.setOutline(color)
    def coverCircle(self):
        self.cir.undraw()
    def coverNumber(self):
        self.tex.undraw()
    def uncoverCircle(self,win):
        self.cir.draw(win)
    def uncoverNumber(self,win):
        self.tex.draw(win)
    def twinkle(self):
        sleep(1)
        self.coverNumber()
    def clicked(self,p):
        r1=(p.getX()-self.center.getX())*(p.getX()-self.center.getX())
        r2=(p.getY()-self.center.getY())*(p.getY()-self.center.getY())
        if r1+r2<self.radius*self.radius:
            return True
        else:
            return False
def reset():
    cho=[]
    while len(cho)<3:
        p=randrange(10)
        if p not in cho:
            cho.append(p)
    return cho
def thread_run(w,b):
    colorlist=['blue','green','yellow','purple','orange','gray']
    while 1:
        num=randrange(6)
        s=colorlist[num]
        sleep(2)
        for i in b:
            i.setColor(s)
    
        
    
    
def main():
    global win
    win=GraphWin('memory test',500,600)
    win.setCoords(0,0,500,600)
    q1=Point(0,100)
    q2=Point(500,100)
    Line(q1,q2).draw(win)
    rb=Button(win,Point(100,50),55,25,'Reset')
    qb=Button(win,Point(400,50),55,25,'Quit')
    rb.activate()
    qb.activate()
    cho=reset()
    b0=CNUM(win,Point(150,200),33,cho[0])
    b1=CNUM(win,Point(350,300),33,cho[1])
    b2=CNUM(win,Point(250,500),33,cho[2])
    s=copy(cho)
    s.sort()
    b=[b0,b1,b2]
    end_mark=[0]
    t=Thread(target=thread_run,args=(win,b,))
    t.start()
    z1=cho.index(s[0])
    z2=cho.index(s[1])
    z3=cho.index(s[2])
    sleep(1)
    for i in b:
        i.coverNumber()
        
    pt=win.getMouse()
    while 1:
        if qb.clicked(pt):
            win.close()
        elif b[z1].clicked(pt):
            b[z1].uncoverNumber(win)
            break
        elif b[z2].clicked(pt):
            b[z2].uncoverNumber(win)
            sleep(0.2)
            b[z2].coverNumber()
            
        elif b[z3].clicked(pt):
            b[z3].uncoverNumber(win)
            sleep(0.2)
            b[z3].coverNumber()
        pt=win.getMouse()
    while 1:
        if qb.clicked(pt):
            win.close()
        elif b[z2].clicked(pt):
            b[z2].uncoverNumber(win)
            break
        elif b[z3].clicked(pt):
            b[z3].uncoverNumber(win)
            sleep(0.2)
            b[z3].coverNumber()
        pt=win.getMouse()
    pt=win.getMouse()
    while 1:
        if qb.clicked(pt):
            win.close()
            break
        elif b[z3].clicked(pt):
            b[z3].uncoverNumber(win)
            break
        pt=win.getMouse()
    qwe=Text(Point(250,50),"success")
    qwe.draw(win)
    pt=win.getMouse()
    while not qb.clicked(pt):
        if rb.clicked(pt):
            qwe.undraw()
            for i in b:
                i.coverNumber()
            cho=reset()
            b0=CNUM(win,Point(150,200),33,cho[0])
            b1=CNUM(win,Point(350,300),33,cho[1])
            b2=CNUM(win,Point(250,500),33,cho[2])
            s=copy(cho)
            s.sort()
            b=[b0,b1,b2]
            t=Thread(target=thread_run,args=(win,b,))
            t.start()
            z1=cho.index(s[0])
            z2=cho.index(s[1])
            z3=cho.index(s[2])
            sleep(1)
            for i in b:
                i.coverNumber()
                
            pt=win.getMouse()
            while  1:
                if qb.clicked(pt):
                    win.close()
                elif b[z1].clicked(pt):
                    b[z1].uncoverNumber(win)
                    break
                elif b[z2].clicked(pt):
                    b[z2].uncoverNumber(win)
                    sleep(0.2)
                    b[z2].coverNumber()
                elif b[z3].clicked(pt):
                    b[z3].uncoverNumber(win)
                    sleep(0.2)
                    b[z3].coverNumber()
                pt=win.getMouse()
            pt=win.getMouse()
            while 1:
                if qb.clicked(pt):
                    win.close()
                elif b[z2].clicked(pt):
                    b[z2].uncoverNumber(win)
                    break
                elif b[z3].clicked(pt):
                    b[z3].uncoverNumber(win)
                    sleep(0.2)
                    b[z3].coverNumber()
                pt=win.getMouse()
            pt=win.getMouse()
            while 1:
                if qb.clicked(pt):
                    win.close()
                elif b[z3].clicked(pt):
                    b[z3].uncoverNumber(win)
                    break
                pt=win.getMouse()
            qwe=Text(Point(250,50),"success")
            qwe.draw(win)
            
        pt=win.getMouse()
    
    win.close()
main()
    
    
    
        
                 
