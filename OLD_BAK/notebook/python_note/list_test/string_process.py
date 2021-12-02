#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/11/19 10:43
# software: PyCharm

# 字符串反转
# 前 和 尾 交换 指针 往中间移动

def str_reversal(astr):
    alist = list(astr)
    start = 0
    last = len(alist) - 1
    while start < last:
        tmp = alist[start]
        alist[start] = alist[last]
        alist[last] = tmp

        start = start + 1
        last = last - 1

    bstr = ''.join(alist)
    return bstr


def test():
    a = 'abcdefggh'
    result = str_reversal(a)
    print(result)


# 给定一个字符串，输出他的全排列
# abc --->  abc acb  bac bca cab cba
def str_permutation(astr):
    alist = list(astr)
    list_permutation(alist, 0)


def swap(alist, i, j):
    if i == j:
        return
    tmp = alist[i]
    alist[i] = alist[j]
    alist[j] = tmp


def list_permutation(alist, index):
    # print('alist --> {},{}'.format(alist,id(alist)))
    if alist == None or index < 0:
        return
    # 打印字符串
    if index == len(alist) - 1:
        print(''.join(alist), end=' ')
    else:
        i = index
        while i < len(alist):
            swap(alist, index, i)  # 交换
            list_permutation(alist, index + 1)
            swap(alist, index, i)  # 还原字符串
            i = i + 1


def test1():
    a = 'abc'
    str_permutation(a)


# 判断字符串是不是换位字符： 相同的字符串组成就是换位字符
# 1.构建一个字符串列表，初始化全为0
# 2.遍历a 字符串，将字符对应的ascll 嘛作为下标，对应数组加1
# 3.遍历b 字符串，将对应的数组元素值，减1
# 4. 遍历该列表，全为0 ， 是换位字符
def is_transposition_str(astr1, astr2):
    ascll_list = [0] * 256

    index = 0
    init_ascll = ord('0')

    alist1 = list(astr1)
    alist2 = list(astr2)
    while index < len(alist1):
        ascll_list[ord(alist1[index]) - init_ascll] += 1
        index = index + 1

    index = 0
    while index < len(alist2):
        ascll_list[ord(alist2[index]) - init_ascll] -= 1
        index = index + 1

    index = 0
    while index < 256:
        if ascll_list[index] != 0:
            return False
        index = index + 1
    return True


def test2():
    a = 'aaaabbbcc'
    b = 'abbaaacbca'
    result = is_transposition_str(a, b)
    print(result)


if __name__ == '__main__':
    # test()
    # test1()
    test2()
