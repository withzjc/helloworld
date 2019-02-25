#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : node.py
# Author : cjz
# Date  : 2019-02-24 20:49
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.head = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,newdata):
        self.data = newdata

    def set_next(self,newnext):
        self.next = newnext

    def is_empty(self):
        return self.head ==None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != 0:
            count = count +1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current !=None and not found:
            if current.get_data() ==item:
                found =True
            else:
                current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data == item:
                found = True
            else:
                previous = current
                current =current.get_next()
        if previous ==None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self,item):
        pass



    def insert(self):
        pass

    def index(self):
        pass

    def pop(self):
        pass