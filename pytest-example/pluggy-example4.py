#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: pluggy-example.py
@time: 2022/3/28 16:34
"""
from pluggy import HookspecMarker, HookimplMarker, PluginManager

spec = HookspecMarker("plugin_demo_2")
impl = HookimplMarker("plugin_demo_2")
pm = PluginManager("plugin_demo_2")


# ookspckMarker装饰器也支持一些参数，主要是
#
# firstresult - 获取第一个plugin 执行结果后就中断后续执行
# historic - 表示这个 hook 是需要保存call history 的，当有新的 plugin 注册的时候，需要回放历史


class Spec:
    @spec
    # @spec(firstresult=True)
    def calculate(self, a, b):
        pass


class Impl1:
    @impl
    def calculate(self, a, b):
        return a + b


class Impl2:
    @impl(tryfirst=True)
    def calculate(self, a, b):
        return a + b + 2


class ImplWrapper:
    @impl(hookwrapper=True)
    def calculate(self, a, b):
        print("before logic")
        outcome = yield
        print("Get Result %s" % outcome.result)
        return a * b * 10


pm.add_hookspecs(Spec)
pm.register(Impl1())
pm.register(Impl2())
pm.register(ImplWrapper())
print(pm.hook.calculate(a=1, b=2))




# before logic
# Get Result [5, 3]
# [5, 3]


# ImplWrapper 是一个类似 coroutine的 生成器，它有两段逻辑，用outcome = yield来分割
# outcome 通过 yield来获取，它是_Result对象，包含了非wrapper 的 plugin 的执行结果，
# 这里就是 Impl1 和 Impl2，从实际的output来看，Get Result [5,3]就是获取了返回值
# wrapper plugin 的返回值是会被 ignore 的，具体的原因下次分析源码的时候会给解释
#