#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: pluggy-example.py
@time: 2022/3/28 16:34
http://markshao.github.io/2019/10/02/pytest-core-design-and-code-structure/
"""
from pluggy import HookspecMarker, HookimplMarker, PluginManager

spec = HookspecMarker("pluggy_demo_1")  # 规范
impl = HookimplMarker("pluggy_demo_1")  # 实现 implementations


class HookSpec:
    # @spec(historic=True)
    @spec
    def calculate(self, a, b):
        pass

class HookImpl1:
    @impl
    def calculate(self, a, b):
        return a + b

pm = PluginManager("pluggy_demo_1")
pm.add_hookspecs(HookSpec)  # 一个规范
pm.register(HookImpl1()) # 具体实现
ret =pm.hook.calculate(a=1, b=2)
print(ret)

# Pluggy的核心就是三个类 HookspecMarker, HookimplMarker,PluginManager，
# 核心的插件逻辑就是定义了一组 hook 的方法，然后 plugin 是hook 方法的具体实现
# 整个 Project 需要用一个全局唯一的 Project Name ，这里是 pluggy_demo_1
# HookSpec是一个申明 hook method 的 class ，每一个 hook method 需要用spec的装饰器来装饰
# HookImpl1 是一个 plugin 的实现，需要完整实现对应的hook方法，并且通过impl装饰器来装饰
# 核心代码的调用逻辑就是先创建一个PluginManager对象，注册 Spec 和对应的 plugin 对象，
# 然后通过 PluginManager自带的 hook 变量来调用对应的hook方法，传入相关的参数即可。
# 切记在调用 hook 的时候参数必须是通过关键字的方式来传递