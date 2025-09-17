from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import pytest

class TestLogin:
    def test_login_with_valid_credentials(self, driver, test_user):
        self.register_user(driver, test_user)
        
        driver.get(MAIN_PAGE)
        
        driver.find_element("css selector", LOGIN_BUTTON).click()
        
        self.login_user(driver, test_user)
        
        assert "Оформить заказ" in driver.page_source
        
        assert test_user["email"] == "sergey_taldykin_31@yandex.ru"
        assert test_user["password"] == "123456"

    def test_login_from_main_button(self, driver, test_user):
        self.register_user(driver, test_user)
        driver.get(MAIN_PAGE)
        
        driver.find_element("css selector", LOGIN_BUTTON).click()
        self.login_user(driver, test_user)
        assert "Оформить заказ" in driver.page_source

    def test_login_from_personal_account(self, driver, test_user):
        self.register_user(driver, test_user)
        driver.get(MAIN_PAGE)
        
        driver.find_element("css selector", PERSONAL_ACCOUNT_BUTTON).click()
        self.login_user(driver, test_user)
        assert "Профиль" in driver.page_source

    def register_user(self, driver, user):
        driver.get(MAIN_PAGE + "register")
        
        driver.find_element("css selector", NAME_INPUT).send_keys(user["name"])
        driver.find_element("css selector", EMAIL_INPUT).send_keys(user["email"])
        driver.find_element("css selector", PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element("css selector", REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("css selector", EMAIL_INPUT))
        )

    def login_user(self, driver, user):
        driver.find_element("css selector", EMAIL_INPUT).send_keys(user["email"])
        driver.find_element("css selector", PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element("css selector", LOGIN_BUTTON_FORM).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("css selector", CONSTRUCTOR_BUTTON))
        )