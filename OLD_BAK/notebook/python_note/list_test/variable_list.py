#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/11/7 10:12
# software: PyCharm

# 可变列表测试

class Bus:
    def __init__(self, passengers=[]):
        self.passengers = passengers
        print(id(self.passengers))

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


def test_bus():
    bus1 = Bus()
    bus2 = Bus()
    # 运算结果
    # 24955720
    # 24955720
    # bus1 和bus2 的self.passengers 的id 一样，说明他们共享了同一个列表
    # 说明了为啥用None 作为接受可变参数的默认值


class WorngBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
            print(id(self.passengers))
        else:
            self.passengers = passengers  # 此处没有新建列表
            print(id(self.passengers))

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)

    def get_passenger(self):
        return self.passengers


def test_worngbus():
    basketball = ['Tom', 'Tim', 'Jim', 'onion']

    bus = WorngBus(basketball)
    bus.drop('onion')
    print(bus.get_passenger())
    print(basketball)
    # 15585568
    # ['Tom', 'Tim', 'Jim']
    # ['Tom', 'Tim', 'Jim']
    # 篮球列表里的值也被移除了，因为WorngBus 里没有新建一个列表，使用的是basketball 的列表引用


class RightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
            print(id(self.passengers))
        else:
            self.passengers = list(passengers)
            print(id(self.passengers))

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


if __name__ == '__main__':
    test_worngbus()
