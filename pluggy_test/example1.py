#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/24 14:53
# software: PyCharm
import pluggy

hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


# pluggy.HookspecMarker()  钩子规格制造器
# pluggy.HookimplMarker()  钩子执行器
# pluggy.PluginManager()   插件管理器

class MySpec(object):
    """A hook specification namespace.
        添加一个规格
    """

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize."""


class Plugin_1(object):
    """A hook implementation namespace.
        做插件
    """

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin_2(object):
    """A 2nd hook implementation namespace."""

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2


def test():
    """
           1. 制作插件规格
           2. 添加执行 类
           3. 注册 真正执行的插件
           4. 调用
    """
    # create a manager and add the spec
    pm = pluggy.PluginManager("myproject")
    pm.add_hookspecs(MySpec)
    # register plugins 注册插件
    pm.register(Plugin_1())
    pm.register(Plugin_2())

    # call our `myhook` hook 调用
    results = pm.hook.myhook(arg1=1, arg2=2)
    print(results)
    # output
    # inside Plugin_2.myhook()
    # inside Plugin_1.myhook()
    # [-1, 3]


if __name__ == '__main__':
    test()
