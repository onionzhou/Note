#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/2/25 上午8:39
# @Author  : onion
# @Site    : 
# @File    : heapsort.py
# @Software: PyCharm

'''
index : 做操作的结点
heapsize:树有多少个结点
heapify 函数，注意点 1.不要越界 2.递归要有递归出口
'''
def heapify(arr, index, heapsize):
    if index >= heapsize:
        return
    #index 代表父节点
    left = 2 * index +1
    right = 2 * index + 2
    #假设最大值为index(父节点)
    maxvlaue = index

    #找最大值
    if (left < heapsize and arr[left] > arr[maxvlaue]):
        maxvlaue = left

    if (right < heapsize and arr[right] > arr[maxvlaue]):
        maxvlaue = right
    #做交换
    if maxvlaue != index:
        arr[index], arr[maxvlaue] = arr[maxvlaue], arr[index]
        heapify(arr, maxvlaue, heapsize)
    # print(arr)
'''
  heapzise: 树的结点数
'''
def build_max_heap(arr,heapsize):
    # 对于数组任一位置i上的元素，
    # 其左儿子在 [2i+1]上，右儿子在[2i+2]，父亲位于[(i-1)/2]
    last_node = heapsize - 1
    parent = (last_node -1 ) //2
    #range(2,-1,-1) --> i = [2,1,0]
    for i in range(parent,-1, -1):
        # print(i)
        heapify(arr, i, heapsize)

#for 循环递减  (n,n-1,...,1,0) 写法
#for i range(n,-1,-1)
def heap_sort(arr,n):
    build_max_heap(arr,n)
    for i in range(n-1 ,-1,-1):
        arr[0],arr[i] = arr[i],arr[0] #根结点和最后一个结点值
        heapify(arr,0,i)

if __name__ == "__main__":
    #此算法有问题待查
    arr = [4,10,3,5,1,2]
    arr1 = [2,5,3,1,6,7,8,10,4]
    arr2 = [2,5,3,1,10,4]
    # heapify(arr,0,6)
    # build_max_heap(arr2,len(arr2))
    heap_sort(arr2,len(arr2))
    print(arr2)