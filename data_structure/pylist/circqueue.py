#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/17 上午10:48
# @Author  : onion
# @Site    : 
# @File    : circqueue.py
# @Software: PyCharm
'''
链表实现循环队列
tips: 如果用数组实现循环队列，其核心是使用模运算，让最后一个位置
        变到第一个位置去
'''


class Empty(Exception):
    pass


class CircQueue(object):
    class _Node(object):
        __slots__ = ['_data', '_next']

        def __init__(self, data):
            self._data = data
            self._next = None

    # 循环队列中 head 可以用tail.next 来表示
    def __init__(self):
        '''创建空对列'''
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        '''返回队列第一个元素'''
        head = self._tail._next
        return  head.data

    def enqueue(self, data):
        new_node = self._Node(data)
        if self.is_empty():
            # self._tail = new_node
            new_node._next = new_node  # 一个元素自循环
        else:
            # 新节点的next指向 head
            new_node._next = self._tail._next
            # 旧的tail 指向 新添加的节点
            self._tail._next = new_node
        self._tail = new_node  # 新节点添加到队列尾部
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty ")
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            # 指针指向头节点的下一个地址,元素自动回收
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._data

if __name__ =="__main__":
    x = CircQueue()
    for i in range(4):
        x.enqueue(i)
