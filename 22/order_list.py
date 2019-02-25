#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : order_list.py
# Author : cjz
# Date  : 2019-02-25 10:39
from node import Node

class order_list:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            if current.get_data() > item:
                return False
            else:
                current = current.get_next()
        return False

    def add(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() > item:
                break
            previous = current
            current = current.get_next()
        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
