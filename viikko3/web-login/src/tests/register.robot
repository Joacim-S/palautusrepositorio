*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kummi
    Set Password  kallenalle
    Set Confirmation  kallenalle
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
# ...
    Set Username  kaisa
    Set Password  kalle123
    Set Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
# ...
    Set Username  masa
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Main Page Should Be Open
    Click Button  Logout
    Set Username  masa
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
# ...
    Set Username  kaisa
    Set Password  kalle123
    Set Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  Passwords do not match
    Click Link  Login
    Set Username  kaisa
    Set Password  kalle123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}