#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: check_host_alive.py
@time: 2020/8/21 15:46
"""
import subprocess

'''
    仅仅应用于Linux 下使用 
'''

def call_ping(ip):
    ret = subprocess.call(['ping', '-c', '2', ip], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    if ret == 0:
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreachable".format(ip))

def main():
    from concurrent.futures import ThreadPoolExecutor
    thread_pool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
    ip_list = []
    with open('ip_list', 'r') as f:
        for ip in f:
            ip_list.append(ip.strip())
    for ip in ip_list:
        thread_pool.submit(call_ping, ip)
    thread_pool.shutdown()
    print('main process end')


if __name__ == '__main__':
    main()
