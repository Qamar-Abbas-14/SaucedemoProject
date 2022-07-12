# Saucedemo Project UI Testing
This project implements Login Scenario testing of saucedemo.com based on Page Object Model with Python Pytest Framework. The project can be executed on Windows/Linux machine by following below-mentioned steps.

# Guide to Run the Project
1. Clone the repo from following link, you will get the SaucedemoProject/ folder:
- git clone https://github.com/Qamar-Abbas-14/SaucedemoProject.git

2. Make sure you have python installed on your Windows or Linux Machine

3. Go to SaucedemoProject folder for creating a virtual environment and activate it by typing in following command:
- Python  -m venv path_of_virtual_environment/
  On Windows:
- /path_of_virtual_environment/Scripts/Activate.ps1

  On Linux Machine:
- source proj-env/bin/activate

4. Get the dependencies/packages of the project from following link:
- pip install –r requirement.txt

6. Change directory of project to saucedemo/ and install local packages from following command:
- Python setup.py develop

7. Change directory and go to testcases directory containing test_login_page.py file:
- cd SaucedemoProject/saucedemo/scenarios.

For Linux Machine:
- Go to directory saucedemo/resources/linux_driver/
- Run following command to make the two drivers for linux executable.
- chmod 775 *

Run the following commands to execute testcases:
  For running in Chrome:
- pytest –browser Chrome

  For Running in Firefox
- pytest –browser Firefox







