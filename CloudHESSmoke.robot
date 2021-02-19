*** Settings ***
Documentation   Smoke test for cloud HES
Library  lib/cloud.py
Resource  ${RESOURCES}/common.robot

*** Variables ***
${meter}=  123

*** Test Cases ***
Ping a meter
    [Tags]    SMOKE
    ${pingstatus}=  Ping meter   ${meter}
    Ensure acceptable http status code  ${pingstatus}
    Ensure acceptable http response  ${pingstatus}
    Set

#*** Keywords ***
#Provided precondition
#    Setup system under test