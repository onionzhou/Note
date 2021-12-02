#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: 3_p1.py
@time: 2020/8/27 11:02
"""
import socket
import os

## error ...

host ='10.0.80.1'

if os.name == 'nt':
    socket_protocol= socket.IPPROTO_IP
else:
    socket_protocol =socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW)

sniffer.bind((host,8888))
#设置捕获数据包中的IP头
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)


# 设置 IOCTL以启用混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

print(sniffer.recvfrom(65535))

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)