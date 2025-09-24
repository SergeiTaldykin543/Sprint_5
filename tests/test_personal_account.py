import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PersonalAccountLocators, AuthLocators, CommonLocators
from urls import LOGIN_PAGE
from data import TestUser

class TestPersonalAccount:
    def login_user(self, driver):
        "Вспомогательный метод для авторизации пользователя"
        driver.get(LOGIN_PAGE)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(TestUser.EMAIL)
        
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestUser.PASSWORD)
        driver.find_element(*AuthLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CommonLocators.MAIN_PAGE_HEADER))


    def test_navigate_to_personal_account(self, driver):
        "Переход в личный кабинет"
        self.login_user(driver)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CommonLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        profile_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))
        
        assert profile_link.is_displayed()


    def test_logout_from_personal_account(self, driver):
        "Выход из аккаунта"
        self.login_user(driver)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CommonLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)).click()

        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.LOGIN_BUTTON))
        
        assert login_button.is_displayed()


    def test_profile_name_displayed_correctly(self, driver):
        "Проверка отображения имени в профиле"
        self.login_user(driver)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CommonLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))

        name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_NAME_INPUT))
        
        actual_name = name_input.get_attribute("value")
        assert actual_name == TestUser.NAME, f"Expected name: {TestUser.NAME}, but got: {actual_name}"


    def test_profile_email_displayed_correctly(self, driver):
        "Проверка отображения email в профиле"
        self.login_user(driver)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CommonLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK))

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_EMAIL_INPUT))
        
        actual_email = email_input.get_attribute("value")
        assert actual_email == TestUser.EMAIL, f"Expected email: {TestUser.EMAIL}, but got: {actual_email}"