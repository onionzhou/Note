#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/6 13:55
# software: PyCharm

'''
双端队列: 某种意义上是栈和队列得结合
'''


class Deque(object):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        '''元素添加在双端队列得前面'''
        self.items.append(item)

    def add_rear(self, item):
        '''元素添加在双端队列得后面'''
        self.items.insert(0, item)

    def remove_front(self):
        '''从双端队列得前端移除，返回一个元素'''
        return self.items.pop()

    def remove_rear(self):
        '''从双端队列得后端移除，返回一个元素'''
        return self.items.pop(0)

    def is_empty(self):
        '''检查队列是否为空，返回一个bool'''
        return self.items == []

    def size(self):
        '''返回队列中的元素数目，返回一个int'''
        return len(self.items)
