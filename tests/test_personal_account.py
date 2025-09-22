import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TestUser
from urls import LOGIN_PAGE

@pytest.mark.run(order=3)
class TestPersonalAccount:
    
    def test_navigate_to_personal_account(self, driver):
        "3. Переход в личный кабинет"
        driver.get(LOGIN_PAGE)
        
        # Локаторы
        EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
        PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
        LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
        MAIN_PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
        ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
        PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EMAIL_INPUT))
        assert email_input.is_displayed()
        
        password_input = driver.find_element(*PASSWORD_INPUT)
        assert password_input.is_displayed()
        
        login_button = driver.find_element(*LOGIN_BUTTON)
        assert login_button.is_displayed()
        
        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()
        
        main_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MAIN_PAGE_HEADER))
        assert main_header.is_displayed()
        
        account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
        assert account_button.is_enabled()
        
        account_button.click()
        
        profile_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LINK))
        assert profile_link.is_displayed()
        
        current_url = driver.current_url
        assert "account" in current_url, f"Неверный URL после перехода в личный кабинет: {current_url}"
        
        account_sections = driver.find_elements(By.XPATH, "//a[contains(text(),'История заказов')]")
        assert len(account_sections) > 0, "В личном кабинете отсутствуют ожидаемые разделы"