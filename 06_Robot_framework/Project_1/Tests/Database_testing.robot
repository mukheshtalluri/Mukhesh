*** Settings ***
Documentation    Database testing in the robot framework
Library    DatabaseLibrary

*** Variables ***
${DBName}    database-name
${DBUser}    username
${DBPassword}    password
${DBHost}    db4free.net
${DBPort}    3306

*** Test Cases ***
Verify successful creation of table
    [Documentation]    This testcase verify user able to create database successfully
    Connect to DB
    ${output}=    Execute Sql String    CREATE TABLE Persons (PersonID int, FirstName varchar(255), Address varchar(255), City varchar(255));
    Should Be Equal As Strings    ${output}    None

Verify data insertion in the table
    [Documentation]    This testcase verify user able to add data into the database
    ${output}=    Execute Sql Script    ./Resources/DBData/insert.sql
    Should Be Equal As Strings    ${output}    None
    
Verify data update in the table
    [Documentation]    This testcase verify user able to update the data in table
    ${output}=    Execute Sql String    UPDATE Persons SET FirstName = 'Mahesh' WHERE City = 'Bangalore';
    Should Be Equal As Strings    ${output}    None

Verify certain record is present or not
    [Documentation]    This testcase verify the presence record in the database table
    Check If Exists In Database    SELECT PersonID FROM Persons WHERE FirstName = 'Mahesh';

Verify the table exist or not
    [Documentation]    This testcase verify table exist in the database or not
    Table Must Exist    Persons

Verify the row count is 1
    [Documentation]    This testcase verify the row count in the table
    Row Count Is Equal To X    SELECT PersonId FROM Persons WHERE City = 'Bangalore'    1

Verify user can delete the table
    [Documentation]    This testcase verify user able to delete table from the database
    ${output}=    Execute Sql String        DROP TABLE Persons;
    Should Be Equal As Strings    ${output}    None
    Disconnect DB

*** Keywords ***
Connect to DB
    Connect To Database    pymysql    ${DBName}    ${DBUser}     ${DBPassword}      ${DBHost}    ${DBPort}

Disconnect DB
    Disconnect From Database

