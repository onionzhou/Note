#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/17 10:41
# software: PyCharm

class MyExcept(Exception):
    pass

#通过抛异常跳出循环
def test():
    try :
        for i in range(100):
            for  j in range(i):
                if j*2 == 86 :
                    raise MyExcept(j)
    except MyExcept as ae:
        print("catch myexcept j=={}".format(ae))
    else:
        print('no catch')
    finally:
        print('end')
    # output ：
    # catch myexcept j == 43
    # end

if __name__ == '__main__':
    test()