*** Settings ***
Documentation     命令测试

# 一个简单的例子通过百度搜索onion
#Suite Setup       Open Browser To Baidu
#Suite Teardown    Close Browser
#Test Setup        Go To Search Page
#Test Template     Login With Invalid Credentials Should Fail
Resource          resource.robot

*** Test Cases ***
Search onion
    Open Browser To Baidu
    ${tmp}=     Get Title
    Should Match Regexp     ${tmp}  百度一下\*
    Log     ${tmp}
    [Teardown]    Close Browser






