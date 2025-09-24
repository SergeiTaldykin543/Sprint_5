import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators, CommonLocators
from urls import MAIN_PAGE

class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.driver.get(MAIN_PAGE)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CommonLocators.MAIN_PAGE_HEADER)
        )
        # Ждем загрузки табов конструктора
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ConstructorLocators.BUNS_TAB)
        )

    def test_switch_to_sauces_tab(self):
        """Проверка перехода к разделу 'Соусы'"""
        sauces_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        )
        sauces_tab.click()

        # Ждем, пока таб станет активным
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Соусы")
        )
        
        active_tab = self.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text, "Таб 'Соусы' не активирован"

    def test_switch_to_fillings_tab(self):
        """Проверка перехода к разделу 'Начинки'"""
        fillings_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)
        )
        fillings_tab.click()

        # Ждем, пока таб станет активным
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Начинки")
        )
        
        active_tab = self.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text, "Таб 'Начинки' не активирован"

    def test_switch_to_buns_tab(self):
        """Проверка перехода к разделу 'Булки' после перехода к другому разделу"""
        # Сначала переходим на другую вкладку
        sauces_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        )
        sauces_tab.click()

        # Ждем активации таба с соусами
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Соусы")
        )

        # Теперь переходим обратно на булки
        buns_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        )
        buns_tab.click()

        # Ждем, пока таб станет активным
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Булки")
        )
        
        active_tab = self.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text, "Таб 'Булки' не активирован"