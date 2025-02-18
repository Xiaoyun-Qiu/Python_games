from graphics import *
class Card:
    def __init__(self,win,filename,center):
        self.image=Image(center,filename)
        self.win=win
        self.x=center.getX()
        self.y=center.getY()
    def drawCard(self):
        self.image.draw(self.win)
    def undrawCard(self):
        self.image.undraw()
    def moveCard(self,dx,dy):
        self.image.move(dx,dy)
        self.x +=dx
        self.y +=dy
        
