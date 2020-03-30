#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 21:03
# @Author  : onion
# @Site    : 
# @File    : py_winlib_test.py
# @Software: PyCharm
import win32api
import os

def test_exce_app():
    #it is Ok
    #ShellExecute(hwnd, op , file , params , dir , bShow )
    win32api.ShellExecute(0,
                          'open',
                          'E:\\mysoftware\\xshell_person\\Xshell.exe','','',
                          1)

def exce_app_by_os():
    #it is ok
    os.system('start E:\\mysoftware\\xshell_person\\Xshell.exe')

import win32gui

hwnd_title = {}

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

def test_get_window():
    '''
    找到 文件句柄，获取活动的句柄
    :return:
    '''
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        # if t :
            #526980 Xshell 6 (Free for Home/School)
            # print (h, t)
        if 'Xshell' in t:
        # if t:
            print(h,t)

def find_app_handle():
    '''
        通过名字找句柄
    :return:
    '''
    app_name ='Xshell 6 (Free for Home/School)'
    hwnd = win32gui.FindWindow(None,app_name)
    print(hwnd)




if __name__ == '__main__':
    # test_exce_app()
    # exce_app_by_os()
    test_get_window()
    # find_app_handle()