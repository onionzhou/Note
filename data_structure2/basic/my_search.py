#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/7 11:15
#  @Author  : onion
#  @Site    :
#  @File    : my_search.py
#  @Software: PyCharm




def sequential_search(alist, item):
    '''顺序列表搜索
    '''
    pos = 0
    found = False
    while not found and pos < len(alist):
        if alist[0] == item:
            found = True
        else:
            pos = pos + 1

    return found


def bin_search(alist, item):
    ''' 有序列表的二分搜索 循环版本'''
    first = 0
    last = len(alist) - 1
    found = False

    while not found and first <= last: #注意点 first <= last 而不是first < last
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        elif item < alist[mid]: #区分 alist[mid] < item ,条件不同
            last = mid - 1
        else:
            first = mid + 1

    return found


def bin_search_recursive(alist, item):
    '''有序列表 的二分搜索 递归版本'''
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return bin_search_recursive(alist[:mid], item)
        else:
            return bin_search_recursive(alist[mid + 1:], item)


if __name__ == '__main__':
    alist = [3, 33, 44, 55, 56, 57, 555, 666]
    v = bin_search_recursive(alist, 666)
    # v = bin_search(alist, 56)
    print(v)
