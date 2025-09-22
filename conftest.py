from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()
    
    yield driver
    
    driver.quit()
    