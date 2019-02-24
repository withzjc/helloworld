#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : dequeue.py
# Author : cjz
# Date  : 2019-02-24 14:59

class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)