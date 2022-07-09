# Saucedemo Project UI Testing
This project implements Login Scenario testing of saucedemo.com based on Page Object Model with Python Pytest Framework

# Guide to Run the Project
1. Clone the repo from following link:
- git clone https://github.com/Qamar-Abbas-14/SaucedemoProject.git

2. make sure you have python installed on you Windows or Linux Machine

3. Make a virtual environment and activate it by typing in following command:
- Python  -m venv path_of_virtual_environment/
on Windows:
- /path_of_virtual_environment/Scripts/Activate.ps1

On Linux Machine:
- source proj-env/bin/activate

4. Get the dependencies/packages of the project from following link:
- pip install –r requirement.txt

6. Change directory of project to DIR_PATH and install local packages from following command:
- Python setup.py develop

7. Change directory and go to testcases directory containing test_login_page.py  file:
- cd SaucedemoProject/saucedemo/scenarios
Run the following commands to execute testcase:

For running in Chrome:
- pytest –browser Chrome

For Running in Firefox
- pytest –browser Firefox
