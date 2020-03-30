#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2020/1/7 12:18
# software: PyCharm

from robot import  run

if __name__ == '__main__':
    # run('test.robot')

    #用于测试 testlibscope  作用范围的
    # run('test.robot','testlibscope.robot')

    # with open('stdout.txt', 'w') as stdout:
    #     run('test.robot', 'testlibscope.robot', name='Example', log=None, stdout=stdout)
    run('customkey.robot')