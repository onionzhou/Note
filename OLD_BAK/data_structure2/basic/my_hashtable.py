#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/7 11:44
#  @Author  : onion
#  @Site    :
#  @File    : my_hashtable.py
#  @Software: PyCharm

'''
散列 构建一个时间复杂度为 O(1)的数据结构

散列表元素的集合，其每个位置称为槽
散列函数将散列表中的元素与其所在位置相对应起来 key value
载荷因子 λ = 元素个数/散列表大小

冲突： 散列函数将两个 元素放入同一个槽中

完美散列函数：
    每个元素映射到不同的槽
如何构造完美散列函数：
    1.增大散列表 --->缺点浪费极大的内存空间
    2.折叠法: 先将元素切成等长的
        436-555-4601 ， 以2位位一组切分--> 43 65 55 46 01
        将数字叠加 为 210， 假设散列槽有11个，(210%11=1)取余为1  ，将其放在1号槽中
    3.平方区中法:先将元素取平方,再提取中间几位数
        44 --->44² = 1936 ， 取中间两位 93， （93%11=5），将其放在5号位


处理冲突：
    1.开放定址法/线性探测： 从初始散列表开始，顺序遍历散列表，直到找到一个空槽。
        为了遍历散列表，可能需要往回探测第一个槽 ----该过程称为 开放定址法
        由于挨个访问 ----这个做法叫 线性探测
        缺点：散列表出现聚集现象

    避免聚集 ---->扩展的线性探测 --->加‘3’

    再散列：
        newhashvalue =  rehash(oldhashvalue)
        rehash(pos) = (pos +1 )% sizeoftable
        加3 探测 策略 可定义为  rehash(pos) = (pos+3)%sizeoftable
        ---->
            再散列的函数定义： rehash(pos) =(pos+skip)%sizeoftable
            跨步(skip) 的大小要能保证表中所有的槽全部都能访问的到--->建议散列表使用素数

    2.平方探测：线性探测的变体，不采用固定的跨步大小，通过再散列函数递增散列值
        如果第一个散列值为h  后续的 h+1 h+4 h+9 h+16

'''


class Hashtable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashvalue = self.hash_function(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value  # 替换原有的值
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def get(self, key):
        startslot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        positon = startslot

        while self.slots[positon] != None and \
                not found and not stop:
            if self.slots[positon] == key:
                found = True
                data = self.data[positon]
            else:
                positon = self.rehash(positon, len(self.slots))
                if positon == startslot:
                    stop = True
        return data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

if __name__ == '__main__':
    h = Hashtable()
    h[54] = 'qqq'

    print(h.data,h.slots)
    print(h[54])