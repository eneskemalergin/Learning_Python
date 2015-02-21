"""
Created on Sat Feb 21 12:51:02 2015

@author: Enes Kemal Ergin

Snowflake 
"""

import turtle
import random

wn = turtle.Screen()
snow = turtle.Turtle()

wn.bgcolor("grey") # set the background color

snow.color("blue") # set turtle's color

colors = ["cyan", "purple", "white", "blue"]

for i in range(15):
    for j in range(2):
        snow.color(random.choice(colors))
        snow.forward(100)
        snow.right(60)
        snow.forward(100)
        snow.right(120)
    snow.right(36)
    
wn.exitonclick()