#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/2/25 上午8:39
# @Author  : onion
# @Site    : 
# @File    : heapsort.py
# @Software: PyCharm

def maxheap(arr, index, heapsize):
    left = 2 * index
    right = 2 * index + 1
    maxvlaue = index

    if (left < heapsize and arr[left] > arr[maxvlaue]):
        maxvlaue = left

    if (right < heapsize and arr[right] > arr[maxvlaue]):
        maxvlaue = right

    if maxvlaue != index:
        arr[index], arr[maxvlaue] = arr[maxvlaue], arr[index]
        maxheap(arr, maxvlaue, heapsize)


def build_max_heap(arr):
    # 对于数组任一位置i上的元素，
    # 其左儿子在 [2i]上，右儿子在[2i+1]，父亲位于[i/2]
    idx = len(arr) // 2
    for i in range(idx, 0, -1):
        maxheap(arr, i, len(arr))



def heap_sort(arr):
    build_max_heap(arr)
    for i in range(len(arr)-1 ,1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        maxheap(arr,0,i)

    return  arr


if __name__ == "__main__":
    #此算法有问题待查
    arr = [31,41,59,26,53,58,97]
    print(heap_sort(arr))