from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from urls import MAIN_PAGE
import pytest
import time

class TestConstructor:
    
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    def wait_for_page_load(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "tab_tab__1SPyG")))
        time.sleep(1) 
    
    @pytest.mark.parametrize("tab_locator,tab_name", [
        (BUNS_TAB, "Булки"),
        (SAUCES_TAB, "Соусы"),
        (FILLINGS_TAB, "Начинки")
    ])
    def test_switch_to_section(self, driver, tab_locator, tab_name):
        "Тест перехода к разделам конструктора"
        driver.get(MAIN_PAGE)
        self.wait_for_page_load(driver)
        
        tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(tab_locator))
        
        actions = ActionChains(driver)
        actions.move_to_element(tab).pause(0.5).click().perform()
        
        WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current__" in tab.get_attribute('class'))
        
        tab_class = tab.get_attribute('class')
        assert "tab_tab_type_current__" in tab_class, f"Раздел '{tab_name}' не активирован"