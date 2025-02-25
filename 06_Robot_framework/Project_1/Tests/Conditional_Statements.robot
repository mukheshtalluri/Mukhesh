*** Settings ***
Documentation    Conditional Statement on the Wikipedia page.
Library    SeleniumLibrary

*** Test Cases ***
Verify the Wikivoyage is Present on the Page and Click on it with if condition
    [Documentation]    Verifies if Wikivoyage is present on the Wikipedia page and clicks on it; otherwise, clicks Wiktionary.
    [Tags]    Regression
    Open Browser    https://www.wikipedia.org/    Chrome
    ${element_count}=    Get Element Count    xpath://span[text()='Wikivoyage']
    Run Keyword If    ${element_count} > 0    Click Wikivoyage
    ...  ELSE    Click Wiktionary    
    Title Should Be    Wikivoyage
    Close Browser

Verify the Wikivoyage is Present on the Page and Click on it with else condition
    [Documentation]    Verifies if Wikivoyage is present on the Wikipedia page and clicks on it; otherwise, clicks Wiktionary.
    [Tags]    Regression
    Open Browser    https://www.wikipedia.org/    Chrome
    ${element_count}=    Get Element Count    wronglocator
    Run Keyword If    ${element_count} > 0    Click Wikivoyage
    ...  ELSE    Click Wiktionary
    Title Should Be    Wiktionary
    Close Browser

*** Keywords ***
Click Wikivoyage
    Click Element    xpath://span[text()='Wikivoyage']

Click Wiktionary
    Click Element    xpath://span[text()='Wiktionary']
