#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/2 10:19
# software: PyCharm

'''
链表逆序
head ->1 ->2->3->4->5
逆序后
head ->5->4->3->2->1
'''

from data_structure.pylist.single_list import SingleList
def reverse(head):
    #do something
    return head


def test():
    x = SingleList()
    for i in range(8):
        x.add_head(i)
    print(x.traversal())
    head  = x.get_head()
    reverse(head)
    print(x.traversal(head))

if __name__ == "__main__":
    test()