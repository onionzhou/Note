#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/24 16:43
# software: PyCharm

# getattr(object, name[, default])
#
# object -- 对象。
# name -- 字符串，对象属性。
# default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

# In [5]: class A:
#    ...:     bar=1
#    ...:
#
# In [6]: a=A()
#
# In [7]: getattr(a,'bar')
# Out[7]: 1
#
# In [8]: getattr(a,'bars')
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-8-85e5f579cc2e> in <module>
# ----> 1 getattr(a,'bars')
#
# AttributeError: 'A' object has no attribute 'bars'
#
# In [9]: getattr(a,'bars',False)        -----------!!!!!!
# Out[9]: False
#
# In [10]: getattr(a,'bar',False)
# Out[10]: 1

# __getattr__    只有类中没有该属性的时候才会触发
# __getattibute__  每次调用属性都会触发