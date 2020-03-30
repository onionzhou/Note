#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2020/1/6 17:32
# software: PyCharm

class Custom:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        print('test robot call python value={} '.format(self.value))


# Test library scope 测试
# TEST CASE   每个实例都会创建一次
# TEST SUITE  一个test suite 创建一次
# GLOBAL      执行一次测试创建一次
class ExampleLibary:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._counter = 0

    def mycount(self):
        self._counter += 1
        print(self._counter)

    def clear_counter(self):
        self._counter = 0


class MyLibary:
    def my_keyword(self, arg):
        return self._helper_method(arg)

    def _helper_method(self, arg):
        return arg.upper()



#######################################
from robot.api.deco import keyword
@keyword('say')
def hello(username):
    print('{} say :hello world '.format(username))
