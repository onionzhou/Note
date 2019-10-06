#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/6 22:00
#  @Author  : onion
#  @Site    :
#  @File    : single_list.py
#  @Software: PyCharm


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next):
        self.next = new_next


class UnorderList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count = count + 1
            cur = cur.get_next()
        return count

    def search(self, item):
        cur = self.head
        found = False
        while cur != None and not found:
            if cur.get_data() == item:
                found = True
            else:
                cur = cur.get_next
        return found



    def remove(self, item):
        cur = self.head
        previous = None
        found = False

        while not found:
            if cur.get_data() == item:
                found = True
            else:
                '''必须先移动pre 到cur，再移动cur,<蠕动>'''
                previous = cur
                cur = cur.get_next()
        if previous != None:
            previous.set_next(cur.get_next)
        else:
            self.head = cur.get_next()
