# More Advance Function Examples #
#--------------------------------#

#Taking square bu addition...
def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)

# Functions can call other Functions:
'''
        It is important to understand that each of the functions we write
    can be used and called from other functions we write.
    This is one of the most important ways that computer scientists take
    a large problem and break it down into a group of smaller problems.
    This process of breaking a problem into smaller subproblems is
    called functional decomposition.
'''

# Sum of squares of 3 numbers.
def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a + b + c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)

# This illustrates an important computer science problem solving technique called generalization. 
# draw rectangle
'''
import turtle
def drawRectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

'''
import turtle

def drawRectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawSquare(tx, sz):        # a new version of drawSquare
    drawRectangle(tx, sz, sz)

wn = turtle.Screen()             # Set up the window
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess

drawSquare(tess, 50)

wn.exitonclick()
