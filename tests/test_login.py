import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, CommonLocators
from data import TestUser 
from urls import MAIN_PAGE, REGISTER_PAGE

class TestLogin:
    def test_login_from_main_page_button(self, driver):
        "2.1 Вход по кнопке «Войти в аккаунт» на главной"
        driver.get(MAIN_PAGE)
        
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CommonLocators.LOGIN_BUTTON_MAIN))
        login_button.click()

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        password_input = driver.find_element(*AuthLocators.PASSWORD_INPUT)
        login_button_form = driver.find_element(*AuthLocators.LOGIN_BUTTON)

        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button_form.click()

        main_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CommonLocators.MAIN_PAGE_HEADER))
        assert main_header.is_displayed(), "Не удалось войти в аккаунт - главная страница не отображается"


    def test_login_from_personal_account(self, driver):
        "2.2 Вход через кнопку «Личный кабинет»"
        driver.get(MAIN_PAGE)

        account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CommonLocators.PERSONAL_ACCOUNT_BUTTON))
        account_button.click()

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        password_input = driver.find_element(*AuthLocators.PASSWORD_INPUT)
        login_button = driver.find_element(*AuthLocators.LOGIN_BUTTON)

        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()

        main_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CommonLocators.MAIN_PAGE_HEADER))
        assert main_header.is_displayed(), "Не удалось войти в аккаунт через личный кабинет"


    def test_login_from_registration_form(self, driver):
        "2.3 Вход через кнопку в форме регистрации"
        driver.get(REGISTER_PAGE)

        login_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.LOGIN_LINK))
        login_link.click()

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        password_input = driver.find_element(*AuthLocators.PASSWORD_INPUT)
        login_button = driver.find_element(*AuthLocators.LOGIN_BUTTON)

        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()

        main_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CommonLocators.MAIN_PAGE_HEADER))
        assert main_header.is_displayed(), "Не удалось войти в аккаунт через форму регистрации"


    def test_login_from_password_recovery_form(self, driver):
        "2.4 Вход через кнопку в форме восстановления пароля"
        from urls import FORGOT_PASSWORD_PAGE
        
        driver.get(FORGOT_PASSWORD_PAGE)

        login_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.LOGIN_LINK))
        login_link.click()

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        password_input = driver.find_element(*AuthLocators.PASSWORD_INPUT)
        login_button = driver.find_element(*AuthLocators.LOGIN_BUTTON)

        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()

        main_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CommonLocators.MAIN_PAGE_HEADER))
        assert main_header.is_displayed(), "Не удалось войти в аккаунт через форму восстановления пароля"

