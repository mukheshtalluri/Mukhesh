*** Settings ***
Documentation    Login functionality
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
Verify successful login to the Heroku
    [Documentation]    This testcase verify that user able to successful login to the Application.
    [Tags]    Smoke
    Start Test
    Login
    End Test

*** Keywords ***
Start Test
    Open Browser    https://the-internet.herokuapp.com/login    Chrome
    Maximize Browser Window

Login
    Wait Until Element Is Visible    id:username    timeout=10
    Input Text    id:username    tomsmith
    Input Password    id:password     SuperSecretPassword!
    Click Element    xpath://button[@type = 'submit']
    Element Should Be Visible    xpath://i[text() = ' Logout']

End Test
    Close Browser





