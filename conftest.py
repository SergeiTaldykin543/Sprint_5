from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

@pytest.fixture
def test_user():
    return {
        "email": "sergey_taldykin_31@yandex.ru",
        "password": "123456",
        "name": "Sergey Taldykin"
    }