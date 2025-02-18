import time
import threading
from button import *
from graphics import *
def demo(demobutton,win2):
    if demobutton.activate():
        win2.setCoords(0.0,0.0,6.0,6.0)
        p1=Point(1.0,1.0)
        p1.draw(win2)
        label1=Text(Point(0.8,0.8),'p1')
        label1.draw(win2)
        time.sleep(1)
        p2=Point(4.0,4.0)
        p2.draw(win2)
        label2=Text(Point(4.2,4.2),'p2')
        label2.draw(win2)
        rec=Rectangle(p1,p2)
        rec.draw(win2)
        time.sleep(1)
        p3=Point(1.8,1.8)
        p3.draw(win2)
        label3=Text(Point(2.0,2.0),'p3')
        label3.draw(win2)
        rec1=Rectangle(Point(1.4,1.0),p3)
        rec1.draw(win2)
        time.sleep(1)
        p4=Point(3.6,3.6)
        p4.draw(win2)
        label4=Text(Point(3.8,3.8),'p4')
        label4.draw(win2)
        rec2=Rectangle(Point(3.2,3.2),p4)
        rec2.draw(win2)
        time.sleep(1)
        p5=Point(3.0,5.4)
        p5.draw(win2)
        label5=Text(Point(3.2,5.6),'p5')
        label5.draw(win2)
        py=Polygon(p5,p2,Point(1.0,4.0))
        py.draw(win2)
        Text(Point(3.0,0.5),'Understand?').draw(win2)
        Text(Point(3.0,0.5),'Understand?').undraw()
        time.sleep(1)
        Text(Point(3.0,0.5),'Click anywhere to return...').draw(win2)
        win2.getMouse()
        win2.close()
def display(demobutton,win2):
    t=threading.Thread(target=demo,args=(demobutton,win2))
    t.start()
def main():
    win=GraphWin('Draw a House',600,800)
    win.setCoords(0.0,-2.0,6.0,6.0)
    win2=GraphWin('How to draw a house.',600,800)
    demobutton=Button(win,Point(2.0,-1.0),1.8,1.2,'Demo')
    demobutton.activate()
    quitbutton=Button(win,Point(4.0,-1.0),1.8,1.2,'Quit')
    quitbutton.activate()
    while True:
        p=win.getMouse()
        if quitbutton.clicked(p):
            break
        elif demobutton.clicked(p):
            demobutton.deactivate()
            display(demobutton,win2)
        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)
        rec=Rectangle(p1,p2)
        rec.draw(win)
        p3=win.getMouse()
        p3.draw(win)
        rec1=Rectangle(p3,Point(p1.getX()+0.6*(p3.getX()-p1.getX()),pi.getY()))
        rec1.draw(win)
        p4=win.getMouse()
        p4.draw(win)
        rec2=Rectangle(p4,Point(p3.getX()+0.7*(p4.getX()-p3.getX()),p3.getY()+0.7*(p4.getY()-p3.getY())))
        rec2.draw(win)
        p5=win.getMouse()
        p5.draw(win)
        ppp=Polygon(p5,p2,Point(p1.getX(),p2.getY()))
        ppp.draw(win)
    win.close()
main()
    
    
    
        
        
        
        
    
