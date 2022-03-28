#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: pluggy-example.py
@time: 2022/3/28 16:34
"""
from pluggy import HookspecMarker, HookimplMarker, PluginManager

spec = HookspecMarker("pluggy_demo_1")
impl = HookimplMarker("pluggy_demo_1")


class HookSpec:
    @spec
    def calculate(self, a, b):
        pass


class HookImpl1:
    @impl(tryfirst=True)
    def calculate(self, a, b):
        return a + b


class HookImpl2:
    @impl
    def calculate(self, a, b):
        return a * b


pm = PluginManager("pluggy_demo_1")
pm.add_hookspecs(HookSpec)
pm.register(HookImpl1())
pm.register(HookImpl2()) #
print(pm.hook.calculate(a=1, b=2))
# [3, 2]

# HookimplMarker 装饰器支持一些特定的参数
#
# tryfirst - 顾名思义就是这个 plugin 在 1:N 的执行链路中先执行
# trylast - 顾名思义后执行
# hookwrapper - 基于 yield 实现的一个wrapper，先执行 wrapper plugin 的一部分逻辑，
# 然后执行其他 plugin，最后执行剩余的 wrapper plugin 逻辑