*** Settings ***
Documentation    Login functionality
Library    SeleniumLibrary

*** Variables ***
${UsernameDemo}    Mukhesh_25
${PasswordDemo}    Test1234
@{HerokuCredentials}    tomsmith    SuperSecretPassword!
&{VisibleElements}    Demo=logout2    Heroku=xpath://i[text() = ' Logout']

*** Test Cases ***
Verify successful login to the DemoBlaze
    [Documentation]    This testcase verify that user able to successful login to the Application.
    [Tags]    Smoke
    Open Browser    https://www.demoblaze.com/index.html   Chrome
    Wait Until Element Is Visible    login2    timeout=5
    Click Element    login2
    Wait Until Element Is Visible    loginusername    timeout=15
    Input Text    loginusername     ${UsernameDemo}
    Input Password    loginpassword    ${PasswordDemo}
    Click Element    xpath://button[text() = 'Log in']
    Wait Until Element Is Visible    ${VisibleElements}[Demo]
    Element Should Be Visible    ${VisibleElements}[Demo]   timeout=5
    Close Browser

Verify successful login to the Heroku
    [Documentation]    This testcase verify that user able to successful login to the Application.
    [Tags]    Smoke
    Open Browser    https://the-internet.herokuapp.com/login    Chrome
    Wait Until Element Is Visible    id:username    timeout=10
    Input Text    id:username    ${HerokuCredentials}[0]
    Input Password    id:password     ${HerokuCredentials}[1]
    Click Element    xpath://button[@type = 'submit']
    Element Should Be Visible    ${VisibleElements}[Heroku]
    Close Browser





