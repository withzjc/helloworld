#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : stack.py
# Author : cjz
# Date  : 2019-02-25 15:25
from Stack2 import Stack
r_stack = Stack()
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.isEmpty():
        res = res + str(r_stack.pop())
    return res
print(to_str(1499, 2))
