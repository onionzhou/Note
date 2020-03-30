*** Settings ***
Documentation     百度搜索测试demo

# 一个简单的例子通过百度搜索onion
#Suite Setup       Open Browser To Baidu
#Suite Teardown    Close Browser
#Test Setup        Go To Search Page
#Test Template     Login With Invalid Credentials Should Fail
Resource          resource.robot

*** Test Cases ***
Search onion
    Open Browser To Baidu
    Input Context   onion
    Click Search Button

    [Teardown]    Close Browser






