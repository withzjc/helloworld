#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : to_str.py
# Author : cjz
# Date  : 2019-02-25 15:06

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n / base, base) + convert_string[n % base]
print(to_str(140, 16))