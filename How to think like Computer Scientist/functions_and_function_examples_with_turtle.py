# -*- coding: cp1252 -*-
# Functions #

'''
In Python, a function is a named sequence of statements that belong together.
'''


#The syntax for a function definition is:
'''
def name( parameters ):
    statements

'''
# Function Definitions
'''
    Function definitions are the second of several compound
statements we will see, all of which have the same pattern:
    1. A header line which begins with a keyword and ends with a colon.
    2. A body consisting of one or more Python statements, each indented the same amount
– 4 spaces is the Python standard – from the header line.
'''
#Drawing square function 
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()              # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # create alex
drawSquare(alex, 50)             # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()
######################################################################3
# Draw two squares...
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex
drawSquare(alex, 50)          # Call the function to draw the square

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex,75)           # Draw another square

wn.exitonclick()

########################################################################
# Draw Horizontal multi Squares.
import turtle

def drawMulticolorSquare(t, sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.speed(50)
tess.pensize(3)

size = 20                        # size of the smallest square
for i in range(15):
    drawMulticolorSquare(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()























