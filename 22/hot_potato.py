#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : hot_potato.py
# Author : cjz
# Date  : 2019-02-24 10:52
from queue import Queue

def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

        return simqueue.dequeue()

print(hotPotato(['David','Naruto','Sasuka','Sakura','Tom','Bob','Smith'],5))
