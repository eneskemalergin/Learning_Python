# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 13:03:49 2015

@author: Enes Kemal Ergin

Snowflake creator 
"""
import turtle
import random

wn = turtle.Screen()
snow = turtle.Turtle()

wn.bgcolor("grey")
snow.color("blue")

def branch():
    for i in range(3):
        for j in range(3):
            snow.forward(30)
            snow.backward(30)
            snow.right(45)
        snow.left(90)
        snow.backward(30)
        snow.left(45)
    snow.right(90)
    snow.forward(90)

for i in range(8):
    branch() 
    snow.left(45)
    
wn.exitonclick()