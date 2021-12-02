*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${SERVER}         www.baidu.com
${BROWSER}        gc
${DELAY}          1
${SEARCH URL}      http://${SERVER}/

*** Keywords ***
Open Browser To Baidu
    Open Browser    ${SEARCH URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Search Page Should Be Open

Search Page Should Be Open
    Title Should Be     百度一下，你就知道

Go To Search Page
    Go To    ${SEARCH URL}
    Search Page Should Be Open

Input Context
    [Arguments]     ${keyword}
    Input Text  kw  ${keyword}

Click Search Button
    Click Element	id:su