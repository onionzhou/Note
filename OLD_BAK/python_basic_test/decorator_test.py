#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/17 20:26
# software: PyCharm

import time


# ===============================================
# 装饰器实现 by 闭包
def w1(func):
    def inner():
        # 操作1
        # 操作2
        func()

    return inner


@w1
def f1():
    pass


# f1 = w1(f1)
# ===============================================
# 装饰器叠放
def make_test2(func):
    def wrapped():
        print("make test2")
        func()

    return wrapped


def make_test1(func):
    def wrapped():
        print("make test1")
        func()

    return wrapped


@make_test2
@make_test1
def test_func():
    print("hello world")


# test_func = make_test2(make_test1(test_func))

# ====================================================
# 无参数的装饰器
def time_no_args(func):
    def wrapfunc():
        print("time_no_args")
        print("{} called at {}".format(func.__name__, time.ctime()))
        func()

    return wrapfunc


@time_no_args
def func1():
    print("I am  func1 use time_no_args decorator")


# ====================================================
def time_with_args(func):
    def wrapfunc(a, b):
        print("time_with_args")
        print(a, b)
        print("{} called at {}".format(func.__name__, time.ctime()))
        func(a, b)

    return wrapfunc


@time_with_args
def func2(a, b):
    print("a+b ={}".format(a + b))


# ===================================
# 带不定长参数
def time_with_variable_args(func):
    def wrapfunc(*args, **kwargs):
        print("time_with_variable_args")
        print(args)
        print(kwargs)
        print("{} called at {}".format(func.__name__, time.ctime()))
        return func(*args, **kwargs)

    return wrapfunc


@time_with_variable_args
def func3(*args, **kwargs):
    # print("a+b+c = {}".format(a+b+c))
    print(func3.__name__)


# ==============================
# 装饰器带return
def time_with_return(func):
    def wrapfunc():
        return "now time is {}-----> {}".format(time.ctime(), func())

    return wrapfunc


@time_with_return
def func4():
    return "hello world"


# =============================================
def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "China":
                print("你好!")
            elif contry == "America":
                print('hello.')
            else:
                return
            # 真正执行函数的地方
            return func(*args, **kwargs)
        return deco
    return wrapper

#装饰器带参数
@say_hello('China')
def chinese():
    print('i am chinese')
    return 1


if __name__ == '__main__':
    # test_func()
    # func1()
    # func2(2,1)
    # func3(2,3)
    # print(func4())
    a = chinese()
    print(a)
