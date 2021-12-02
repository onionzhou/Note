#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/6 13:28
# software: PyCharm
from  data_structure2.basic.my_queue import Queue
from random import  randint
'''
传土豆游戏
接收一个名字列表 和一个用于计数的常亮num
程序将这个孩子的名字移出队列，然后立即将他插入队列得尾部,
随后该孩子会一直等待，直到再次达到队列得头部，在出队列和入队列num次后，
位于队列头部的孩子出局，如此反复，直到队列只剩下一个名字（队列大小为1）
'''


def hot_potato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for _ in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


if __name__ == '__main__':
    namelist=['a','b','c','d','e','f']
    num= randint(1,10)
    tmp =hot_potato(namelist,num)
    print(tmp)