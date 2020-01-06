*** Settings ***
Documentation     testlink case create test
Resource          case_common.robot
Suite Setup       Open Browser To Testlink
Suite Teardown    Close Browser

*** Variables ***
${project_name}         project:project_4
${suit_name}            https
*** Test Cases ***
creat testcase
    user login   admin  admin
    choose project  ${project_name}
#    选择工程  ${project_name}
    click testspecification
    choose testsuite    ${suit_name}
    create testcase