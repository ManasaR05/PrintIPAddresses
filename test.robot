*** Settings ***
Library     Process
Library     OperatingSystem

*** Variables ***
${IP_PRINT}      ip_print.py

*** Test Cases ***
Valid Input1
    ${result} =    Run Process    python3    ${IP_PRINT}    input1.json
    Should Be Equal As Strings    ${result.stdout}    192.168.101.101\n192.168.101.70\n192.168.101.153      strip_spaces=True   collapse_spaces=True

Valid Input2
    ${result} =    Run Process    python3    ${IP_PRINT}    input2.json
    Should Be Equal    ${result.stdout}    192.168.102.33 10.0.0.87\n192.168.103.74 10.0.0.77\n192.168.102.155 10.0.0.99

Missing File
    ${result} =    Run Process    python3    ${IP_PRINT}    nonexistent.json
    Should Contain    ${result.stderr}    'nonexistent.json' not found

Invalid JSON1
    Create File    invalid.json    {"key": "value}  # Missing closing quote
    ${result} =    Run Process    python3    ${IP_PRINT}    invalid.json
    Should Contain    ${result.stderr}    Invalid JSON

Invalid JSON2
    Create File    invalid.json    {"key": "value""}  # Missing closing quote
    ${result} =    Run Process    python3    ${IP_PRINT}    invalid.json
    Should Contain    ${result.stderr}    Invalid JSON

Missing vm_private_ips Key
    Create File    missing_key.json    {"some_other_key": "value"}
    ${result} =    Run Process    python3    ${IP_PRINT}    missing_key.json
    Should Contain    ${result.stderr}    'vm_private_ips' or 'value' key not found in 'missing_key.json'