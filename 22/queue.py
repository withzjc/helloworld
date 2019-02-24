#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : queue.py
# Author : cjz
# Date  : 2019-02-24 10:42
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items ==[]

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('dog')
q.enqueue(45)
q.enqueue('hasagi')
q.enqueue(['dog'])
print(q.size())