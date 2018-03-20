# 103 Johnstone UAB Fall 2016

from turtle import *

'''
  If are running on an Apple, don't let the warnings about deprecated features
  bother you.  This is a corollary of Apple's fight with Tcl/Tk.
  Turtle geometry works just fine regardless.

  To explore turtle geometry commands, see the Python documentation, such as
  https://docs.python.org/3.1/library/turtle.html#turtle.home
  https://docs.python.org/3.1/library/turtle.html#turtle.color
'''

def drawTriangle (T):

    """Draw the boundary of a triangle in the present color.

    Params: T (tuple) tuple of 3 points in 2-space
    """

    penup ()
    goto (T[0])  # using motion to absolute Cartesian coords, like this,
    pendown ()   # rather than relative motions (e.g., 'forward'), 
    goto (T[1])  # often adds clarity; have no fear that we are violating
    goto (T[2])  # Dijkstra's cardinal rule; see his famous paper at:
    goto (T[0])  # http://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf
    penup()      # he was referring to a different goto

def drawFilledTriangle (T):

    """Draw a filled triangle in the present colors.

    Params: T (tuple) tuple of 3 points in 2-space
    """

    begin_fill()
    drawTriangle (T)
    end_fill()

home ()
hideturtle ()                  # be discreet and hide the turtle
color ('red', 'yellow')        # challenge: change this to UAB colors
                               # hints:
                               # - switch to RGB mode using 'colormode(255)'
                               # - call 'color' w. RGB tuples, not strings
                               # - RGB of UAB green is (30, 107, 82)
                               # - RGB of UAB gold is (244, 195, 0)
T = ((0,0), (300,0), (0,300))  # nice, a right triangle, my favourite sort
drawFilledTriangle (T)
# drawTriangle (T)             # try me! (first comment out the previous line)
done()                         # hold on a second, let me admire you

