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


class BinaryMinHeap(object):
    '''二叉堆实现优先队列
    队列得重要变体，
    从头部移除元素，不过元素的逻辑顺序由优先级决定，
    优先级最高的在前面，低的在后面
    优先队列实现经典方法是二叉堆，
    二叉堆 入队出队 O(logn)
    最小堆：最小元素一直在队首  parent < child
    最大堆：最大元素一直在队首

    '''

    def __init__(self):
        ''' 位于 p 节点，左子节点为 2p ,右节点为 2p+1
                     5
                    /  \
                   9    11
                  / \   / \
                14  18 19
        vaule|  0 5 9 11 14 19
        index   0 1 2  3  4  5

        '''
        self.heaplist = [0]  # 使后续的方法能使用整数除法
        self.currentsize = 0

    def perc_up(self, i):
        while i // 2 > 0:  # 父节点的下标就是当前节点的下标除以2
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = \
                    self.heaplist[i // 2], self.heaplist[i]
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentsize += 1
        self.perc_up(self.currentsize)

    def find_min(self):
        return self.heaplist[1]

    def min_child(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2  # 左孩子
            else:
                return i * 2 + 1  # 右孩子

    def perc_down(self, i):
        '''删除后向下'''
        while (i * 2) <= self.currentsize:
            mc = self.min_child(i)  # 一层一层的向下移
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def del_min(self):
        '''
        难点：移除节点后，如何重建堆得结构和有序性
        1.取出列表的最后一个元素，移动到根节点，保证堆得结构
        2. 新的根节点沿着树推到正确的位置，重获堆得有序性
        :return:
        '''
        ret = self.heaplist[1]  # heaplist[0] 我们是没有使用的
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize -= 1
        self.heaplist.pop()
        self.perc_down(1)
        return ret

    def is_empty(self):
        pass

    def size(self):
        return self.currentsize

    def build_heap(self, alist):
        ''''''
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1

if __name__ == '__main__':
    alist = [9,5,6,2,3]
    s = BinaryMinHeap()
    s.build_heap(alist)
    print(s.del_min())
    print(s.heaplist)