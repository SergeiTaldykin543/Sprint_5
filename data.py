# data.py
class TestUser:
    EMAIL = "sergey_taldykin_31@yandex.ru"
    PASSWORD = "123456"
    NAME = "Sergey Taldykin"

    @classmethod
    def get_dict(cls):
        return {
            "email": cls.EMAIL,
            "password": cls.PASSWORD,
            "name": cls.NAME
        }
