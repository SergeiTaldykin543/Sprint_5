import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TestUser
from urls import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE

@pytest.mark.run(order=2)
class TestLogin:
    
    def test_login_from_main_button(self, driver):
        "2.1 Вход по кнопке «Войти в аккаунт» на главной"
        driver.get(MAIN_PAGE)
        
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        login_button.click()
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
        
        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))

    def test_login_from_personal_account(self, driver):
        "2.2 Вход через кнопку «Личный кабинет»"
        driver.get(LOGIN_PAGE)
        
        account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
        account_button.click()
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
        
        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))

    def test_login_from_registration_form(self, driver):
        "2.3 Вход через кнопку в форме регистрации"
        driver.get(REGISTER_PAGE)
        
        login_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Войти')]")))
        login_link.click()
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
        
        email_input.send_keys(TestUser.EMAIL)
        password_input.send_keys(TestUser.PASSWORD)
        login_button.click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))

