from random import randint

class User:
    user_name = 'Эдуард'
    email = f'eduard_karpov_18_161@yandex.ru'
    password = f'Qwerty1'

class UserGenerate:
    user_name = 'Иван'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe'