#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 2:51 PM
# @Author  : onion
# @Site    : 
# @File    : chain_test.py
# @Software: PyCharm

from  itertools import chain


def f1(x):
    return x + 1


func_list = [f1,lambda x: x-1]

def f2(x):
    return  x+2

#执行chain 拼接列表里的值，这里是拼接函数
# 将3个函数添加在一个列表中

l1 = [1,3,5]
l2 =[2,4,6]


if __name__ == '__main__':
    new_func_list = chain([f2], func_list)
    for func in new_func_list:
        print(func)

    l3 =chain(l1,l2)
    for item  in l3 :
        print(item)

