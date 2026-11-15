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
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To    ${REGISTER_URL}
