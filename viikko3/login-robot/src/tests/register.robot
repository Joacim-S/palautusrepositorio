*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kaisa  maija123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials   maija  testi1234
    Output Should Contain  User with username maija already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ap  haha1234
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  äää  kakka123
    Output Should Contain  Only a-z allowed in the username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  ville  1234567
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  ville  hahahaha
    Output Should Contain  Password can't only contain letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials   maija  maija123