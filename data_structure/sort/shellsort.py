#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/2/23 上午9:49
# @Author  : onion
# @Site    : 
# @File    : shell_sort.py
# @Software: PyCharm


def shell_sort(arr):
    D = len(arr) // 2
    count = 0
    while D > 0:  # 希尔增量序列
        for i in range(D, len(arr)):  # 插入排序的1 改成D
            tmp = arr[i]
            while i >= D and arr[i - D] > tmp:
                arr[i] = arr[i - D]
                i -= D
            arr[i] = tmp

        D //= 2
        count += 1
    print("排序次数: " + str(count))
    return arr


if __name__ == "__main__":
    l = [9, 3, 2, 8, 5, 7, 1]
    arr = [34, 8, 64, 51, 32, 31]
    print(shell_sort(arr))
