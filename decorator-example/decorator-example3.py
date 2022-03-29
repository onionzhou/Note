#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: decorator-example1.py
@time: 2022/3/29 10:14
"""


class Decorator:
    def __init__(self, arg1, arg2):
        print('执行类Decorator的__init__()方法')
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, f):
        print('执行类Decorator的__call__()方法')

        def wrap(*args):
            print('执行wrap()')
            print('装饰器参数：', self.arg1, self.arg2)
            print('执行' + f.__name__ + '()')
            f(*args)
            print(f.__name__ + '()执行完毕')

        return wrap


@Decorator('Hello', 'World')
def example(a1, a2, a3):
    print('传入example()的参数：', a1, a2, a3)


if __name__ == '__main__':
    print('装饰完毕')
    example('Wish', 'Happy', 'EveryDay')
    print('测试代码执行完毕')

    '''
    
    执行类Decorator的__init__()方法
    执行类Decorator的__call__()方法
    装饰完毕
    执行wrap()
    装饰器参数： Hello World
    执行example()
    传入example()的参数：Wish Happy EveryDay
    example()执行完毕
    测试代码执行完毕
    
    @Decorator('Hello', 'World')实际上生成了一个类Decorator的对象
    ，然后该对象作为装饰器修饰example()函数，修饰过程就是调用了Decorator对象的__call__()方法来“封装”exmaple()
    ，最后example()函数的实际上是闭包后，__call__()方法中定义的wrap()函数。
    
    '''

