#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/14 下午8:55
# @Author  : onion
# @Site    : 
# @File    : single_list.py
# @Software: PyCharm
class Node(object):
    def __init__(self, data=None):
        self._data = data
        self._next = None


class SingleList(object):
    def __init__(self):
        self._head = Node()
        self._tail = self._head


    '''头插'''

    def add_head(self, e):
        new_node = Node(e)
        new_node._next = self._head
        self._head = new_node

    '''尾插'''

    def add_tail(self, e):
        new_node = Node(e)
        self._tail._next = new_node
        self._tail = new_node


    '''是否为空'''

    def is_empty(self):
        return self._head == None

    def get_head(self):
        if not self.is_empty():
            return self._head

    '''遍历'''

    def traversal(self,head=None):

        tmp = []
        if head is None:
            cur = self._head
        else :
            cur = head

        if self.is_empty():
            print('list is empty')
            return

        while cur != None:
            tmp.append(cur._data)
            cur = cur._next
        return tmp

    def remove_list(self):
        if not self.is_empty():
            while self._head != None:
                self._head = self._head._next


if __name__ == "__main__":
    x = SingleList()
    for i in range(8):
        x.add_head(i)
        # x.add_tail(i)
    print(x.traversal())
    x.remove_list()
    print("===")
    print(x.traversal())


