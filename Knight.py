from graphics import *
from button import *
from stack import *
import math
def main():
    win=GraphWin('Tic-Tac-Toe',640,720)
    win.setCoords(0.0,-1.0,8.0,8.0)
    rowlist=[]
    for i in range(8):
        columnlist=[]
        for j in range(8):
            rec=Rectangle(Point(j*1.0,i*1.0),Point(1.0+j*1.0,1.0+i*1.0))
            rec.draw(win)
            columnlist.append(rec)
        rowlist.append(columnlist)
    for i in range(0,8,2):
        for j in range(1,8,2):
            rowlist[i][j].setFill('lightgrey')
    for i in range(1,8,2):
        for j in range(0,8,2):
            rowlist[i][j].setFill('lightgrey')
    undobutton=Button(win,Point(3.0,-0.5),1.6,0.8,'Roll Back')
    undobutton.deactivate()
    quitbutton=Button(win,Point(5.0,-0.5),1.6,0.8,'Quit')
    quitbutton.activate()
    knightfoot=Stack()
    whiteknight=Stack()
    q1=win.getMouse()
    if quitbutton.clicked(q1):
        win.close()
    else:
        x1=math.floor(q1.getX())
        y1=math.floor(q1.getY())
        image1=Image(Point(x1+0.5,y1+0.5),'2.gif')
        image1.draw(win)
        knightfoot.push(image1)
    q2=win.getMouse()
    if quitbutton.clicked(q2):
        win.close()
    else:
        x2=math.floor(q2.getX())
        y2=math.floor(q2.getY())
        if abs(x1-x2)==2.0 and abs(y1-y2)==1.0 or abs(x1-x2)==1.0 and abs(y1-y2)==2.0:
            image2=Image(Point(x2+0.5,y2+0.5),'2.gif')
            knightfoot.item(-1).undraw()
            a=image1.getAnchor()
            whiteknight.push(Image(a,'1.gif'))
            whiteknight.item(-1).draw(win)
            image2.draw(win)
            knightfoot.push(image2)
            undobutton.activate()
        else:
            pass
    while True:
        p=win.getMouse()
        if quitbutton.clicked(p):
            break
        elif undobutton.clicked(p):
            knightfoot.pop().undraw()
            whiteknight.pop().undraw()
            knightfoot.item(-1).draw(win)
        else:
            x=math.floor(p.getX())
            y=math.floor(p.getY())
            pp=knightfoot.item(-1).getAnchor()
            if abs(pp.getX()-0.5-x)==2.0 and abs(pp.getY()-0.5-y)==1.0 or abs(pp.getX()-0.5-x)==1.0 and abs(pp.getY()-0.5-y)==2.0:
                image=Image(Point(x+0.5,y+0.5),'2.gif')
                knightfoot.item(-1).undraw()
                aa=knightfoot.item(-1).getAnchor()
                whiteknight.push(Image(aa,'1.gif'))
                whiteknight.item(-1).draw(win)
                image.draw(win)
                knightfoot.push(image)
            else:
                pass
    win.close()
main()
            
            
            
        
        
            
            
    
