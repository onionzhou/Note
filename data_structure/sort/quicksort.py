#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19/3/4 下午8:33
# @Author  : onion
# @Site    : 
# @File    : quicksort.py
# @Software: PyCharm


'''
实现1：
def quickSort(list):

    if len(list) < 2 :
        return list
    else:
        base = list[0] #基准条件

        base_left = [i for i in list[1:] if i<=base] #< 基准条件的子数组

        base_right = [i for i in list[1:] if i>base] #> 基准条件的子数组


        return quickSort(base_left) + [base] + quickSort(base_right)



def quick_sort_test1():
    #list = [3,5,22,3,1]
    list =[49,38,65,97,76,13,27,49]

    print(quickSort(list))
'''


# 快排实现2
def part(arr, left, right):
    pivot = arr[left]  # 基准

    while left < right:
        # 1.利用 arr[left]已保存在pivot，数组最左边第一个(arr[left])可以被覆盖
        # 然后可以先把数组右边的比主元大的数复制到数组左边，
        # 2.再把左边比主元大的数复制到，数组[right]中，交替覆盖，
        # 3.最后left < right ,说明指针已经到正中间，然后把pivot的值复制给中间，
        # 返回left,作为下一个子集划分的中间点，递归调用


        while left < right and arr[right] > pivot:
            right -= 1

        arr[left] = arr[right]

        while left < right and arr[left] <= pivot:
            left += 1

        arr[right] = arr[left]

    arr[left] = pivot
    return left
#快排实现3
#算法导论 170
#对子数组原址重排
def partion(arr, left, right):
    pivot = arr[right]
    i = left - 1
    #注意右边界问题，python中 right 其值取到 right-1
    for j in range(left, right):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    #print(arr)
    return i + 1


def _quick_sort(arr, left, right):
    if left < right:
        #pivot = part(arr, left, right)
        pivot = partion(arr, left, right)
        print(pivot)
        _quick_sort(arr, left, pivot - 1)
        _quick_sort(arr, pivot + 1, right)

    return arr


def quick_sort(arr):
    return _quick_sort(arr, 0, len(arr) - 1)


def quick_sort_test2():
    my_list = [49, 38, 65, 97, 76, 13, 27, 49]
    #my_list = [2, 8, 7, 1, 3, 5, 6, 4]
    print(quick_sort(my_list))


if __name__ == "__main__":
    quick_sort_test2()
