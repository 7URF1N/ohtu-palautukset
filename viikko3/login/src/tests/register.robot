*** Settings ***
Resource    resource.robot
Suite Setup    Open And Configure Browser
Suite Teardown    Close Browser
Test Setup    Reset Application Create User And Go To Register Page

*** Variables ***
${PASSWORD}    salasana123
${SHORT_PASSWORD}    abc123

*** Test Cases ***
Register With Valid Username And Password
    Fill Text    id=username    maija
    Fill Secret    id=password    $PASSWORD
    Fill Secret    id=password_confirmation    $PASSWORD
    Click    button >> text=Register
    Get Url    ==    ${HOME_URL}/welcome

Register With Password Containing Numbers
    Register User With Password    maija    kalle123
    Get Url    ==    ${HOME_URL}/welcome

Register With Password Containing Special Characters
    Register User With Password    maija    kalle#abc
    Get Url    ==    ${HOME_URL}/welcome

Register With Password Containing Only Lowercase Letters
    Register User With Password    maija    kallekalle
    Registration Should Fail With Message

Register With Password Containing Only Uppercase And Lowercase Letters
    Register User With Password    maija    KalleKalle
    Registration Should Fail With Message

Register With Matching Password Confirmation
    Register User With Password And Confirmation    maija    kalle123    kalle123
    Get Url    ==    ${HOME_URL}/welcome

Register With Different Password Confirmation
    Register User With Password And Confirmation    maija    kalle123    kalle456
    Registration Should Fail With Message

Register With Too Short Username And Valid Password
    Fill Text    id=username    ab
    Fill Secret    id=password    $PASSWORD
    Fill Secret    id=password_confirmation    $PASSWORD
    Click    button >> text=Register
    Get Url    ==    ${REGISTER_URL}

Register With Valid Username And Too Short Password
    Fill Text    id=username    liisa
    Fill Secret    id=password    $SHORT_PASSWORD
    Fill Secret    id=password_confirmation    $SHORT_PASSWORD
    Click    button >> text=Register
    Get Url    ==    ${REGISTER_URL}

Register With Username That Is Already In Use
    Fill Text    id=username    kalle
    Fill Secret    id=password    $PASSWORD
    Fill Secret    id=password_confirmation    $PASSWORD
    Click    button >> text=Register
    Get Url    ==    ${REGISTER_URL}

*** Keywords ***
Register User With Password
    [Arguments]    ${username}    ${password}
    Register User With Password And Confirmation    ${username}    ${password}    ${password}

Register User With Password And Confirmation
    [Arguments]    ${username}    ${password}    ${password_confirmation}
    Fill Text    id=username    ${username}
    Fill Secret    id=password    $password
    Fill Secret    id=password_confirmation    $password_confirmation
    Click    button >> text=Register

Registration Should Fail With Message
    Get Url    ==    ${REGISTER_URL}
    Get Element Count    ul li    ==    1
    Get Text    ul li    *=    Password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To    ${REGISTER_URL}
