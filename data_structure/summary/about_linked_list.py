#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/22 20:30
# software: PyCharm

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
# 链表逆序
def reverse(head):
    if head ==None or head.next ==None:
        return
    # pre =cur =nex = None
    cur_node= head.next
    next_node = cur_node.next
    cur_node.next = None  #把第一个节点的下个结点置空，

    pre_node =cur_node    #指针右移
    cur_node =next_node   #指针右移

    while cur_node.next !=None:
        next_node =cur_node.next
        cur_node.next =pre_node    #链表反转
        pre_node =cur_node         #指针右移
        cur_node =next_node        #指针右移

    cur_node.next =pre_node     #最后一个结点，手动反转
    head.next =cur_node    #head下个结点指向最后一个结点
#链表逆序插入
#从链表的第二个结点，把遍历的结点插入到头结点的后面
#head->1->2->3->4
#head->2->1->3->4
#head->3->2->1->4
def reverse_by_insert(head):
    cur_node = head.next.next
    head.next.next =None

    while cur_node is not None:
        next_node = cur_node.next
        cur_node.next = head.next
        head.next =cur_node
        cur_node = next_node

def create_node(n):
    i = 1
    head = Node()
    head.next = None
    # tmp = None
    cur = head
    while i < n:
        tmp =Node()
        tmp.data =i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i+=1
    return head

def traversal(head):
    cur = head.next
    while cur != None:
        print(cur.data, end=" ")
        cur = cur.next


def main():

    head =create_node(5)
    print("逆序前.... ")
    traversal(head)
    print("\n逆序后....")
    # reverse(head)
    reverse_by_insert(head)
    traversal(head)



if __name__ == '__main__':
    main()
