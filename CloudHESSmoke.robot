*** Settings ***
Documentation   Smoke test for cloud HES
Library  lib/cloud.py

*** Variables ***
${meter}=  123

*** Test Cases ***
Ping a meter
    [Tags]    SMOKE
    Ping meter   ${meter}

#*** Keywords ***
#Provided precondition
#    Setup system under test