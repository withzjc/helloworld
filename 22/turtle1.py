#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : turtle.py
# Author : cjz
# Date  : 2019-02-25 16:23
import turtle
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
    myTurtle.right(60)
    drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

    