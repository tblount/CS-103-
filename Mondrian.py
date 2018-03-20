
from turtle import *
from random import *

def mondrian(ref = (0,0), w = 100, spacing = 25):
    
    speed(0)
    vertLine(ref,w,spacing)
    horiLine(ref,w,spacing)
    blueBox(ref,w,color)
    mondPic(ref,w,color)
    
def vertLine(ref,w,spacing):
    for i in range(10):
        down()
        left(200)
        goto(w + 25)
        done()

def horiLine(ref,w,spacing):
    for i in range(10):
        down()
        forward(200)
        goto(w + 25)
        done()
        
def blueBox(ref,w,color):
    
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(w)
        left(90)
    end_fill()
    done()
    
def mondPic(ref,w,color):
    
    color = 'blue'
    setpos(ref)
    vertLine(ref,spacing)
    horiLine(ref,spacing)
    for i in range(7):
        blueBox(ref,w,color)
    horiLine(ref + 25)
    
mondrian((0,0)100,10)
    

    
    