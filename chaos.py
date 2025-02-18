from graphics import *
from button import *
from stack import *
import math
import random
import time
from stack import *
import threading
class Game:
    def __init__(self,win,width,length,bombnum):
        self.win=win
        self.win.setCoords(-0.25,-1.0,width*1.00+1.25,length*1.0+1.0)
        self.width=width
        self.length=length
        self.bombnum=bombnum
        
        self.startbutton=Button(win,Point(1.0,-0.5),1.2,0.8,'Start')
        self.setbomb=Button(win,Point(3.0,-0.5),1.2,0.8,'SetBomb')
        self.quitbutton=Button(win,Point(width*1.0-1.0,-0.5),1.2,0.8,'quit')
        self.newgame=Button(win,Point(width*1.0+0.6,length*1.0-1.0),1.0,0.8,'NewGame')
        self.easy=Button(win,Point(width*1.0+0.6,length*1.0-2.0),1.0,0.8,'Easy')
        self.middle=Button(win,Point(width*1.0+0.6,length*1.0-3.0),1.0,0.8,'Middle')
        self.hard=Button(win,Point(width*1.0+0.6,length*1.0-4.0),1.0,0.8,'Hard')
        self.setbutton=Button(win,Point(width*1.0+0.6,length*1.0-5.0),1.0,0.8,'Set')

        self.startbutton.activate()
        self.quitbutton.activate()
        self.newgame.activate()
        self.easy.activate()
        self.middle.activate()
        self.hard.activate()
        self.setbutton.activate()
        self.undobutton=Button(win,Point(width*1.0-3.0,-0.5),1.2,0.8,'Undo')
        self.rec1=Rectangle(Point(width-1,length*1.0+0.2),Point(width-3,length*1.0+0.8))
        label=Text(Point(width-2,length*1.0+0.5),'%d'% bombnum)
        label.draw(self.win)
        self.rec1.draw(self.win)
        self.rec2=Rectangle(Point(width-4,length*1.0+0.2),Point(width-6,length*1.0+0.8))
        self.rec2.draw(win)
        self.rowlist=[]  #所有的格
        self.playerbomb=Stack() #用户标记的雷
        self.restplayerbomb=[] #用户标记的雷
        self.realbomb=[]
        self.square=Stack()
        self.timeused=0


        for i in range(self.length):
            columnlist=[]
            for j in range(self.width):
                rec=Rectangle(Point(j*1.00,i*1.00),Point(j*1.00+1.00,i*1.00+1.00))
                rec.setFill('lightgrey')
                columnlist.append(rec)
                rec.draw(self.win)
            self.rowlist.append(columnlist)
        for i in range(self.length):
            for j in range(self.width):
                self.square.push(self.rowlist[i][j])
    def setground(self):
        for i in range(self.length):
            columnlist=[]
            for j in range(self.width):
                rec=Rectangle(Point(j*1.00,i*1.00),Point(j*1.00+1.00,i*1.00+1.00))
                rec.setFill('lightgrey')
                columnlist.append(rec)
                rec.draw(self.win)
            self.rowlist.append(columnlist)
        for i in range(self.length):
            for j in range(self.width):
                self.square.push(self.rowlist[i][j])
    def setbomb(self,q,imagename):
        x=math.floor(q.getX())
        y=math.floor(q.getY())
        if [x,y] in self.realbomb:
            self.restplayerbomb.remove([x,y])
        image=Image(Point(x*1.0+0.5,y*1.0+0.5),imagename)
        if self.rowlist[y][x] in self.square.mylist():
            self.playerbomb.push(image)
            a=self.square.pop(self.rowlist[y][x])
            image.draw(self.win)
    def undo(self):
        a=self.playerbomb.pop()
        self.playerbombnum.push()
        a.undraw()
        p=a.getAnchor()
        x=p.getX()-0.5
        y=p.getY()-0.5
        self.square.push(self.rowlist[y][x])
    def start(self):
        self.setground()
        self.startbutton.deactivate()
        self.setbomb.activate()
        self.counttime()
        for i in range(self.width):
            ll=[]
            a=random.randrange(1,self.width)
            ll.append(a)
            for j in range(self.length):
                b=random.randrange(1,self.length)
                ll.append(b)
            self.realbomb.append(ll)
            self.restplayerbomb.append(ll)
    def fail(self):
        self.setbomb.deactivate()
        self.undobutton.deactivate()
        label=Text(Point(self.width/2,self.length/2),'BOMB!!!')
    def getrealbomb(self):
        return self.realbomb
    def uncover(self,q):
        x=int(math.floor(q.getX()))
        y=int(math.floor(q.getY()))
        if [x,y] in self.realbomb:
            self.fail()
        elif self.rowlist[y][x] in self.square.mylist:
            ll=[x,y]
            self.displaynum(ll)
    def displaynum(self,ll):
        k=0
        x=ll[0]
        y=ll[1]
        if ll in self.realbomb:
            pass
        elif self.rowlist[y][x] in self.square.mylist:
            for i in range(3):
                for j in range(3):
                    if [x+i-1,y+j-1] in self.realbomb:
                        k+=1
            if k!=0:
                labal=Text(Point(x*1.0+0.5,y*1.0+0.5),str(k))
                label.draw(self.win)
                self.rowlist[y][x].setFill('white')
                a=self.square.pop(self.rowlist[y][x])
            else:
                for i in range(3):
                    for j in range(3):
                        if self.rowlist[y-1+i][x-1+j] in self.square.mylist:
                            self.displaynum([x-1+j,y-1+i])
    def IsWin(self):
        if len(self.restplayerbomb)==0:
            return True
        else:
            return False
    def setlevel(self,q):
        self.easy.activate()
        self.middle.activate()
        self.hard.activate()
        self.setbutton.activate()
        if self.easy.clicked(q):
            win1=GraphWin('Mining',330,330)
            return Game(win1,9,9,10)
        elif self.middle.clicked(q):
            win2=GraphWin('Mining',9*30+60,16*30+60)
            return Game(win2,9,16,40)
        elif self.hard.clicked(q):
            win3=GraphWin('Mining',16*30+60,16*30+60)
            return Game(win3,16,16,99)
        elif self.setbutton.clicked(q):
            win=GraphWin('Set it!',100,100)
            win.setCoords(0,0,10,10)
            sure=Button(win,Point(5,2),2,1,'Set')
            sure.activate()
            Text(Point(3,8),'       Width:').draw(win)
            time.sleep(1)
            Text(Point(3,6),'      Length:').draw(win)
            time.sleep(1)
            Text(Point(3,4),'Bomb Numbers:').draw(win)
            time.sleep(1)
            input1=Entry(Point(6,8),4)
            input1.setText('9')
            input1.draw(win)
            input2=Entry(Point(6,6),4)
            input2.setText('9')
            input2.draw(win)
            input3=Entry(Point(6,4),4)
            input3.setText('10')
            input3.draw(win)
            p=win.getMouse()
            if sure.clicked(p):
                ww=eval(input1.getText())
                ll=eval(input2.getText())
                bb=eval(input3.getText())
                win4=GraphWin('Mining',ww*30+60,ll*30+60)
                return Game(win4,ww,ll,bb)
                win.close()
    def WIN(self):
        if self.IsWin():
            t=str(calTime([1]))
            Text(Point(width-5,length*1.0-0.5),t).draw(self.win)
    def counttime(self):
        for i in xrange(1,1000):
            if self.IsWin==False:
                self.timeused=i
                Text(Point(width-2,length*1.0+0.5),'%d'% self.timeused).draw(win)
                time.sleep(1)
        
            
            
            
        
    
        
        
    
        
            
            
def main():
    win=GraphWin('mining',330,330)
    base=Game(win,9,9,10)
    base.setground()
    while True:
        p=win.getMouse()
        if base.quitbutton.clicked(p):
            break
        elif base.newgame.clicked(p):
            q=win.getMouse()
            base=base.setlevel(q)
        elif base.startbutton.clicked(p):
            base.start()
            while not base.IsWin():
                pp=base.win.getMouse()
                if base.quitbutton.clicked(pp):
                    break
                elif base.setbomb.clicked(pp):
                    p1=base.win.getMouse()
                    base.setbomb(p1,'bomb.gif')
                elif 0<=math.floor(pp.getX())<=base.width and 0<=math.floor(pp.getY())<=base.length:
                    base.uncover(pp)
                elif base.undobutton.clicked(pp):
                    base.undo()
            time=str(base.WIN())
    base.win.close()
main()
    
    
            
        


            
       





    



















    
