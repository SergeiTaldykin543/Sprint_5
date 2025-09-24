from selenium.webdriver.common.by import By

class CommonLocators:
    MAIN_PAGE_HEADER = (By.CLASS_NAME, "AppHeader_header__X9aJA")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.CSS_SELECTOR, "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc")
    TAB_SECTION = (By.CLASS_NAME, "tab_tab__1SPyG")

class AuthLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")
    PASSWORD_ERROR = (By.XPATH, "//input[@name='Пароль']/following-sibling::p")

class PersonalAccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile' and contains(@class, 'Account_link_active__2opc9')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3')]")
    PROFILE_NAME_INPUT = (By.XPATH, "//input[@type='text' and @name='Name']")
    PROFILE_EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name' and @value]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Отмена')]")

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")

class OrderLocators:
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title__2L34m")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close__2F_7G']")
    ORDER_STATUS = (By.CLASS_NAME, "OrderHistory_orderStatus__3S-Mq")

class ModalLocators:
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2Rcr")
    MODAL_CONTENT = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    MODAL_CLOSE = (By.XPATH, "//button[@class='Modal_modal__close__2F_7G']")