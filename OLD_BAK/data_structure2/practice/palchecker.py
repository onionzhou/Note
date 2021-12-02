#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/6 14:09
# software: PyCharm

from data_structure2.basic.my_deque import Deque

'''
回文检测器,
分别从左和右边pop一个字符串来比较，回文是相等的，
'''


def palchecker(astring):
    chardeque = Deque()
    for i in astring:
        chardeque.add_front(i)

    stillequal = True

    while chardeque.size() > 1 and stillequal:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()

        if first != last:
            stillequal = False

    return stillequal

if __name__ == '__main__':
    s = 'assdddsa'
    print(palchecker(s))