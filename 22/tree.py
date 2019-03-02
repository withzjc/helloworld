#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : tree.py
# Author : cjz
# Date  : 2019-02-26 9:45
# import random
import turtle
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(21)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(19)
        t.backward(branchLen)
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
main()