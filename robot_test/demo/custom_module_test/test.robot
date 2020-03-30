
#用于测试 robot 调用 python 代码
#此处把python 一个类 当做一个模块

*** Settings ***
Library    .custom_module.Custom    10086
Library    .custom_module.ExampleLibary

*** Test Cases ***
custom test
    mycount
    ${ret}=     get_value
    LOG     ${ret}