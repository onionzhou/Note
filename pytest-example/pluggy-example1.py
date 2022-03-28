#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: pluggy-example.py
@time: 2022/3/28 16:34
hook 与 plugin 的关系
"""
from pluggy import HookspecMarker, HookimplMarker, PluginManager

spec = HookspecMarker("pluggy_demo_1")
impl = HookimplMarker("pluggy_demo_1")


class HookSpec:
    @spec
    def calculate(self, a, b):
        pass


class HookImpl1:
    @impl
    def calculate(self, a, b):
        return a + b


class HookImpl2:
    @impl
    def calculate(self, a, b):
        return a * b


pm = PluginManager("pluggy_demo_1")
pm.add_hookspecs(HookSpec)
pm.register(HookImpl1())
pm.register(HookImpl2()) # 先注册2  再注册的1
print(pm.hook.calculate(a=1, b=2))
# [2, 3]

#hook 和 plugin 的对应关系是 1:N，如果说注册了多个实现了同一个 hook 的 plugin ，会返回多个结果，我们来看这个例子

#在这里我们注册了两个 plugin , HookImpl1和 HookImpl2，分别对应了加法和乘法的两个不同逻辑

# 一次 hook 的调用返回了2个plugin 执行的结果，
# 注意一下这里是先执行后注册的 HookImpl2，
# 再执行先注册的HookImpl1, 下次具体分析 pluggy 实现的时候会解释