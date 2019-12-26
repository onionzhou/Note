#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/26 16:06
# software: PyCharm
import pluggy

hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


class MySpec(object):
    """A hook specification namespace."""

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize."""


class Plugin_1(object):
    """A hook implementation namespace."""

    @hookimpl(tryfirst=True) #尝试最先执行
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin_2(object):
    """A 2nd hook implementation namespace."""

    @hookimpl(trylast=True) #尝试最后执行
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2

class Plugin_4(object):
    """A 2nd hook implementation namespace."""

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_4.myhook()")
        return arg1 * arg2

class Plugin_3(object):
    '''
    使用了 hookwrapper =True
    以yield 为分隔线
    yield  之前的代码 在使用了@hookimpl 的函数之前调用
    yield  之后的代码在使用了 @hookimpl 的函数之后调用
    '''
    @hookimpl(hookwrapper=True)
    def myhook(self, arg1, arg2):
        print("inside Plugin_3.myhook()")
        print('do something first ')
        x =yield
        print('do something after x={}'.format(x.get_result()))
        return  arg1 *arg2

# create a manager and add the spec
pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)
# register plugins
pm.register(Plugin_1())
pm.register(Plugin_2())
pm.register(Plugin_3())
pm.register(Plugin_4())

# call our `myhook` hook
results = pm.hook.myhook(arg1=1, arg2=2)
print(results)

# output:
# inside Plugin_3.myhook()
# do something first
# inside Plugin_1.myhook()
# inside Plugin_4.myhook()
# inside Plugin_2.myhook()
# do something after x=[3, 2, -1]
# [3, 2, -1]