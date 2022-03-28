#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: pytest-example.py
@time: 2022/3/28 16:22
"""
import pluggy
import pytest

def test_func(): # test开头的测试函数
    print("test_func")
    assert 1 # 断言成功

if __name__ == '__main__':
    pytest.main() # 执行测试