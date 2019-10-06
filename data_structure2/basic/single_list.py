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

    '''
        新增 节点 26
            * 26 的next 指向 93
            * head 指向 26 
        head ---> [93|-]---->[66|-]--->[33|-] --->None
                    
             [26|-]--->None
    '''
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
        '''
        previous不为空 在中间， 空说明第一个节点就是要移除的节点
        A:移除列表中段节点
                                previous    cur
        head ---> [93 | -]----> [66 |-]---> [17|-]---> [33 |-]--->None
        
        B:移除链表第一个节点
        
        previous --->None
                    cur
        head ---> [93 | -]----> [66 |-]---> [17|-]---> [33 |-]--->None
            
        '''
        if previous != None:
            previous.set_next(cur.get_next)
        else:
            self.head = cur.get_next()
