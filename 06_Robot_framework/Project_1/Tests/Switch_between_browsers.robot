*** Settings ***
Documentation    This testcase verify the user able to switch between the windows
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
Verify user able to switch between the browser windows based on the page title
    [Documentation]    This test case will be about switching between the windows and verify the page title
    [Tags]    Regression
    Open Browser    https://the-internet.herokuapp.com/windows    chrome
    Wait Until Element Is Visible    tag:h3    timeout=10
    Click Element    xpath://a[text() = 'Click Here']
    Switch Window    title:The Internet
    Element Text Should Be    tag:h3    Opening a new window    timeout=10
    Switch Window    title:New Window
    Element Text Should Be    tag:h3    New Window    timeout=10
    Close Browser
    
Verify user able to switch between the browser windows based on the window handles
    [Documentation]    This test case verify that page switching between the windows using window handles
    [Tags]    smoke
    Open Browser    https://the-internet.herokuapp.com/windows    chrome
    Wait Until Element Is Visible    tag:h3    timeout=10
    Click Element    xpath://a[text() = 'Click Here']
    ${handles}=    Get Window Handles    
    Switch Window    ${handles}[1]
    Element Text Should Be    tag:h3    New Window    timeout=10
    Switch Window    ${handles}[0]
    Element Text Should Be    tag:h3    Opening a new window    timeout=10
    Close Browser
       

