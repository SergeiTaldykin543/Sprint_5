import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#class TestUser:
   #EMAIL = "sergey_taldykin_31@yandex.ru"
   #PASSWORD = "123456"
   #NAME = "Sergey Taldykin"

# URL страниц
#MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
#LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"
#REGISTER_PAGE = "https://stellarburgers.nomoreparties.site/register"
#FORGOT_PASSWORD_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")  # Для запуска в CI
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()