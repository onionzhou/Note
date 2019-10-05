#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/5 9:06
# software: PyCharm
'''
括号匹配
左括号必须跟右括号相对应
'''
from data_structure2.basic.stack import Stack


def par_checker(symbolStr):
    '''
        小括号匹配
        遇到左括号就压栈，遇到右括号就出栈，
        如果栈中任意一个左括号找不到右括号，balacne = Flase
        处理完括号匹配，栈应该为空
    '''
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolStr) and balance:
        symbol = symbolStr[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                s.pop()
        index = index + 1
    if balance and s.is_empty():
        return True
    else:
        return False


def matches(left, right):
    lefts = '([{'
    rights = ')]}'
    return lefts.index(left) == rights.index(right)


def par_checker1(symbolStr):
    '''
        匹配符号 [({ })]
    '''
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolStr) and balance:
        symbol = symbolStr[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        index = index + 1
    if balance and s.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    sym = '{[()]}}'
    p = par_checker1(sym)
    print(p)
