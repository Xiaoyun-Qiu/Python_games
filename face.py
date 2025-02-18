from graphics import *
import time
class Face:
    def __init__(self,win,center,size): 
        eyesize=0.2*size
        eyeOff=size/2.0
        self.eyeOff=eyeOff
        mouthSize=0.8*size
        mouthOff=size/2.0
        self.mouthOff=mouthOff
        self.head=Circle(center,size)
        self.head.draw(win)
        self.headx=self.head.getCenter().getX()
        self.heady=self.head.getCenter().getY()
        self.lefteye=Circle(center,eyesize)
        self.lefteye.move(-eyeOff,eyeOff)
        self.lefteye.draw(win)
        self.righteye=Circle(center,eyesize)
        self.righteye.move(eyeOff,eyeOff)
        self.righteye.draw(win)
        p1=center.clone()
        p2=center.clone()
        p1.move(-mouthOff,-mouthOff)
        p2.move(mouthOff,-mouthOff)
        self.mouth=Line(p1,p2)
        self.mouth.draw(win)
        pm=center.clone()
        pm.move(0.0,-mouthOff)
        self.lefteyeOff=Line(p1,pm)
        self.lefteyeOff.move(-0.8*eyeOff,mouthOff)
        self.lefteyeOff.move(0.0,eyeOff)
        self.righteyeOff=Line(pm,p2)
        self.righteyeOff.move(0.8*eyeOff,mouthOff)
        self.righteyeOff.move(0.0,eyeOff)
        self.win=win
        self.center=center
    def eyeblink(self):
        self.lefteye.undraw()
        self.righteye.undraw()
        self.lefteyeOff.draw(self.win)
        self.righteyeOff.draw(self.win)
        time.sleep(1)
        self.lefteyeOff.undraw()
        self.righteyeOff.undraw()
        self.lefteye.draw(self.win)
        self.righteye.draw(self.win)
    def turn(self):
        if self.mouth.getCenter().getY()<=self.center.getY():
            self.mouth.move(0,2*self.mouthOff)
            self.lefteye.move(0,-2*self.eyeOff)
            self.righteye.move(0,-2*self.eyeOff)
        else:
            self.mouth.move(0,-2*self.mouthOff)
            self.lefteye.move(0,2*self.eyeOff)
            self.righteye.move(0,2*self.eyeOff)
    def left(self):
        self.head.move(-0.2,0.0)
        self.lefteye.move(-0.2,0.0)
        self.righteye.move(-0.2,0.0)
        self.mouth.move(-0.2,0.0)
        self.lefteyeOff.move(-0.2,0.0)
        self.righteyeOff.move(-0.2,0.0)
        self.center.move(-0.2,0.0)
        self.headx=self.headx-0.2
    def right(self):
        self.head.move(0.2,0.0)
        self.lefteye.move(0.2,0.0)
        self.righteye.move(0.2,0.0)
        self.mouth.move(0.2,0.0)
        self.lefteyeOff.move(0.2,0.0)
        self.righteyeOff.move(0.2,0.0)
        self.center.move(0.2,0.0)
        self.headx=self.headx+0.2
    def up(self):
        self.head.move(0.0,0.2)
        self.lefteye.move(0.0,0.2)
        self.righteye.move(0.0,0.2)
        self.mouth.move(0.0,0.2)
        self.lefteyeOff.move(0.0,0.2)
        self.righteyeOff.move(0.0,0.2)
        self.center.move(0.0,0.2)
        self.heady=self.heady+0.2
    def down(self):
        self.head.move(0.0,-0.2)
        self.lefteye.move(0.0,-0.2)
        self.righteye.move(0.0,-0.2)
        self.mouth.move(0.0,-0.2)
        self.lefteyeOff.move(0.0,-0.2)
        self.righteyeOff.move(0.0,-0.2)
        self.center.move(0.0,-0.2)
        self.heady=self.heady-0.2
    def Getx(self):
        return self.headx
    def Gety(self):
        return self.heady
    def Move(self,dx,dy):
        self.head.move(dx,dy)
        self.lefteye.move(dx,dy)
        self.righteye.move(dx,dy)
        self.mouth.move(dx,dy)
        self.lefteyeOff.move(dx,dy)
        self.righteyeOff.move(dx,dy)
        self.center.move(dx,dy)
        
        
        
            
    
        
    
        
        
        
        
