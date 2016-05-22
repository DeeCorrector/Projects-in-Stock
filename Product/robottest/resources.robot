*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.
Library           Selenium2Library

*** Variables ***
${SERVER}         localhost:8000
${BROWSER}        Firefox
${DELAY}          0
${VALID USER}     HerlB
${VALID PASSWORD}    ormengorm
${FRONT URL}      http://${SERVER}/
${COUNSELORLIST URL}    http://${SERVER}/counselors
${PROJECTLIST URL}    http://${SERVER}/projects
${LOGIN URL}      http://${SERVER}/accounts/login/
${WELCOME URL}    http://${SERVER}/edit/profile/
${ERROR URL}      http://${SERVER}/accounts/auth_login/
