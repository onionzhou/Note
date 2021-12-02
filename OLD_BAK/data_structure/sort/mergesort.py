#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/2/26 下午9:07
# @Author  : onion
# @Site    : 
# @File    : mergesort.py
# @Software: PyCharm

'''
分而治之
归并排序
'''
def merge_sort_1(left_arr, right_arr):
    li = 0  # left index
    ri = 0
    result = []

    while li < len(left_arr) and ri < len(right_arr):
        if left_arr[li] < right_arr[ri]:
            result.append(left_arr[li])
            li += 1
        else:
            result.append(right_arr[ri])
            ri += 1

    if li < len(left_arr):
        result += left_arr[li:]
    if ri < len(right_arr):
        result += right_arr[ri:]

    return result

def merge_sort_2(left_arr, right_arr):
    li = 0  # left index
    ri = 0
    result = []

    while li < len(left_arr) and ri < len(right_arr):
        # 判断调节 < =  保持稳定性，而不是 <
        if left_arr[li] <= right_arr[ri]:
            result.append(left_arr.pop(li))
            li += 1
        else:
            result.append(right_arr.pop(ri))
            ri += 1

    result += left_arr
    result += right_arr

    return result


# 递归
def merge_recursive(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_recursive(arr[:mid])
    right = merge_recursive(arr[mid:])

    return merge_sort_2(left, right)



'''
有序子序列的归并
L：左边的起始位置
R:右边的起始位置
rightend:右边的终点位置
'''
def sub_merge(arr, tmparr, L, R, rightend):
    # tmparr = []
    leftend = R - 1

    while (L <= leftend and R <= rightend):
        if arr[L] <= arr[R]:
            tmparr.append(arr[L])
            L += 1
        else:
            tmparr.append(arr[R])
            R += 1

    # 实现1
    while L <= leftend:
        tmparr.append(arr[L])
        L += 1

    '''
    #实现2
    if L <= leftend:
        for i in range(L,leftend+1):
            tmparr.append(arr[i])
    #实现3
    if L <= leftend:
        for i in arr[L:leftend+1]:
            tmparr.append(i)
    '''
    while R <= rightend:
        tmparr.append(arr[R])
        R += 1
    # print(tmparr)
    return tmparr

def merge_sort(arr):
    mid =len(arr)//2
    end =len(arr)-1
    tmparr =[]
    return sub_merge(arr,tmparr,0,mid,end)
    # return merge_recursive(arr)

if __name__ == "__main__":
    arr = [1, 13, 24, 30, 2, 15, 27, 28, 29]
    arr2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    tmparr =[]
    # print(sub_merge(arr,tmparr,0,4,8))
    print(merge_sort(arr))
    # print(merge_recursive(arr2))
