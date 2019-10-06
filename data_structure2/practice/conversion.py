#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/5 10:26
# software: PyCharm

from  data_structure2.basic.stack import Stack

'''将十进制转换为二进制
'''
def divide_by_2(decnumber):
    s = Stack()

    while decnumber > 0:
        rem = decnumber % 2
        s.push(rem)
        decnumber = decnumber // 2

    binstr = ''
    while not s.is_empty():
        binstr = binstr + str(s.pop())

    return binstr


'''将十进制数转换为任意进制数
'''
def base_converter(decnumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while decnumber > 0:
        rem = decnumber % base
        s.push(rem)
        decnumber = decnumber // base

    newstr = ''
    while not s.is_empty():
        newstr = newstr + digits[s.pop()]

    return newstr


