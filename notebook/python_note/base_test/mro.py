#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/12 11:44
# software: PyCharm

class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super(B,self).__init__()


class C(A):
    def __init__(self):
        print('C')
        super(C,self).__init__()


class D(A):
    def __init__(self):
        print('D')
        super(D,self).__init__()


class E(B, C):
    def __init__(self):
        print('E')
        super(E,self).__init__()


class F(C, D):
    def __init__(self):
        print('F')
        super(F,self).__init__()


class G(E, F):
    def __init__(self):
        print('G')
        super(G,self).__init__()


if __name__ == '__main__':
    g= G()
    print(G.__mro__)
    # G E B F C D A

