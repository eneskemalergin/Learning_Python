# -*- coding: cp1252 -*-
### Brief Explanation of Graphic Module in Python ###
'''
        We will introduce a module that allows us to create a data object called a
    turtle that can be used to draw pictures.
    
        '''
'''
# Turtles default direction is to east so if you want to make it go to west use
name.left(180) or 2 time name.left(90)

import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(150)           # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)
'''
'''
turtle is the name of module that we called in the first line of the actual code.
turtle.Screen() creates a graphics window
turtle.Turtle() creates our object Alex
then giving commands.
'''
# Different topic
'''
Each turtle has a color attribute.
The method invocation alex.color(“red”) will make alex red and the line
that it draws will be red too.
Different Attributes of the Turtle
'''

'''
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
'''
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)

