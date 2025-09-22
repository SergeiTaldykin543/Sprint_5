# data.py
class TestUser:
    EMAIL = "sergey_taldykin_31@yandex.ru"
    PASSWORD = "123456"
    NAME = "Sergey Taldykin"

    # Метод для возврата данных в виде словаря, если нужен именно такой формат для некоторых фикстур
    @classmethod
    def get_dict(cls):
        return {
            "email": cls.EMAIL,
            "password": cls.PASSWORD,
            "name": cls.NAME
        }