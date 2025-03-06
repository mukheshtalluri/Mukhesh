*** Settings ***
Library    DatabaseLibrary
Library    OperatingSystem

Suite Setup    Connect To Database    pymysql    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
Suite Teardown    Disconnect From Database    

*** Variables ***
${DBName}    mukhesh
${DBUser}    root
${DBPass}    Mukhesh@1234
${DBHost}    localhost
${DBPort}    3306

*** Test Cases ***
Create person table in database mukhesh
    ${output}=    Execute Sql String    create table person(id int, first_name varchar(20), last_name varchar(20));
    Log To Console    ${output}
    Should Be Equal As Strings    ${output}    None
