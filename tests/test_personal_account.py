from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import pytest

class TestPersonalAccount:
    def test_go_to_personal_account_with_valid_user(self, driver, test_user):
        self.register_and_login(driver, test_user)
        
        driver.find_element("css selector", PERSONAL_ACCOUNT_BUTTON).click()
        
        assert "Профиль" in driver.page_source
        
        profile_email = driver.find_element("css selector", EMAIL_INPUT)
        assert profile_email.get_attribute("value") == test_user["email"]

    def test_logout_with_valid_user(self, driver, test_user):
        self.register_and_login(driver, test_user)
        
        driver.find_element("css selector", PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element("css selector", LOGOUT_BUTTON).click()
        
        assert "Вход" in driver.page_source

    def register_and_login(self, driver, user):
        driver.get(MAIN_PAGE + "register")
        driver.find_element("css selector", NAME_INPUT).send_keys(user["name"])
        driver.find_element("css selector", EMAIL_INPUT).send_keys(user["email"])
        driver.find_element("css selector", PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element("css selector", REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("css selector", EMAIL_INPUT)))
        driver.find_element("css selector", EMAIL_INPUT).send_keys(user["email"])
        driver.find_element("css selector", PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element("css selector", LOGIN_BUTTON_FORM).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("css selector", CONSTRUCTOR_BUTTON)))