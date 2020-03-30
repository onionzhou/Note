*** Settings ***
Documentation     testlink login test

# 一个简单的例子通过百度搜索onion
Suite Setup       Open Browser To Testlink
Suite Teardown    Close Browser
#Test Setup        Go To Search Page
#Test Template     Login With Invalid Credentials Should Fail
Resource          ../resource.robot

*** Test Cases ***
vaild login
#    Open Browser To Testlink
    Input Loginname     ${LOGIN_NAME}
    Input Passwd        ${PASSWD}
    Click Login Button







