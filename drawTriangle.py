from turtle import*
from random import*

def drawTriangle(p):
    
    forward(p)
    up()
    left(120)
    down()
    forward(p)
    up()
    left(120)
    down()
    forward(p)
    done()
    
print(drawTriangle(100))