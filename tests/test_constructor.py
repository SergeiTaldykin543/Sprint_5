from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import pytest

class TestConstructor:
    def test_go_to_buns(self, driver):
        driver.find_element("css selector", BUNS_SECTION).click()
        
        active_section = driver.find_element("css selector", ACTIVE_SECTION)
        assert "Булки" in active_section.text

    def test_go_to_sauces(self, driver):
        driver.find_element("css selector", SAUCES_SECTION).click()
        
        active_section = driver.find_element("css selector", ACTIVE_SECTION)
        assert "Соусы" in active_section.text

    def test_go_to_fillings(self, driver):
        driver.find_element("css selector", FILLINGS_SECTION).click()
        
        active_section = driver.find_element("css selector", ACTIVE_SECTION)
        assert "Начинки" in active_section.text