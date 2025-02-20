# Sprint_5 - "UI-тестирование"

## Структура проекта

1. **tests** - Папка с тестами
   - **test_log_in.py** - Тесты для авторизации
      - `test_login_from_main_page` - Проверка входа через кнопку "Войти в аккаунт" на главной странице
      - `test_login_from_personal_account_button` - Проверка входа через кнопку "Личный кабинет"
      - `test_login_from_registration_form` - Проверка входа через форму регистрации
      - `test_login_from_recover_password_form` - Проверка входа через форму восстановления пароля
   - **test_profile.py** - Тесты для личного кабинета
      - `test_navigate_to_personal_area_from_main_page` - Проверка перехода в личный кабинет
      - `test_navigate_to_constructor_from_personal_area_via_constructor_btn` - Проверка перехода в конструктор через кнопку "Конструктор"
      - `test_navigate_to_constructor_from_personal_area_via_logo` - Проверка перехода в конструктор через логотип
      - `test_logout_from_personal_area` - Проверка выхода из аккаунта
   - **test_registration.py** - Тесты для регистрации
      - `test_successful_registration` - Проверка успешной регистрации
      - `test_incorrect_password_registration` - Проверка ошибки при некорректном пароле
   - **test_constructor_burgers.py** - Тесты для конструктора бургера
      - `test_constructor_buns_section` - Проверка перехода к разделу "Булки"
      - `test_constructor_sauces_section` - Проверка перехода к разделу "Соусы"
      - `test_constructor_toppings_section` - Проверка перехода к разделу "Начинки"

2. **data.py**:  
Содержит данные для тестов, такие как учетные данные пользователей и генерация случайных данных.

3. **locators.py**:  
Содержит локаторы для элементов на страницах, организованные по классам для каждой страницы.

4. **links.py**:  
Содержит URL-адреса страниц приложения.

5. **conftest.py**:  
Содержит фикстуры для инициализации драйвера, авторизации и других общих настроек.

6. **requirements.txt**:  
Содержит список зависимостей проекта (например, selenium, pytest).

7. Установить зависимости: ```pip install -r requirements.txt```
3. Запустить все тесты: ```pytest tests```
