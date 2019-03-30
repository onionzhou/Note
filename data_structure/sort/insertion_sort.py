#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insertion_sort(arr):
    # 从第一张牌开始插，不从0开始，代表手里有一张牌

    for i in range(1, len(arr)):
        tmp = arr[i]  # 摸牌
        while (i > 0 and arr[i - 1] > tmp):  # 手里的牌比摸牌大
            arr[i] = arr[i - 1]  # 往后移
            i -= 1
        arr[i] = tmp  # 新牌位置

    return arr
'''
for 循环
void insertion_sort(elementType arr[],int  N)
    for (p =1 ,p<N,p++)
        tmp = arr[p]
        for (i =p,i >0 && arr[i-1] > tmp,i--)
            arr[i] =arr[i-1]
        arr[i] =tmp
'''

if __name__ == "__main__":
    l = [9, 3, 2, 8, 5, 7, 1]
    arr = [34, 8, 64, 51, 32, 31]
    print(insertion_sort(arr))

