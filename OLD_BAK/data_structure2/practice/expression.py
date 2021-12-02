#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/8 11:51
# software: PyCharm

from data_structure2.basic.my_tree import BinaryTree
from data_structure2.basic.stack import Stack

'''
将(7+3)*(5-2)，转换为一颗解析树
'''


# astring ='( 7 + 3 ) * ( 5 - 2 ) '
def build_parse_tree(asting):
    alist = asting.split()
    pstack = Stack()
    etree = BinaryTree('')
    pstack.push(etree)
    curtree = etree

    for i in alist:
        if i == '(':
            curtree.insert_left('')
            pstack.push(curtree)
            curtree = curtree.get_leftchild()
        elif i == ')':
            curtree = pstack.pop()
        elif i not in '+-*/':
            curtree.set_rootval(i)
            curtree = pstack.pop()  # 返回到父节点
        elif i in '+-*/':
            curtree.set_rootval(i)
            curtree.insert_right('')
            pstack.push(curtree)
            curtree = curtree.get_rightchild()
        else:
            raise ValueError('unknown oprator: {}'.format(i))

    return etree

import operator
def evaluate(parsetree):
    opers = {'+':operator.add,'-':operator.sub,
             '*':operator.mul,'/':operator.truediv}
    left= parsetree.get_leftchild()
    right = parsetree.get_rightchild()

    if left and right :
        fn = opers[parsetree.get_rootval()]
        return fn(evaluate(left),evaluate(right))
    else:
        return parsetree.get_rootval()

if __name__ == '__main__':
    astring='( 7 + 3 ) * ( 5 - 2 )'
    etree =build_parse_tree(astring)
    print(evaluate(etree))