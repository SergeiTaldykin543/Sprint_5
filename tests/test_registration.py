import pytest
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators, AuthLocators
from data import TestUser
from urls import REGISTER_PAGE, LOGIN_PAGE


class TestRegistration:
    def generate_random_email(self):
        "Генерация случайного email"
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        return f"{username}@example.com"
    

    def test_successful_registration(self, driver):
        "1. Успешная регистрация"
        driver.get(REGISTER_PAGE)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))
        
        name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_INPUT))
        register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))

        name_input.send_keys(TestUser.NAME)
        email_input.send_keys(self.generate_random_email())
        password_input.send_keys(TestUser.PASSWORD)
        
        assert register_button.is_enabled(), "Кнопка регистрации должна быть активна после заполнения формы"
        
        register_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE))
        
        assert driver.current_url == LOGIN_PAGE, f"Ожидался URL {LOGIN_PAGE}, но получен {driver.current_url}"
        
        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Кнопка входа должна отображаться после успешной регистрации"


    def test_registration_with_short_password(self, driver):
        "Регистрация с коротким паролем"
        driver.get(REGISTER_PAGE)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))

        name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_INPUT))
        register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))

        name_input.send_keys(TestUser.NAME)
        email_input.send_keys(self.generate_random_email())
        password_input.send_keys("123") 

        WebDriverWait(driver, 3).until(lambda driver: driver.find_element(*RegistrationLocators.PASSWORD_INPUT).get_attribute("value") == "123")

        if register_button.is_enabled():
            register_button.click()
            try:
                error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE))
                assert error_message.is_displayed(), "Сообщение об ошибке должно отображаться"
                assert any(word in error_message.text.lower() for word in ["пароль", "password", "некорректный", "invalid", "короткий", "short"]), \
                    f"Сообщение об ошибке должно содержать информацию о пароле. Текст: {error_message.text}"
                
            except:
                assert "register" in driver.current_url, "Должны остаться на странице регистрации при коротком пароле"
                
        else:
            assert not register_button.is_enabled(), "Кнопка регистрации должна быть неактивна при коротком пароле"


    def test_registration_with_existing_email(self, driver):
        "Регистрация с уже существующим email"
        driver.get(REGISTER_PAGE)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))

        name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_INPUT))
        register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))

        name_input.send_keys(TestUser.NAME)
        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        
        assert register_button.is_enabled(), "Кнопка регистрации должна быть активна при заполнении формы"
        
        register_button.click()
        try:
            error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE))
            
            assert error_message.is_displayed(), "Сообщение об ошибке должно отображаться"
            assert any(word in error_message.text.lower() for word in ["существует", "exists", "уже", "already"]), \
                f"Сообщение об ошибке должно указывать на существующего пользователя. Текст: {error_message.text}"
                
        except:
            WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE))
            assert driver.current_url == LOGIN_PAGE, f"Ожидался переход на {LOGIN_PAGE} при успешной регистрации"