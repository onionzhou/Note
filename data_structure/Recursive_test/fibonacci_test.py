#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/1 20:30
# software: PyCharm
import time
#斐波那契数列 实现
#初始值 0 接着值1 然后后续的值是前两个值的总和
#0，1，1，2，3，5，8，13，21
#慢
def bad_fib(n):
    if n <= 1:
        return n
    else :
        return bad_fib(n-2) + bad_fib(n-1)
#快
def good_fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a,b) = good_fib(n-1)
        return (a+b,b)
#最快
#cache : {}
def cache_fib(n,cache):
    if n <= 1 :
        return n
    if n in cache:
        return cache[n]
    cache[n] = cache_fib(n-2,cache) + cache_fib(n-1,cache)
    return cache[n]
#生成器实现fib，递归有最大限制
def yield_fib(max):
    n =0
    a =0
    b =1
    while n <max:
        yield a
        a,b = b,a+b
        n +=1
def yield_fib_test():
    f = yield_fib(1000)
    for i in range(1000):
        print(next(f))
if __name__ =="__main__":
    cache = {}
    start_time =time.time()

    yield_fib_test()

    end_time =time.time()
    print(end_time-start_time)
    # print(fib_seq)