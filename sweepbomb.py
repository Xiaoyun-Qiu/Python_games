from graphics import *
from button import *
def main():
    win=GraphWin('sweep bombs',600,600)
    win.setCoords(0.0,-0.005,10.0,11.005)
    newgame=Button(win,Point(9.5,10.500),0.8,0.6,'New Game')
    newgame.activate()
    easy=Button(win,Point(9.5,9.500),0.8,0.6,'Easy')
    middle=Button(win,Point(9.5,8.500),0.8,0.6,'Middle')
    hard=Button(win,Point(9.5,7.500),0.8,0.6,'Hard')
    setlevel=Button(win,Point(9.5,6.500),0.8,0.6,'Set')
    setbomb=Button(win,Point(9.5,5.500),0.8,0.6,'SetBomb')
    start=Button(win,Point(9.5,4.500),0.8,0.6,'Start')
    time=Button(win,Point(9.5,3.500),0.8,0.6,'Time')
    bombnum=Button(win,Point(9.5,2.500),0.8,0.6,'BombNum')
    undo=Button(win,Point(9.5,1.500),0.8,0.6,'Undo')
    quitbutton=Button(win,Point(9.5,0.500),0.8,0.6,'Quit')
    for i in range(9):
        for j in range(9):
            rec=Rectangle(Point(j*1.0,i*1.000+1.000),Point(j*1.0+1.0,i*1.000+2.000))
            rec.draw(win)
main()
            
