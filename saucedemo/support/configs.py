import imp
import os
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1]
CHROME_DRIVER_PATH = f"{PROJECT_DIR}\\resources\\chromedriver.exe"
FIREFOX_DRIVER_PATH = f"{PROJECT_DIR}\\resources\\geckodriver.exe"

def browser(brower_type):
    if brower_type == "Chrome":
        driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)
    if brower_type == "Firefox":
        firefox_service = Service(FIREFOX_DRIVER_PATH)
        driver = webdriver.Firefox(service=firefox_service)
        driver.maximize_window()
        driver.implicitly_wait(5)
    return driver