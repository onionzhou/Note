*** Settings ***
Documentation     testlink invalid login test

# 一个简单的例子通过百度搜索onion
Suite Setup       Open Browser To Testlink
Suite Teardown    Close Browser
#Test Setup        Go To Search Page
Test Template     invalid login should be failed
Resource          ../resource.robot

*** Test Cases ***      login_name          pwd
#test case  名字为 Invalid Username ，  ${username}=invalid ${password}=${PASSWD}
Invalid Username       invalid           ${PASSWD}
Invalid Password       xxxx              xxdddd


*** Keywords ***
invalid login should be failed
    [Arguments]    ${username}    ${password}
    Input Loginname     ${username}
    Input Passwd        ${password}
#    Click Login Button





