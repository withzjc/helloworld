#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : palchecker.py
# Author : cjz
# Date  : 2019-02-24 15:04
from dequeue import Dequeue

def palchecker (aString):
    chardequeue = Dequeue()
    for ch in aString:
        chardequeue.addRear(ch)
    stillEqual = True
    while chardequeue.size()>1 and stillEqual:
        first = chardequeue.removeFront()
        last = chardequeue.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
print(palchecker('lsdjiasdjasdjaskd'))
print(palchecker('上海自来水来自海上'))
