#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/18 下午8:50
# @Author  : onion
# @Site    : 
# @File    : doublylinkedqueue.py
# @Software: PyCharm

'''
双端队列 链表是实现
'''


class Empty(Exception):
    pass


class _DoublyLinkedBase(object):
    class _Node(object):
        __slots__ = ['_data', '_next', '_pre']

        def __init__(self, data=None, pre=None, next=None, ):
            self._data = data
            self._next = next
            self._pre = pre

    # 初始化头哨兵和尾哨兵
    def __init__(self):
        self._header = self._Node()
        self._tailer = self._Node()
        self._header._next = self._tailer
        self._tailer._pre = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert(self, data, pre, next):
        new_node = self._Node(data, pre, next)
        # new_node.pre = self._header
        # new_node.next = self._tailer
        pre._next = new_node
        next._pre = new_node
        self._size += 1

        return new_node

    def _delete_node(self, node):
        pre_node = node._pre
        back_node = node._next

        back_node._pre = pre_node
        pre_node._next = back_node

        self._size -= 1
        del_data = node._data
        # 帮助python 进行垃圾回收
        node._pre = node._next = node._data = None

        return del_data


class LinkedQueue(_DoublyLinkedBase):
    def first(self):
        '''返回队列第一个元素，不会移除元素'''
        if self.is_empty():
            raise Empty("the queue is empty ")
        return self._header._next._data

    def last(self):
        '''返回队列最后一个元素，不会移除元素'''
        if self.is_empty():
            raise Empty("the queue is empty ")
        return self._tailer._pre._data

    def add_first(self, data):
        self._insert(data, self._header, self._header._next)

    def add_last(self,data):
        self._insert(data,self._tailer._pre,self._tailer)

    def del_first(self):
        if self.is_empty():
            raise Empty("the queue is empty ")
        return self._delete_node(self._header._next)

    def del_last(self):
        if self.is_empty():
            raise Empty("the queue is empty ")
        return self._delete_node(self._tailer._pre)

if __name__ =="__main__":
    x = LinkedQueue()
    #  3 2 1 4 5 6
    x.add_first(1)
    x.add_first(2)
    x.add_first(3)
    x.add_last(4)
    x.add_last(5)
    x.add_last(6)
    print(len(x))

    print("first data {} ,last data {}".format(x.first(),x.last()))
    x.del_last()

    print("first data {} ,last data {}".format(x.first(), x.last()))
    x.del_first()
    print("first data {} ,last data {}".format(x.first(), x.last()))
    x.del_first()
    print("first data {} ,last data {}".format(x.first(), x.last()))
    x.del_first()
    print("first data {} ,last data {}".format(x.first(), x.last()))
    x.del_first()
    print("first data {} ,last data {}".format(x.first(), x.last()))
    x.del_first()
    #x.del_last()
    #print("first data {} ,last data {}".format(x.first(), x.last()))

    print(len(x))
