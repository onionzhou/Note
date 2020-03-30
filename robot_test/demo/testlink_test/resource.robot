*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
#http://148.70.174.22:8080/testlink/login.php
${SERVER}         148.70.174.22:8080
${BROWSER}        gc
${DELAY}          1
${SEARCH URL}     http://${SERVER}/testlink/login.php
${LOGIN_NAME}       admin
${PASSWD}           admin

*** Keywords ***
Open Browser To Testlink
    Open Browser    ${SEARCH URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Search Page Should Be Open

Search Page Should Be Open
    Title Should Be     Login


Input Loginname
    [Arguments]                 ${loginname}
    Input Text      tl_login    ${loginname}

Input Passwd
    [Arguments]                 ${passwd}
    Input Text  tl_password     ${passwd}

Click Login Button
    Click Button    Log in

#    Log     ${title}
Login Should Sucess
    ${title}    Get Title
    # 正则匹配
    Should Match Regexp      ${title}   TestLink\*

#小写的为自己定义的关键字方法
login should fail
    ${title}    Get Title
    # 正则匹配
    Should Not Match Regexp      ${title}   TestLink\*