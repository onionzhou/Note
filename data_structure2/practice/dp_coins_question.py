#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 10:38
# @Author  : onion
# @Site    : 
# @File    : dp_coins_question.py
# @Software: PyCharm

def dp_makechange(coin_list,change,mincoins,coinused):
    '''
    :param coin_list: 硬币的面值列表,list
    :param change: 找零的金额 int
    :param mincoins: 找零金额0-change 的所有最优解,list
    :param coinused :记录所用的硬币
    :return: 最少的硬币数
    '''
    for cents in range(change+1):
        coincount = cents
        newcoin  = 1
        for j in [c for c in coin_list if c <= cents]:
            if mincoins[cents-j] +1 < coincount:
                coincount = mincoins[cents-j] +1
                newcoin=j

        mincoins[cents] =coincount
        coinused[cents] =newcoin
    return mincoins[change]

def print_coins(coinused,change):
    coin = change
    while coin >0 :
        thiscoin = coinused[coin]
        print(thiscoin)
        coin = coin -thiscoin


if __name__ == '__main__':
    c1 =[1,5,10,21,25]
    coinused = [0]*64
    coincount= [0]*64
    dp_makechange(c1,63,coincount,coinused)
    print_coins(coinused,63)
