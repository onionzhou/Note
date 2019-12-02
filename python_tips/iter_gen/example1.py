#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/11/26 11:06
# software: PyCharm


'''
问题1：反向迭代
 1. 对象拥有确定的大小 or  实现了__reversed__ 方法

如果都没有实现需要把对象转换成list
我们需要反向迭代序列中的元素
通过 reversed 内建函数实现

'''


def list_reversed(alist):
    for i in reversed(alist):
        print(i)


class Numrevesed():
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):  # 实现此方法，无需把数据放在列表中，再去反向列表
        print('反转')
        n = 1
        while n <= self.start:
            yield n
            n += 1


'''
问题2: 对迭代器做切片操作
迭代器和生成器无法向列表一样做切片，因为不知道他们的长度大小
使用itertool.islice(seq, [start,] stop [, step]) 
test code in test_iter.test_iter_lice()
'''


def my_count(n):
    while True:
        yield n
        n += 1


'''
问题3： 对某个迭代进行迭代处理，但是想丢弃掉前几个元素
itertools.dropwhile(pred, seq)

dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1

例如： 读取一个文件，跳过前面的注释 
test_iter.test_dropwhile()
'''

'''
问题4：在不同的容器中进行迭代
需要对许多个对象进行相同的操作，但是这些对象包含在不同的容器内，
而我们希望可以避免写重复的循环处理， 保证代码可读性

itertools.chain(*iterables)
a = [1,2,3]
b = [4,5,6]

for i in itertools.chain(a,b):
    print(i)    ----> 1,2,3,4,5,6 

'''

'''
问题5： 迭代元素在多个序列中，想同时对它们进行迭代

zip(a,b) 创建一个迭代器，产出元组(x,y) ,x from a , y from b ;
注意: 1.当某个序列没有元素时，停止迭代！！
      2. zip 只是一个迭代器，如果要保存数据，需要把他转换成list 
zip('ABCD','xy') ----> Ax  By

itertools.zip_longest()
	
zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

'''

'''
问题6 ：
将多个已排序的输入合并为一个已排序的输出
（例如，合并来自多个日志文件的带时间戳的条目

heapq.merge(*iterables, key=None, reverse=False) 

a =[1,4,10]
b=[2,3,7]

for c in heapq.merge(a,b):
    print(c)
'''