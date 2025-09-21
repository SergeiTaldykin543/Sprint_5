# Sprint_5 - Автотесты для Stellar Burgers

Этот проект содержит автотесты для сервиса Stellar Burgers, написанные на Python с использованием Selenium.

## Установка

1. Установите Python 3.8+
2. Установить зависимости: `pip install -r requirements.txt`
3. WebDriver Manager автоматически установит ChromeDriver

## Структура проекта

- `tests/` - директория с тестами
  - `__init__.py` - Инициализационный файл пакета тестов
  - `conftest.py` - фикстуры и настройки
  - `locators.py` - локаторы элементов страницы
  - `test_constructor.py` - тесты конструктора бургеров
  - `test_login.py` - тесты входа
  - `test_logout.py` - Тесты выхода из аккаунта
  - `test_personal_account.py` - тесты личного кабинета
  - `test_registration.py` - тесты регистрации
- `.gitignore` - исключения из репозитория
- `README.md` - Документация проекта
- `requirements.txt` - Зависимости проекта

## Тестовые данные

Email: sergey_taldykin_31_025@yandex.ru
Пароль: 123456
Имя: Sergey

  
## Установить зависимости
```bash
pip install selenium pytest

## Запуск тестов

Запуск всех тестов: `pytest -v`


