from graphics import *
import time
import random
from button import *
import copy
class CNUM:
    def __init__(self,centerpoint,num,win):
        self.num=num
        self.win=win
        self.centerpoint=centerpoint
        self.circle=Circle(self.centerpoint,0.5)
        self.label=Text(self.centerpoint,str(self.num))
    def drawnum(self):
        self.label.draw(self.win)
    def covernum(self):
        self.label.undraw()
        self.circle.setFill('purple')
        self.circle.draw(self.win)
        self.active=False
    def uncovernum(self):
        self.circle.undraw()
        self.label.draw(self.win)
        self.activate=True
    def clicked(self,p):
        if self.active:
            pass
        else:
            if (p.getX()-self.centerpoint.getX())**2+(p.getY()-self.centerpoint.getY())**2<=0.25:
                return True
    def movenum(self,dx,dy):
        self.centerpoint.move(dx,dy)
        self.circle.move(dx,dy)
        self.label.move(dx,dy)
    def getnum(self):
        return self.num
    def uncovered(self):
        return self.active
    def covered(self):
        return not self.active
    
def test():
    win=GraphWin('memory test',600,800)
    win.setCoords(0.0,-2.0,6.0,6.0)
    reset=Button(win,Point(1.0,-1.0),1.6,0.8,'reset')
    reset.activate()
    quitbutton=Button(win,Point(5.0,-1.0),1.6,0.8,'quit')
    quitbutton.activate()
    p=win.getMouse()
    ll=range(1,10)
    l=[]
    while True:
        if quitbutton.clicked(p):
            break
        elif reset.clicked(p):
            random.shuffle(ll)
            for i in range(4):
                a=CNUM(Point(3.0,3.0),ll[i],win)
                a.movenum((2-i)*0.8,i-2)
                a.drawnum()
                l.append(a)
            time.sleep(1)
            for i in range(4):
                l[i].covernum()
            lll=copy.copy(ll)
            while l[0].covered() or l[1].covered() or l[2].covered() or l[3].covered():
                q=win.getMouse()
                for i in range(4):
                    if l[i].clicked(q):
                        l[i].uncovernum()
                        lll.remove(ll[i])
                        lll.sort(key=int)
                        if l[i].getnum()>lll[0]:
                            for b in range(4):
                                if l[b].uncovered():
                                    l[b].covernum()
            if l[0].uncovered() and l[1].uncovered() and l[2].uncovered() and l[3].uncovered():
                label=Text(Point(3.0,-1.0),'Success!')
                label.draw(win)
    win.close()
if __name__=='__main__':
    test()
                
                            
                        
                        
                        
                
                            
        
            
            
        
        
            
        
