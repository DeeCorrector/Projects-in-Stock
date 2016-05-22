*** Settings ***
Documentation     A test suite for basic site navigation

Resource          resources.robot

*** Keywords ***
Open Browser To Front Page
    Open Browser    ${FRONT URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Front Page Should Be Open

Go To Front Page
    Go To     ${FRONT URL}
    Front Page Should Be Open

Front Page Should Be Open
    Location Should Be    ${FRONT URL}
    Title Should Be     Home

Navigate To Counselor List
    Click Element   Counselor-list
    Counselor List Page Should Be Open

Counselor List Page Should Be Open
    Location Should Be    ${COUNSELORLIST URL}
    Title Should Be     Counselor overview

Navigate To Project List
    Click Element   Project-list
    Project List Page Should Be Open

Project List Page Should Be Open
    Location Should Be    ${PROJECTLIST URL}
    Title Should Be     Projects overview

*** Test Cases ***
Navigate To Counserlor Overview
    Open Browser To Front Page
    Navigate to Counselor List

Navigate To Project Overview
    Go To Front Page
    Navigate to Project List
    [Teardown]    Close Browser
