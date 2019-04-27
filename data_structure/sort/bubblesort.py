#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubble_sort(arr):
    for j in range(len(arr) - 1):
        flag = 0
        # 一趟冒泡
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                # python 交换两个数
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = 1
        # 如果一趟排序没有交换说明序列有序跳出循环
        if 0 == flag:
            break
    return arr


if __name__ == "__main__":
    arr = [3, 2, 8, 4, 1]
    print(bubble_sort(arr))

