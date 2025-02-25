*** Settings ***
Documentation    API Testing with the robot framework
Library    SeleniumLibrary
Library    Collections
Library    RequestsLibrary
Library    JSONLibrary

*** Variables ***

*** Test Cases ***
Do a GET request and validate response code and response body
    [Documentation]    This testcase verify GET Response code as 200 and validate the response body
    ...    In this test case we can validate the how to test api.
    [Tags]    smoke
    Create Session    mysession    https://www.metaweather.com    verify=true
    ${response}=    GET On Session    mysession    /api/location/search/  params=query=london
    Status Should Be    200    ${response}
    
    ${title}=    Get Value From Json    ${Response.json()}[0]    title
    ${title_from_list}=    Get From List    ${title}    0
    Should Be Equal    ${title_from_list}    London

    ${body}=  Convert To String  ${response.content}
    Should Contain  ${body}  location_type

*** Keywords ***
