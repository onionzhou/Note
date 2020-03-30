# 创建case 的公共关键字方法

*** Settings ***
Documentation     testlink case create  common  function
Resource          ../resource.robot

*** Variables ***
${project_element}      name:testproject
${action_element}       xpath://div[@class='workBack']//img[@title="Actions"]
${create_testsuit_element}      xpath://div[@id='tsuite_control_panel']//fieldset[1]//input[@title='Create']
${create_testcase_element}      xpath://div[@id='tsuite_control_panel']//fieldset[2]//input[@title='Create']

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

#选择test suite

choose testsuite
    [Arguments]     ${suite_name}
    Select Frame    treeframe
    #xpath 精确匹配
#    Click Element   xpath://li[@class='x-tree-node']//span[text()='${suite_name}']
    #xpath 模糊匹配
    Click Element   xpath://li[@class='x-tree-node']//span[contains(text(),'${suite_name}')]
    Unselect Frame

create testcase
    Select Frame    mainframe
    Select Frame    workframe
    Click Element   ${action_element}
    Click Element   ${create_testcase_element}
    Input Text      id:testcase_name    'auto testcase name for onion'

#    Wait Until Page Contains Element    id:cke_1_contents     timeout=5
#    Input Text      id:cke_1_contents    'auto summary name for onion'
    #使用source格式输入
#    Wait Until Page Contains Element    id:cke_17_label     timeout=5
#    Click Element   id:cke_17_label
#    Wait Until Page Contains Element    id:cke_1_contents     timeout=5
#    Input Text      id:cke_1_contents   'summary summary !!!!'
    Capture Page Screenshot     oniontest-{index}.png