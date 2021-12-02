#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/16 上午7:17
# @Author  : onion
# @Site    : 
# @File    : linkedstack.py
# @Software: PyCharm

'''单链表实现栈
    s.push(i)    O(1)
    s.pop()      O(1)
    s.top()      O(1)
    s.is_empty   O(1)
    len(s)       O(1)
'''

class Empty(Exception):
    pass
class DataException(Exception):
    pass

class _Node(object):
    __slots__ = ["_data","_next"]
    def __init__(self, data):
        self._data = data
        self._next = None


class LinkedStack(object):
    def __init__(self):
        ''' 创建空栈'''
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,data):
        if not isinstance(data,(int,float)):
            raise DataException("data is not int or float")
        new_code =_Node(data)
        new_code._next = self._head
        self._head = new_code
        self._size += 1


    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        data = self._head._data
        self._head = self._head._next
        self._size -= 1
        return data


    def top(self):
        '''是否为栈顶'''
        if self.is_empty():
            raise Empty("stack is empty ")
        return self._head._data

if __name__ == "__main__":
    x =LinkedStack()
    for i in range(0,9):
       x.push(i)

    print(len(x))
    print(x.top())
    print(x.pop())
    print(x.top())



