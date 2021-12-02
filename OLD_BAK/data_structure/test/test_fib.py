#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/11/23 10:20
#  @Author  : onion
#  @Site    :
#  @File    : test_fib.py
#  @Software: PyCharm
import sys
sys.path.append('../../')
from data_structure.Recursive_test.fibonacci_test import *
import pytest


class Testfib():
    @classmethod
    def setup_class(cls):
        print('类执行前')

    @classmethod
    def teardown_class(cls):
        print('类执行后')

    def test_fib_bottom_up_return_type(self):
        result = fib_bottom_up(5)
        assert isinstance(result, int)

    def test_fib_bottom_up_boundary(self):
        # 边界值测试
        result = fib_bottom_up(1)
        assert result == 1

    def test_fib_except(self):
        # 异常测试
        with pytest.raises(ValueError):
            fib_bottom_up(0)
        with pytest.raises(TypeError):
            fib_bottom_up(0.1)

    def test_fib_except2(self):
        print('test_fib_except2')
        with pytest.raises(ValueError, match='参数最小为1') as info:
            fib_bottom_up(0)

    @pytest.mark.xfail(raises=ValueError)
    def test_fib_except3(self):

        fib_bottom_up(0)

    def test_fib_except4(self):
        # 异常处理判断异常信息
        print('test_fib_except4')
        with pytest.raises(ValueError) as excinfo:
            fib_bottom_up(0)
        assert '参数最d' in str(excinfo.value)


if __name__ == '__main__':
    pytest.main(['-q', 'test_fib.py::Testfib::test_fib_except4'])
