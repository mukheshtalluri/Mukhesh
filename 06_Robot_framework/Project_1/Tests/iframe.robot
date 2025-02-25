*** Settings ***
Documentation    Iframes
Library    SeleniumLibrary

*** Test Cases ***
Verify read and write in the i frame
    [Documentation]    This testcase verify read and write happen from the i frame
    Open Browser    https://the-internet.herokuapp.com/iframe    Chrome
    Wait Until Element Is Visible    xpath://div[@role = 'menubar']    timeout=15
    Select Frame    id:mce_0_ifr
    Click Element    id:tinymce
    #Clear Element Text    id:tinymce
    #Input Text    id:tinymce    Text from the robot framework
    Element Text Should Be    id:tinymce    Your content goes here.
    Close Browser

Verify the different text from the i frame
    [Documentation]    This text case verify the text present in the i frame
    Open Browser    https://the-internet.herokuapp.com/nested_frames    Chrome
    Wait Until Element Is Visible    xpath://frame[@name = 'frame-top']    timeout=10
    Select Frame    xpath://frame[@name = 'frame-top']
    Select Frame    xpath://frame[@name = 'frame-left']
    Current Frame Should Contain    LEFT
    Unselect Frame
    Close Browser

