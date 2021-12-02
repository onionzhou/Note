#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/2 7:17
# software: PyCharm

import sys
#python 中列表长度和底层数组大小关系
def test_list_len(n):
    data = []
    for i in range(n):
        a=len(data)
        b=sys.getsizeof(data)
        print("len: {0:3d};Size in bytes {1:4d}".format(a,b))
        data.append(None)
if __name__ == "__main__":
    test_list_len(30)