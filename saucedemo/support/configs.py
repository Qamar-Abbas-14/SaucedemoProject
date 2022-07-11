import imp
import os
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1]
OS_NAME = os.name

if OS_NAME == 'nt':
    CHROME_DRIVER_PATH = f"{PROJECT_DIR}\\resources\\windows_driver\\chromedriver.exe"
    FIREFOX_DRIVER_PATH = f"{PROJECT_DIR}\\resources\\windows_driver\\geckodriver.exe"
else:
    FIREFOX_DRIVER_PATH = f"{PROJECT_DIR}/resources/linux_driver/geckodriver"
    CHROME_DRIVER_PATH = f"{PROJECT_DIR}/resources/linux_driver/chromedriver"

def browser(brower_type):
    if brower_type == "Chrome":
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)
    if brower_type == "Firefox":
        driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)
    return driver