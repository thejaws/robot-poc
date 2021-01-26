*** Settings ***
Library  lib/CircuitBreaker.py

*** Variables ***
${URL} =     http://vg.no

*** Test Cases ***
Control CB from interface C
    @{meter} =  Select meter    with circuit breaker      that communicates well
    Length Should Be    ${meter}    2
    Log Many    @{meter}
    Ensure CB   @{meter} is connected and enabled for local disconnection
