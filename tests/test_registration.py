import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data import TestUser
from urls import REGISTER_PAGE

@pytest.mark.run(order=1)
class TestRegistration:
    
    def test_successful_registration(self, driver):
        "1. Успешная регистрация"
        driver.get(REGISTER_PAGE)
        time.sleep(3)
        
        try:
            name_input = driver.find_element(By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
            email_input = driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
            password_input = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")

        except Exception as e:
            pytest.fail(f"Не удалось найти поля формы: {e}")
        
        name_input.send_keys(TestUser.NAME)
        print("Заполнили имя")
        time.sleep(1)
        
        email_input.send_keys(TestUser.EMAIL)
        time.sleep(1)
        
        password_input.send_keys(TestUser.PASSWORD)
        time.sleep(1)
        
        try:
            register_button = driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
            
            register_button.click()
            time.sleep(3)
                     
        except Exception as e:
            pytest.fail(f"Не найдена кнопка регистрации: {e}")

    def test_unsuccessful_registration_short_password(self, driver):
        "2. Неуспешная регистрация - короткий пароль"
        driver.get(REGISTER_PAGE)
        time.sleep(3)
        
        try:
            name_input = driver.find_element(By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
            email_input = driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
            password_input = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
            register_button = driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

        except Exception as e:
            pytest.fail(f"Не удалось найти элементы формы: {e}")
        
        name_input.send_keys(TestUser.NAME)
        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys("123")
        
        register_button.click()
        time.sleep(2)
        
        assert "register" in driver.current_url, "Ожидалось остаться на странице регистрации при коротком пароле"

    def test_unsuccessful_registration_existing_email(self, driver):
        "3. Неуспешная регистрация - существующий email"
        driver.get(REGISTER_PAGE)
        time.sleep(3)
        
        try:
            name_input = driver.find_element(By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
            email_input = driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
            password_input = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
            register_button = driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

        except Exception as e:
            pytest.fail(f"Не удалось найти элементы формы: {e}")
        
        name_input.send_keys(TestUser.NAME)
        email_input.send_keys(TestUser.EMAIL)  
        password_input.send_keys(TestUser.PASSWORD)
        
        register_button.click()
        time.sleep(2)
        
        assert "register" in driver.current_url
        
