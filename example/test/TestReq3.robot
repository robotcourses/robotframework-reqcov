*** Settings ***
Test Tags  KJTF-62

*** Test Cases ***
Scenario: Test Req 4

    Pass Execution    Hello KJTF-62

Scenario: Test HIST01
    [Tags]    HIST-001

    Pass Execution    Hello HIST-001