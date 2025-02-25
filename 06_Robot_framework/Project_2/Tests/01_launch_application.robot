*** Settings ***
# In settings we will maintain the documentation, library and resources.
Documentation    Launch the automation blog spot application
Library    SeleniumLibrary

*** Variables ***
# If any variables which we are using multiple times in the application we can store it as the variable and we can reuse.
${browser}=    Chrome
${url}=    https://testautomationpractice.blogspot.com/
${title_card}=    xpath://h1[normalize-space()='Automation Testing Practice']
${email}=    'mukhesh.t@gmail.com'

*** Test Cases ***
# This Portion we will maintain testcases
Verify use able to launch the application in maximise window and verify the page title
    [Documentation]    This testcase verify the user able launch the maximise screen and verify the page title.
    [Tags]    Smoke
    Open Browser     ${url}   ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    ${title_card}    timeout=5
    ${page_title}=    Get Title
    Should Be Equal As Strings    ${page_title}    Automation Testing Practice
    Close Browser
    
Verify user able add the data into the textbox
    [Documentation]    This testcase verify user able to enter text in the textbox
    [Tags]    Smoke
    Open Browser     ${url}   ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    ${title_card}
    Input Text    name    Mukhesh
    ${name}=    Get Value    name
    Log    The name textbox contain : ${name}
    Input Text    email    ${email}
    ${email}=    Get Value    email
    Log    The email textbox contain : ${email}
    Input Text    phone    1234567890
    ${phone}=    Get Value    phone
    Log     The phone textbox contain : ${phone}
    Input Text    textarea    5-156, \nHoodi main road, \nTigarala palya, \nBangalore, \n560067
    Capture Page Screenshot    textbox.png
    Close Browser

Verify user able to select the radio button
    [Documentation]    This testcase verify the user able to successfully click on the radio button
    [Tags]    Smoke
    Open Browser     ${url}   ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    ${title_card}
    Click Element    male
    Capture Page Screenshot    radiobutton.png
    Close Browser

Verify user able to select multiple checkbox
    [Documentation]    This testcase verify user able to click on multiple checkbox
    [Tags]    Regression
    Launch Application
    ${list_of_elements}=    Get Webelements    xpath://input[@type = 'checkbox']
    FOR     ${element}    IN    @{list_of_elements}
        ${text}=    Get Element Attribute    ${element}    id
        Log    ${text}
        IF    '${text}' == 'sunday' or '${text}' == 'wednesday'
            Click Element    ${element}
            Execute JavaScript  
            ...  window.scrollTo({top: arguments[0].getBoundingClientRect().top + window.scrollY - (window.innerHeight / 2), behavior: 'smooth'});  
            ...  ARGUMENTS  ${element}
            Capture Page Screenshot    checkbox.jpg
        END
    END
    Close Application






*** Keywords ***
# Here we well define keyword. In simpler terms we can make list of steps to single step
Launch application
    Open Browser     ${url}   ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    ${title_card}

Close application
    Close Browser

