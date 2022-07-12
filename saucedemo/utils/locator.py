from selenium.webdriver.common.by import By

class LoginPageLocator:
    USR_NAME_TXTB = (By.ID, "user-name")
    PASSWORD_TXTB = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_DISP1 = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    IMG_ITEM_0 = (By.ID, 'item_0_img_link')

class MainPageLocators:
    SRC_IMG = 'src="/static/media/bike-light-1200x1500.a0c9caae.jpg"'