#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : ro_word.py
# Author : cjz
# Date  : 2019-02-25 15:16
#尝试用python判断回文字符串
while True:
    str=input("please input a string:")#输入一个字符串
    length=len(str)#求字符串长度
    left=0#定义左右‘指针’
    right=length-1
    while left<=right:#判断
        if str[left].upper()==str[right].upper():
            left+=1
            right-=1
        else:
            break;
    if left>right:
        print("yes")
    else :
        print("no")