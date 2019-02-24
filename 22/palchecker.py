#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : palchecker.py
# Author : cjz
# Date  : 2019-02-24 15:04
from dequeue import Dequeue

def pal_checker (aString):
    char_dequeue = Dequeue()
    for ch in aString:
        char_dequeue.addRear(ch)
    stillEqual = True
    while char_dequeue.size()>1 and stillEqual:
        first = char_dequeue.removeFront()
        last = char_dequeue.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
print(pal_checker('lsdjiasdjasdjaskd'))
print(pal_checker('上海自来水来自海上'))
