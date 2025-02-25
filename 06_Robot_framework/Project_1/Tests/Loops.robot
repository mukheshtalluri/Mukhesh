*** Settings ***
Documentation    Here we will use to validate the elements
Library    SeleniumLibrary
Library    Collections

*** Variables ***
@{mobile_list}    Samsung galaxy s6    Nokia lumia 1520    Nexus 6    Samsung galaxy s7    Iphone 6 32gb    Sony xperia z5    HTC One M9

*** Test Cases ***
Verify the successful login and count the phones count
    [Documentation]    This testcase will verify the used successful login and count no.of phones were there
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
    Click Link    xpath://a[text() = 'Phones']
    @{element_list}=    Get Webelements    css:.card-title
    @{text_list}=    Create List
    FOR    ${element}    IN    @{element_list}
        ${text}=    Get Text    ${element}
        Append To List    ${text_list}    ${text}
    END
    Log To Console    \n List from the webpage:
    Log To Console    ${text_list}
    Log To Console    Our list:
    Log To Console    ${mobile_list}
    Lists Should Be Equal    ${text_list}    ${mobile_list}
    Close Browser



*** Keywords ***
