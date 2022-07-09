from support.configs import browser
from utils.locator import LoginPageLocator
from utils.inputs import *


class SauceDemoPage():
    def __init__(self, browser_choice = "Chrome"):
        self.driver = browser(browser_choice)
        self.timeout = 30

    def visit_login_page(self):
        self.driver.get(MAIN_PAGE_URL)

    def verify_page_load(self):
        self.driver.find_element(*LoginPageLocator.LOGIN_BTN)
       
    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocator.USR_NAME_TXTB).send_keys(username)

    def clear_username_txtbx(self):
        self.driver.find_element(*LoginPageLocator.USR_NAME_TXTB).clear()

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocator.PASSWORD_TXTB).send_keys(password)

    def clear_password_txtbx(self):
        self.driver.find_element(*LoginPageLocator.PASSWORD_TXTB).clear()

    def click_login_btn(self):
        self.driver.find_element(*LoginPageLocator.LOGIN_BTN).click()

    def check_error_display(self):
        text1 = self.driver.find_element(*LoginPageLocator.ERROR_DISP1).text
        return text1

    def check_image_item_html(self):
        elem = self.driver.find_element(*LoginPageLocator.IMG_ITEM_0)
        innerhtml = elem.get_attribute("innerHTML")
        return innerhtml
   
    def close_browser(self):
        self.driver.quit()