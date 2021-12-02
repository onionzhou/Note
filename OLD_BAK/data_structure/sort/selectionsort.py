#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/2/23 下午3:03
# @Author  : onion
# @Site    : 
# @File    : selectionsort.py
# @Software: PyCharm

def find_min(arr, min, ):
    for j in range(min, len(arr)):
        if arr[j] < arr[min]:
            min = j
    return min


def selection_sort(arr):
    for i in range(len(arr) - 1):
        # N = len(arr)
        # 从arr[i]到 arr[N-1] 中找到最小元，
        min = find_min(arr, i)
        # 将未排序的最小元，换到有序部分的最后位置
        arr[i], arr[min] = arr[min], arr[i]

    return arr


if __name__ == "__main__":
    arr = [34, 8, 64, 51, 32, 31]
    print(selection_sort(arr))
