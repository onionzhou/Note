#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/7 14:02
#  @Author  : onion
#  @Site    :
#  @File    : my_sort.py
#  @Software: PyCharm

def bubble_sort(alist):
    '''冒泡 O(n²)'''
    for num in range(len(alist) - 1, 0, -1):
        for i in range(num):
            if alist[i] > alist[i + 1]: #大的在后面
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def short_bubblesort(alist):
    '''短冒泡，当发现是有序的序列就停止冒泡'''
    exchange = True
    num = len(alist) - 1
    while num > 0 and exchange:
        exchange = False
        for i in range(num):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        num = num - 1


def selection_sort(alist):
    '''选择排序 O(n²)，冒泡的改进款，改进如下
        每一轮遍历都选择待排序元素中最大的元素，将其放入在正确的位置
    '''
    for fillslot in range(len(alist) - 1, 0, -1):
        postion_max = 0
        for i in range(1, fillslot + 1):
            if alist[i] > alist[postion_max]:
                postion_max = i

        alist[fillslot], alist[postion_max] = alist[postion_max], alist[fillslot]


def insert_sort(alist):
    '''插入排序O(n²)
        列表低端 维护一个有序列表，并逐步将每个新元素"插入"这个子列表
        类似于打牌
    '''
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        postion = index
        while postion > 0 and alist[postion - 1] > currentvalue:
            alist[postion] = alist[postion - 1]
            postion = postion - 1
        alist[postion] = currentvalue


def gap_insert_sort(alist, start, gap):
    '''
    把插入排序的 1 改为希尔增量
    :param alist:
    :param start:
    :param gap: 希尔增量
    :return:
    '''
    for i in range(start + gap, len(alist), gap):
        curvalue = alist[i]
        postion = i

        while postion > gap and alist[postion - gap] > curvalue:
            alist[postion] = alist[postion - gap]
            postion = postion - gap

        alist[postion] = curvalue


def shell_sort(alist):
    '''希尔排序 O(n)-O(n²)之间,对插入排序的改进，将列表分成几个子列表，并
    对几个子列表进行插入排序
    如何切分列表是希尔排序的关键
    '''
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        # for startpostion in range(sublistcount):
        # gap_insert_sort(alist, startpostion, sublistcount)  # 把插入排序的 1 改为希尔增量
        for i in range(sublistcount, len(alist)):  # 插入排序的1 改成D
            tmp = alist[i]
            while i >= sublistcount and alist[i - sublistcount] > tmp:
                alist[i] = alist[i - sublistcount]
                i -= sublistcount
            alist[i] = tmp

        print("after increments of size {},the list is {}".format(sublistcount, alist))
        sublistcount = sublistcount // 2


def merge_sort(alist):
    '''归并排序 拆 O(logn) 合 O(n),总时间复杂度为O(nlogn)
    递归算法,每次将列表一分为二，如果列表为空或者只有一个元素
    从定义上说它就是有序的
    归并：将两个较小的有序列表归并为一个有序列表的过程
    '''
    print('splitting ', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        # 合并列表
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        # 处理列表奇数的情况
        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1

        print('merging ', alist)


def partion(alist, first, last):
    pivot = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and \
                        alist[leftmark] <= pivot:
            leftmark = leftmark + 1

        while rightmark >= leftmark and \
                        alist[rightmark] >= pivot:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


def _quick_sort(alist, first, last):
    if first < last:
        splitpoint = partion(alist, first, last)
        print(splitpoint)
        _quick_sort(alist, first, splitpoint - 1)
        _quick_sort(alist, splitpoint + 1, last)


def quick_sort(alist):
    '''快速排序
    分治策略，不使用额外的存储空间，代价是 列表不会一分为2
    算法效率会有所下降
    1.选基准点，作为分割点
    2.分为左右两边， 左边小于基准点右边大于基准点
    O(nlogn) ，快速排序不会像归并哪样使用额外的存储空间
    如果分割点不在列表中端，导致分隔不均匀，会导致时间复杂度变为O(n²)
    三位数取中可以避免切分不均匀
    '''
    _quick_sort(alist, 0, len(alist) - 1)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # insert_sort(alist)
    # shell_sort(alist)
    # merge_sort(alist)
    # quick_sort(alist)
    bubble_sort(alist)
    print(alist)
