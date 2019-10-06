#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/6 13:09
# software: PyCharm

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''尾部添加一个元素，无返回值
        '''
        self.items.insert(0, item)

    def dequeue(self):
        '''
        队列头部移除一个元素，
        :return:
        '''
        return self.items.pop()

    def is_empty(self):
        '''
        判断队列是否为空，返回一个 bool
        :return:
        '''
        return self.items == []

    def size(self):
        '''
        返回队列里元素的数目，返回一个int
        :return:
        '''
        return len(self.items)
