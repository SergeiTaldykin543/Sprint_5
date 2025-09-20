from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import pytest

class TestRegistration:
    def test_successful_registration_with_valid_data(self, driver, test_user):
        driver.find_element("css selector", LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("css selector", EMAIL_INPUT))
        )
        
        driver.find_element("css selector", REGISTER_LINK).click()
        
        name_input = driver.find_element("css selector", NAME_INPUT)
        email_input = driver.find_element("css selector", EMAIL_INPUT)
        password_input = driver.find_element("css selector", PASSWORD_INPUT)
        
        name_input.send_keys(test_user["name"])
        email_input.send_keys(test_user["email"])
        password_input.send_keys(test_user["password"])
        
        assert test_user["name"].strip() != "", "Имя не должно быть пустым"
        assert "@" in test_user["email"] and "." in test_user["email"], "Email должен быть валидным"
        assert len(test_user["password"]) >= 6, "Пароль должен быть не менее 6 символов"
        
        driver.find_element("css selector", REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("css selector", EMAIL_INPUT)))
        
        assert "Вход" in driver.page_source

    def test_registration_short_password(self, driver, test_user):
        driver.find_element("css selector", LOGIN_BUTTON).click()
        driver.find_element("css selector", REGISTER_LINK).click()
        
        driver.find_element("css selector", NAME_INPUT).send_keys(test_user["name"])
        driver.find_element("css selector", EMAIL_INPUT).send_keys(test_user["email"])
        driver.find_element("css selector", PASSWORD_INPUT).send_keys("12345")
        
        driver.find_element("css selector", REGISTER_BUTTON).click()
         
        error_text = driver.page_source
        assert "Некорректный пароль" in error_text or "ошибка" in error_text.lower()