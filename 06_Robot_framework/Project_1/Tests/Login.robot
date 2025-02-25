*** Settings ***
Documentation    Login functionality
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
Verify successful login to the DemoBlaze
    [Documentation]    This testcase verify that user able to successful login to the Application.
    [Tags]    Smoke
    Open Browser    https://www.demoblaze.com/index.html   Chrome
    Wait Until Element Is Visible    login2    timeout=5
    Click Element    login2
    Wait Until Element Is Visible    loginusername    timeout=15
    Input Text    loginusername     Mukhesh_25
    Input Password    loginpassword    Test1234
    Click Element    xpath://button[text() = 'Log in']
    Wait Until Element Is Visible    logout2
    Element Should Be Visible    logout2   timeout=5
    Close Browser

Verify successful login to the Heroku
    [Documentation]    This testcase verify that user able to successful login to the Application.
    [Tags]    Smoke
    Open Browser    https://the-internet.herokuapp.com/login    Chrome
    Wait Until Element Is Visible    id:username    timeout=10
    Input Text    id:username    tomsmith
    Input Password    id:password     SuperSecretPassword!
    Click Element    xpath://button[@type = 'submit']
    Element Should Be Visible    xpath://i[text() = ' Logout']
    Close Browser




