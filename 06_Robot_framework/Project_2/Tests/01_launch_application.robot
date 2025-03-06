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
    Capture Page Screenshot    Screenshorts/textbox.png
    Close Browser

Verify user able to select the radio button
    [Documentation]    This testcase verify the user able to successfully click on the radio button
    [Tags]    Smoke
    Open Browser     ${url}   ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    ${title_card}
    Click Element    male
    Capture Page Screenshot    Screenshorts/radiobutton.png
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
            Capture Page Screenshot    Screenshorts/checkbox.jpg
        END
    END
    Close Application

Verify user able select element from the dropdown
    [Documentation]    This testcase will verify user able to select item from the static drop down
    [Tags]    Smoke
    Launch Application
    Select From List By Label    country    India
    Capture Page Screenshot    Screenshorts/dropdown.jpg
    Close Browser

Verify user able to select the item from given list
    [Documentation]    This testcase will verify user able to select item from the unsorted list
    [Tags]    Smoke
    Launch Application
    Select From List By Label    colors    Green
    Capture Page Screenshot    Screenshorts/list_selection.jpg
    Close Application


Verify user able to select the item from given sorted list
    [Documentation]    This testcase will verify user able to select item from the sorted list
    [Tags]    Smoke
    Launch Application
    Select From List By Label    animals    Cheetah
    Capture Page Screenshot    Screenshorts/static_list_selection.jpg
    Close Application

Verify user able to select the date by providing input text
    [Documentation]    This testcase will verify user able to select date by providing input text
    [Tags]    Smoke
    Launch Application
    Input Text    datepicker    03/02/2025
    Capture Page Screenshot    Screenshorts/date_picker_1.jpg
    Close Application

Verify user able to select the date from date picker
    [Documentation]    This testcase will verify user able to select the date from date picker
    [Tags]    Smoke
    Launch Application
    Click Element    txtDate
    Select From List By Value    css:.ui-datepicker-month    10
    Select From List By Value    css:.ui-datepicker-year    2018
    Click Element    xpath://a[text() = '17']
    Capture Page Screenshot    Screenshorts/date_picker_2.jpg
    Close Application

Verify user able to select the date from date from the given range
    [Documentation]    This testcase will verify user able to select the date from date picker
    [Tags]    Smoke
    Launch Application
    Input Text    xpath://input[@placeholder='Start Date']    25-01-2024
    Input Text    xpath://input[@placeholder='End Date']    25-01-2025
    Click Element    xpath://div[@class = 'date-picker-box']/button
    Capture Page Screenshot    Screenshorts/date_picker_3.jpg
    Close Application

Verify user able to upload single file
    [Documentation]    This testcase will verify user able to upload file
    [Tags]    Smoke
    Launch Application
    Choose File    singleFileInput    D:/Test.py
    Click Element    xpath://button[text() = 'Upload Single File']
    Wait Until Element Is Visible    singleFileStatus
    Capture Page Screenshot    Screenshorts/file_upload.jpg
    Close Application

Verify user able to upload multiple files
    [Documentation]    This testcase will verify user able to upload multiple files
    [Tags]    Smoke
    Launch Application
    Choose File    multipleFilesInput    D:/Text1.txt \n D:/Text2.txt
    Click Element    xpath://button[text() = 'Upload Multiple Files']
    Wait Until Element Is Visible    multipleFilesStatus
    Capture Page Screenshot    Screenshorts/files_upload.jpg
    Close Application
    
Verify elements in static web table
    [Documentation]    This testcase verify the elements in the static web table
    [Tags]    Smoke
    Launch Application
    ${web_table_elements}=    Get Webelements    xpath://table[@name = 'BookTable']/tbody/tr/td[1]
    FOR    ${element}    IN    @{web_table_elements}
        ${text}=    Get Text    ${element}
        Log    ${text}
    END
    ${amount}=    Set Variable    0
    ${web_table_amount}=    Get Webelements    xpath://table[@name = 'BookTable']/tbody/tr/td[4]
    FOR    ${element}    IN    @{web_table_amount}
        ${text}=    Get Text    ${element}
        ${text}=    Convert To Integer    ${text}
        ${amount}=    Evaluate    ${amount} + ${text}
    END
    Log    ${amount}
    Close Application

