*** Settings ***
Library     OperatingSystem
Resource    /opt/robot/user.resource

*** Variables ***
${KB_PATH}       /home/${USER}/kb
${FILE_NAME}     dummy_robot_test_file
${FILE_PATH}     ${KB_PATH}/${FILE_NAME}
${FILE_CONTENT}  "dummy robot test file content"

*** Test Cases ***
Check kb Path
    [Documentation]    Check kb path exists.
    Directory Should Exist    ${KB_PATH}
    Log To Console    "Path for kb is: ${KB_PATH}"

Directory Is Open For Creating Entries
    [Documentation]    User should be able to manually add a file in ${KB_PATH}
    Create File        ${FILE_PATH}    ${FILE_CONTENT}
    Log To Console     "Tried to create a file in ${KB_PATH}"

Entry Exists
    [Documentation]    Verify that entry can be read.
    Directory Should Not Be Empty    ${KB_PATH}
    File Should Exist                ${FILE_PATH}
    Get File Size                    ${FILE_PATH}
    Log To Console                   "Directory is not empty and a file exists."
