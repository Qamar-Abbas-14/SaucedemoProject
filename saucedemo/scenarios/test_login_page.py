import pytest
import os
import time
from pages.login import SauceDemoPage
from support.configs import browser
from utils.inputs import *


class TestCases():
    def test_login_verification(self, browser):
        global page_driver
        page_driver = SauceDemoPage(browser)
        page_driver.visit_login_page()   

    def test_page_loaded_successfully(self):
        page_driver.verify_page_load()

    def test_invalid_username(self):
        page_driver.enter_username(wrong_user['name'])
        page_driver.enter_password(wrong_user['password'])
        page_driver.click_login_btn()

    def test_errordisplay_invalid_username(self):
        error = page_driver.check_error_display()
        assert(error == 'Epic sadface: Username and password do not match any user in this service')

    def test_invalid_password(self):
        page_driver.clear_username_txtbx()
        page_driver.enter_username(validusers['name'])
        page_driver.clear_password_txtbx()
        page_driver.enter_password(validusers['wrong_password'])
        page_driver.click_login_btn()

    def test_errordisplay_invalid_password(self):
        error = page_driver.check_error_display()
        assert(error == 'Epic sadface: Username and password do not match any user in this service')

    def test_invalid_username_password(self):
        page_driver.clear_username_txtbx()
        page_driver.enter_username("nonstandard_user")
        page_driver.clear_password_txtbx()
        page_driver.enter_password("secret_sauce1")
        page_driver.click_login_btn()

    def test_empty_password_error(self):
        page_driver.clear_username_txtbx()
        page_driver.enter_username(validusers['name'])
        page_driver.clear_password_txtbx()
        page_driver.click_login_btn()
        error = page_driver.check_error_display()
        assert(error == 'Epic sadface: Password is required')
  

    def test_locked_user_credentials(self):
        page_driver.clear_username_txtbx()
        page_driver.enter_username(lockedusers['name'])
        page_driver.clear_password_txtbx()
        page_driver.enter_password(lockedusers['password']) 
        page_driver.click_login_btn()
        error = page_driver.check_error_display()
        assert(error == 'Epic sadface: Sorry, this user has been locked out.')

    def test_problem_user_credentials(self):
        page_driver.clear_username_txtbx()
        page_driver.enter_username(problem_user['name'])
        page_driver.clear_password_txtbx()
        page_driver.enter_password(problem_user['password']) 
        page_driver.click_login_btn()
        item_html = page_driver.check_image_item_html()
        assert('src="/static/media/bike-light-1200x1500.a0c9caae.jpg"' in item_html)

    def test_glitch_user_credentials(self):
        page_driver.visit_login_page()
        page_driver.clear_username_txtbx()
        page_driver.enter_username(glitch_user['name'])
        page_driver.clear_password_txtbx()
        page_driver.enter_password(glitch_user['password']) 
        page_driver.click_login_btn()
        item_html = page_driver.check_image_item_html()
        assert('src="/static/media/bike-light-1200x1500.a0c9caae.jpg"' in item_html)
        

    def test_valid_login(self):
        page_driver.visit_login_page()
        page_driver.clear_username_txtbx()
        page_driver.enter_username(validusers['name'])
        page_driver.clear_password_txtbx()
        page_driver.enter_password(validusers['password'])
        page_driver.click_login_btn()
        item_html = page_driver.check_image_item_html()
        assert('src="/static/media/bike-light-1200x1500.a0c9caae.jpg"' in item_html)

    def test_teardown(self):
        page_driver.close_browser()