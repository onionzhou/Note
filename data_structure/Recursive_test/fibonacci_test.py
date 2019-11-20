#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/1 20:30
# software: PyCharm
import time
import functools


# 斐波那契数列 实现
# 初始值 0 接着值1 然后后续的值是前两个值的总和
# 0，1，1，2，3，5，8，13，21

@functools.lru_cache()  # python 自带的缓存装饰器
def bad_to_cache_fib(n):
    if n <= 1:
        return n
    else:
        return bad_fib(n - 2) + bad_fib(n - 1)


# 慢
# @functools.lru_cache()  #python 自带的缓存装饰器
def bad_fib(n):
    if n <= 1:
        return n
    else:
        return bad_fib(n - 2) + bad_fib(n - 1)


# 快
def good_fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fib(n - 1)
        return (a + b, b)


# 最快
# cache : {}
def cache_fib(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = cache_fib(n - 2, cache) + cache_fib(n - 1, cache)
    return cache[n]


# 生成器实现fib，递归有最大限制
def yield_fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield a
        a, b = b, a + b
        n += 1


def yield_fib_test():
    f = yield_fib(1000)
    for i in range(1000):
        print(next(f))


#
def fib(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result


# 此处缓存使用的 list，上面使用的dict 递归有最大限制
def fib_memo(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


# dp求解思路 fib
# 1.递归 2.存储memo  3. bottom_up
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


if __name__ == "__main__":
    cache = {}
    start_time = time.time()
    # bad_to_cache_fib(200)
    # yield_fib_test()
    print(fib_bottom_up(1000))
    end_time = time.time()
    print(end_time - start_time)
    # print(fib_seq)
