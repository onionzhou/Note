#自定义关键字测试
*** Settings ***
Library    .custom_module.MyLibary
#Library    ./custom_module.py


*** Test Cases ***

custom test
    ${ret}=     my_keyword  qwer
    LOG     ${ret}
#通过装饰器
custom test1
    Import Library  ./custom_module.py
    ${ret}=     say  onion
    LOG     ${ret}