from graphics import *
class Button:
    "(win,centerpoint,length,height,label)"
    def __init__(self,win,centerpoint,length,height,label):
        l,h=length/2.0,height/2.0
        x,y=centerpoint.getX(),centerpoint.getY()
        self.xmin,self.xmax=x-l,x+l
        self.ymin,self.ymax=y-h,y+h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)
        self.label=Text(centerpoint,label)
        self.label.draw(win)
        self.deactivate()
    def clicked(self,point):
        if self.active and self.xmin<=point.getX() and point.getX()<=self.xmax and self.ymin<=point.getY() and point.getY()<=self.ymax:
            return True
        else:
            return False
    def getLabel(self):
        return self.label.getText()
    def activate(self):
        self.rect.setWidth(2)
        self.label.setFill('black')
        self.active=True
    def deactivate(self):
        self.rect.setWidth(1)
        self.label.setFill('darkgrey')
        self.active=False
        
        
        
        
        
