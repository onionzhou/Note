#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/17 上午9:54
# @Author  : onion
# @Site    : 
# @File    : linkedqueue.py
# @Software: PyCharm
'''
单链表实现队列
s.enqueue(i)  入队
s.dequeue()  出队
s.is_empty()
s.first()   是否为第一个
len(s)
'''


class Empty(Exception):
    pass


class LinkedQueue(object):
    class _Node(object):
        __slots__ = ['_data', '_next']

        def __init__(self, data):
            self._data = data
            self._next = None

    def __init__(self):
        '''创建空队列'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("queue is empty ")
        return self._head._data

    def enqueue(self, data):
        new_node = self._Node(data)
        if self.is_empty():
            self._head = new_node

        else:
            # 连接链表
            self._tail._next = new_node
        # 指针后移
        self._tail = new_node
        # self._tail = self._tail._next
        self._size += 1

    # 出队类似于栈的pop 操作，需要多维护一个尾指针
    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")

        data = self._head._data
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return data


if __name__ == "__main__":
    x = LinkedQueue()
    for i in range(1, 4):
        x.enqueue(i)
    print(x.first())
    print("出队{0},当前长度为{1}".format(x.dequeue(), len(x)))
    print("出队{0},当前长度为{1}".format(x.dequeue(), len(x)))
    print("出队{0},当前长度为{1}".format(x.dequeue(), len(x)))

    # print("出队{0},当前长度为{1}".format(x.dequeue(), len(x)))
