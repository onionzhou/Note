#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/19 下午9:10
# @Author  : onion
# @Site    : 
# @File    : heappriorityqueue.py
# @Software: PyCharm

'''
堆实现的优先队列（数组形式）
'''


class Empty(Exception):
    pass


class PriorityQueueBase(object):
    class _item(object):
        __slots__ = ["_key", "_value"]

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []

    def _left_child(self, j):
        return 2 * j + 1

    def _right_child(self, j):
        return 2 * j + 2

    def _parent(self, j):
        return (j - 1) // 2

    def _has_left(self, j):
        return self._left_child(j) < len(self._data)

    def _has_right(self, j):
        return self._right_child(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # 插入元组向上冒泡
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    # 删除后，向下冒泡
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left_child(j)
            small_child = left

            if self._has_right(j):
                right = self._right_child(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty("priority queue is empty")
        tmp =self._data[0]
        return (tmp._key,tmp._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty("priority queue is empty")
        self._swap(0, len(self._data) - 1)
        tmp =self._data.pop()
        self._downheap(0)
        return (tmp._key,tmp._value)

if __name__ == "__main__":
    x =HeapPriorityQueue()
    x.add(2,"b")
    x.add(5,"c")
    x.add(1,"a")
    x.remove_min()
    print(x.min())