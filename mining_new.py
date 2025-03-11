from graphics import *
from button import *
from stack import *
import time
import random
import math
import threading

class Game:
    def __init__(self):
        self.columnlist=[]  
        self.restrec=[]     
        self.minerec=[]    
        self.usermark=Stack() 
        
        self.all=[]  
        self.mine=[] 
        self.sweptlist=[] 
        self.mark=Stack()   
        

        self.state='playing'
        self.timeused=0
    def size(self,width,length,bombnum,win):
        self.win=win
        self.win.setCoords(-0.25,-1.0,width*1.00+2.25,length*1.0+1.0)
        self.width=width
        self.length=length
        self.bombnum=str(bombnum)
        self.minenum=bombnum 
        
        self.startbutton=Button(self.win,Point(1.0,-0.5),1.2,0.8,'Start')
        self.setbombbutton=Button(self.win,Point(3.5,-0.5),2.2,0.8,'SetBomb')
        self.quitbutton=Button(self.win,Point(width*1.0-1.0,-0.5),1.2,0.8,'quit')
        self.newgamebutton=Button(self.win,Point(width*1.0+1.2,length*1.0-1.0),2.2,0.8,'NewGame')
        self.easybutton=Button(self.win,Point(width*1.0+1.2,length*1.0-2.0),1.6,0.8,'Easy')
        self.middlebutton=Button(self.win,Point(width*1.0+1.2,length*1.0-3.0),1.6,0.8,'Medium')
        self.hardbutton=Button(self.win,Point(width*1.0+1.2,length*1.0-4.0),1.6,0.8,'Hard')
        self.setbutton=Button(self.win,Point(width*1.0+1.2,length*1.0-5.0),1.6,0.8,'Set')
        self.undobutton=Button(self.win,Point(width*1.0-3.0,-0.5),1.2,0.8,'Undo')
        
        self.startbutton.activate()
        self.quitbutton.activate()
        self.newgamebutton.activate()
        self.easybutton.activate()
        self.middlebutton.activate()
        self.hardbutton.activate()
        self.setbutton.activate()
        self.undobutton.deactivate()
        
        self.labelnum=Text(Point(width-2,length*1.0+0.5),'mines:%d'% self.minenum)
        self.labelnum.draw(self.win)
        self.labeltime=Text(Point(width-6,length*1.0+0.5),'Time:%d'% self.timeused)
        self.labeltime.draw(self.win)

        for i in range(self.width):
            rowlist=[]
            for j in range(self.length):
                rec=Rectangle(Point(i*1.00,j*1.00),Point(i*1.00+1.00,j*1.00+1.00))
                rec.setFill('lightgrey')
                rowlist.append(rec)
                rec.draw(self.win)
            self.columnlist.append(rowlist)  

        for i in range(self.width):
            for j in range(self.length):
                self.all.append([i,j])    

        for i in random.sample(self.all,eval(self.bombnum)):
            self.mine.append(i)    
    def easy(self):
        self.win.close()
        self.__init__()
        self.size(9,9,10,GraphWin('Mining',360,330))
        self.setbombbutton.activate()
        self.undobutton.activate()
    def middle(self):
        self.win.close()
        self.__init__()
        self.size(9,16,40,GraphWin('Mining',360,16*30+60))
        self.setbombbutton.activate()
        self.undobutton.activate()
    def hard(self):
        self.win.close()
        self.__init__()
        self.size(16,16,99,GraphWin('Mining',16*30+90,16*30+60))
        self.setbombbutton.activate()
        self.undobutton.activate()
    def diy(self):
        win=GraphWin('Set your level!',400,500)
        win.setCoords(0,0,4,5)
        sure=Button(win,Point(2,1),1.4,0.8,'Set')
        sure.activate()

        Text(Point(1,4),'       Width:').draw(win)
        Text(Point(1,3),'      Length:').draw(win)
        Text(Point(1,2),'Bomb Numbers:').draw(win)
        
        input1=Entry(Point(3,4),3)
        input1.setText('9')
        input1.draw(win)
        input2=Entry(Point(3,3),3)
        input2.setText('9')
        input2.draw(win)
        input3=Entry(Point(3,2),3)
        input3.setText('10')
        input3.draw(win)
        
        p=win.getMouse()
        
        if sure.clicked(p):
            ww=eval(input1.getText())
            ll=eval(input2.getText())
            bb=eval(input3.getText())
            if bb<=ww*ll:
                self.win.close()
                self.__init__()
                self.size(ww,ll,bb,GraphWin('Mining',ww*30+90,ll*30+60))
                self.setbombbutton.activate()
                self.undobutton.activate()
                win.close()
    def setlevel(self,q):
        self.easybutton.activate()
        self.middlebutton.activate()
        self.hardbutton.activate()
        self.setbutton.activate()
        if self.easybutton.clicked(q):
            self.easy()
        elif self.middlebutton.clicked(q):
            self.middle()
        elif self.hardbutton.clicked(q):
            self.hard()
        elif self.setbutton.clicked(q):
            self.diy()
    def newgame(self):
        self.win.close()
        self.__init__()
        if self.width==9 and self.length==9:
            self.easy()
        elif self.width==9 and self.length==16:
            self.middle()
        else:
            self.hard()
    def start(self):
        self.size(9,9,10,GraphWin('sweepbomb',360,330))
        self.setbombbutton.activate()
        self.undobutton.activate()
    def setbomb(self,q):
        x=int(math.floor(q.getX()))
        y=int(math.floor(q.getY()))
        if [x,y] in self.all and self.state=='playing':   
            if [x,y] in self.mine:  
                self.minenum-=1    
                image=Image(Point(x*1.0+0.5,y*1.0+0.5),'bomb.gif')
                image.draw(self.win)
                self.usermark.push(image)
                self.all.remove([x,y])
                self.mark.push([x,y])
                self.sweptlist.append([x,y]) 
                self.labelnum.setText('mines:'+str(self.minenum))
                self.success()
            else:
                image=Image(Point(x*1.0+0.5,y*1.0+0.5),'bomb.gif')
                image.draw(self.win)
                self.usermark.push(image)
                self.all.remove([x,y])
                self.mark.push([x,y])
                self.sweptlist.append([x,y]) 
    def undo(self):
        if self.mark.mylist!=[]:
            a=self.mark.pop()
            self.all.append(a)
            self.sweptlist.remove(a)
            self.usermark.pop().undraw()
            self.minenum+=1
            self.labelnum.setText('mines:'+str(self.minenum))
    def firsthit(self,x,y): 
        if [x,y] in self.all:
            if [x,y] in self.mine:
                self.fail()
            else:
                self.state='begining'
                self.t=threading.Thread(target=self.counttime,args=(self.state,))
                self.t.start()
    def uncover(self,x,y):
        a=max(x-1,0)
        b=min(x+2,self.width)
        c=max(y-1,0)
        d=min(y+2,self.length)
        mark=0
        if self.state=='playing' and [x,y] in self.all:
            if [x,y] in self.mine:
                self.fail()
            else:
                self.all.remove([x,y])
                self.sweptlist.append([x,y])
                for i in range(a,b):
                    for j in range(c,d):
                        if [i,j] in self.mine:
                            mark+=1
                if mark!=0:
                    Text(Point(x*1.0+0.5,y*1.0+0.5),'%d'% mark).draw(self.win)
                    self.columnlist[x][y].setFill('white')
                    self.success()
                else:
                    self.columnlist[x][y].setFill('white')
                    for r in range(a,b):
                        for s in range(c,d):
                            if ([r,s] in self.sweptlist)==False:
                                self.uncover(r,s)
    def fail(self):
        self.setbombbutton.deactivate()
        self.undobutton.deactivate()
        win=GraphWin('Bomb!!!',400,400)
        win.setCoords(0,0,2,2)
        new=Button(win,Point(0.5,0.5),0.8,0.6,'New Game')
        quitbutton=Button(win,Point(1.5,0.5),0.8,0.6,'Quit')
        new.activate()
        quitbutton.activate()
        Text(Point(1,1.4),'You lose.Click "New Game" to continue,"Quit" to quit.').draw(win)
        p=win.getMouse()
        if quitbutton.clicked(p):
            win.close()
            self.win.close()
        if new.clicked(p):
            win.close()
            self.newgame()

            
    def success(self):      
        if self.minenum==0 and len(self.mark.mylist)==eval(self.bombnum):
            self.state=='win'
            win=GraphWin('Congratulations',300,300)
            win.setCoords(0,0,3,3)
            Text(Point(1.5,2.2),'You won!').draw(win)
            quitbutton=Button(win,Point(0.6,0.8),1.2,0.8,'Quit')
            new=Button(win,Point(2.4,0.8),1.2,0.8,'New Game')
            quitbutton.activate()
            new.activate()
            p=win.getMouse()
            if quitbutton.clicked(p):
                win.close()
                self.win.close()
            if new.clicked(p):
                win.close()
                self.win.close()
                self.newgame()
    def counttime(self,state):
        for i in range(1,1000):
            if self.state=='begin':
                self.timeused=i
                self.labeltime.setText('time:'+str(self.timeused))
                time.sleep(1)
    def qquit(self):
        self.win.close()
        

    
            
            

def main():
    base=Game()
    base.start()
    base.newgame()
    while True:
        pp=base.win.getMouse()
        if base.quitbutton.clicked(pp):
            base.qquit()
        elif base.newgamebutton.clicked(pp):
            qq=base.win.getMouse()
            base.setlevel(qq)
        elif base.undobutton.clicked(pp):
            base.undo()
        elif base.setbombbutton.clicked(pp):
            pp1=base.win.getMouse()
            base.setbomb(pp1)
        elif base.startbutton.clicked(pp):
            base.newgame()
        else:
            x=int(math.floor(pp.getX()))
            y=int(math.floor(pp.getY()))
            base.uncover(x,y)
            
main()
        

            
        
        










    

    
