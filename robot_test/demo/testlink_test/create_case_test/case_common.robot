# 创建case 的公共关键字方法

*** Settings ***
Documentation     testlink case create  common  function
Resource          ../resource.robot

*** Variables ***
${project_element}      name:testproject

*** Keywords ***
user login
    [Arguments]     ${login_name}   ${passwd}
    Input Loginname     ${login_name}
    INPUT PASSWD        ${passwd}
    Click Login Button
    Login Should Sucess
#选择工程
choose project
    [Arguments]     ${project_name}
    Select Frame    titlebar
#    Click Element   ${project_element}
    Select From List By Label       ${project_element}      ${project_name}
    Unselect Frame

#点击用例创建页面
click testspecification

    Select Frame    mainframe
#    Click Element   css:div:nth-child(3) > div:nth-child(3) > a:nth-child(1)
    Click Element   xpath:/html/body/div[2]/div[3]/a[1]