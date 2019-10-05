#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/5 8:49
# software: PyCharm
'''
添加和删除总发生在同一端
特点： 插入顺序与移除顺序正好相反
'''

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        '''将一个元素添加到栈的顶端'''
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        '''返回栈顶元素，但不移除该元素'''
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
