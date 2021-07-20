#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: 4.py
@time: 2020/11/19 10:28
"""
from datetime import datetime
import os
import time
import psutil
import subprocess

if __name__ == '__main__':

    while True:
        now_time = datetime.now().strftime('%Y%m%d%H%M%S')
        with open('time.txt', 'w+') as f:
            print('现在的时间是：\n' + now_time, file=f)

        proc = subprocess.Popen(['notepad', 'time.txt'])
        pid = proc.pid
        print(pid)
        time.sleep(1)

        # ret = os.system('%s%s' % ("taskkill /F /IM ", name))
        ret = os.system('%s%s' % ("taskkill /pid ", pid))
        time.sleep(1)