Verify wiki search in the application and take to the right page
    [Documentation]    This testcase verify user able to enter in the textbox and it was displaying correct results or not
    [Tags]    Smoke
    Launch Application
    Input Text    Wikipedia1_wikipedia-search-input    Mukhesh
    Click Element    xpath://input[@class = 'wikipedia-search-button']
    Sleep    2s
    ${wiki_elements}=    Get Webelements    xpath://div[@id = 'wikipedia-search-result-link']/a
    Log    ${wiki_elements}
    FOR     ${element}    IN    @{wiki_elements}
        ${text}=    Get Text    ${element}
        IF    '${text}' == 'Mukesh (singer)'
            Click Element    ${element}
            Exit For Loop
        END
    END
    ${windows}=    Get Window Handles
    Switch Window    ${windows}[1]
    Capture Page Screenshot    Screenshorts/wiki_search.jpg
    Switch Window    ${windows}[0]
    Capture Page Screenshot    Screenshorts/homepage.jpg
    Close Application

Verify user able to click on simple alert and handle it carefully
    [Documentation]    This testcase verify user able to click on simple alert and handle successfully
    [Tags]    Smoke
    Launch Application
    Click Element    alertBtn
    ${alert_text}=    Handle Alert    ACCEPT
    Log    ${alert_text}
    Close Application

Verify user able to click on conformation alert and capture text from alert
    [Documentation]    This testcase verify user able to click on conformation alert and get text from the alert
    [Tags]    Smoke
    Launch Application
    Click Element    confirmBtn
    ${con_alert_text}=    Handle Alert    DISMISS
    Log    ${con_alert_text}
    Close Application

Verify user able to click on prompt alert and get text from the alert
    [Documentation]    This testcase verify user able to click on the prompt alert enter text and get text from it
    [Tags]    Smoke
    Launch Application
    Click Element    promptBtn
    Input Text Into Alert    Mukhesh    ACCEPT
    Close Application

Verify user able to switch between tabs
    [Documentation]    This testcase verify user able to switch between different tabs
    [Tags]    Smoke
    Launch Application
    Click Element    xpath://button[text() = 'New Tab']
    ${windows}=    Get Window Handles    
    Switch Window    ${windows}[1]
    Capture Page Screenshot    Screenshorts/newtab.jpg
    Close Application

Verify user able to switch to popup window
    [Documentation]    This testcase verify user able to switch to popup window
    [Tags]    Smoke
    Launch Application
    Click Element    PopUp
    ${windows}=    Get Window Handles    
    Switch Window    ${windows}[1]
    Capture Page Screenshot    Screenshorts/popup_window.jpg
    Close Application

Verify user able to perform mouse over action
    [Documentation]    This testcase verify user able to perform mouse over actions
    [Tags]    Smoke
    Launch Application
    Mouse Over    xpath://button[text() = 'Point Me']
    Capture Page Screenshot    Screenshorts/mouse_over.jpg
    Click Element    xpath://a[text() = 'Mobiles']
    Close Application

Verify user able to perform double click
    [Documentation]    This testcase verify user able to perform double click operation
    [Tags]    Smoke
    Launch Application
    Double Click Element    //button[text() = 'Copy Text']
    ${text}=    Get Value    field2
    Should Be Equal    ${text}    Hello World!
    Close Application

Verify user able to perform drag and drop
    [Documentation]    This testcase verify user able to perform drag and drop
    [Tags]    Smoke
    Launch Application
    Drag And Drop    xpath://p[text() = 'Drag me to my target']    droppable
    Capture Page Screenshot    Screenshorts/drag_and_drop.jpg
    Close Application







*** Keywords ***
# Here we well define keyword. In simpler terms we can make list of steps to single step
Launch application
    Open Browser     ${url}   ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    ${title_card}

Close application
    Close Browser

