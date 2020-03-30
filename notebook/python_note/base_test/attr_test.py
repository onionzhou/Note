#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/24 16:18
# software: PyCharm

# attr  库测试
import attr


# 在一个类中 定义一个类来接收属性
class C:
    @attr.s  # 类装饰器
    class D:
        x = attr.ib()  # 把 接收的属性传给 X
        y = attr.ib()

    def __init__(self, instance_obj):
        self.obj_D = instance_obj  # 实例化的对象 instance_obj = D()

    def get_x(self):
        return self.obj_D.x


def test():
    s = C.D(2, 'w')
    print(s.x)
    # output 2


def test1():
    s = C(instance_obj=C.D(2, 'w'))
    print(s.get_x())
    # output 2


if __name__ == '__main__':
    test1()
