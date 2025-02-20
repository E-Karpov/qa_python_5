from random import randint

class User:
    USER_NAME = 'Эдуард'
    EMAIL = 'eduard_karpov_18_161@yandex.ru'
    PASSWORD = 'Qwerty1'

class UserGenerate:
    USER_NAME = 'Иван'
    EMAIL = f'test{randint(0, 999)}@yandex.ru'
    PASSWORD = f'{randint(1000, 9999)}Qwe'