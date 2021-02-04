*** Settings ***
Library  lib/CircuitBreaker.py
Library  lib/listener.py
#Test Teardowns Stop Listener

*** Keywords ***
Read CircuitBreaker status of
        [Arguments]   ${meter}
        Read CircuitBreaker status    ${meter}

Set CircuitBreaker status of
        [Arguments]     ${meter}        ${status}
        Set CircuitBreaker status  ${meter}  ${status}


*** Variables ***
${URL} =     http://vg.no

*** Test Cases ***
#Test Setup Start Listener
#Test Teardown Stop Listener
Control CB from interface C
    ${meterpoint} =  Select meter    with circuit breaker      that communicates well
    Ensure CB   ${meterpoint} is connected and enabled for local disconnection
    @{CB_status}=  Read CircuitBreaker status of  ${meterpoint}
#    Set CircuitBreaker status of  ${meterpoint}      Disconnect
#    @{CB_status}=  Read CircuitBreaker status of  @{meter}
#    Set CircuitBreaker status to  connected