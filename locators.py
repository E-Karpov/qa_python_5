from selenium.webdriver.common.by import By

# Главная страница Stellar Burgers
class HomePageLocators:
    main_page_container = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")  # Контейнер главной страницы
    header_logo = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Логотип в шапке сайта
    header_personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный Кабинет" в шапке
    header_login_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт" в шапке
    order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ" на главной странице
    header_constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" в шапке
    header_order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента Заказов" в шапке
    ingredient_category_bun = (By.XPATH, ".//span[text() = 'Булки']")  # Кнопка переключения на категорию "Булки"
    ingredient_category_sauce = (By.XPATH, ".//span[text() = 'Соусы']")  # Кнопка переключения на категорию "Соусы"
    ingredient_category_topping = (By.XPATH, ".//span[text() = 'Начинки']")  # Кнопка переключения на категорию "Начинки"
    ingredient_section_sauces = (By.XPATH, ".//h2[text() = 'Соусы']")  # Заголовок раздела "Соусы"
    ingredient_list_sauces = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # Список соусов
    ingredient_section_buns = (By.XPATH, ".//h2[text() = 'Булки']")  # Заголовок раздела "Булки"
    ingredient_list_buns = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # Список булок
    ingredient_section_toppings = (By.XPATH, ".//h2[text() = 'Начинки']")  # Заголовок раздела "Начинки"
    ingredient_list_toppings = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # Список начинок


# Форма "Вход"
class LoginPageLocators:
    login_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Контейнер формы авторизации
    login_email_input = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email на странице входа
    login_password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля на странице входа
    login_submit_btn = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти" на странице входа
    register_link = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Ссылка "Зарегистрироваться" на странице входа
    forgot_password_link = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Ссылка "Восстановить пароль" на странице входа


# Форма "Регистрация"
class RegistrationPageLocators:
    register_name_input = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени на странице регистрации
    register_email_input = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email на странице регистрации
    register_password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля на странице регистрации
    register_submit_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    login_link = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти" на странице регистрации
    error_existing_user = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка: пользователь уже существует
    error_invalid_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка: некорректный пароль


# Форма "Восстановление пароля"
class ForgotPasswordPageLocators:
    recovery_email_input = (By.XPATH, ".//label[text() = 'Email']")  # Поле ввода email на странице восстановления пароля
    recovery_submit_btn = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка "Восстановить"
    login_link = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти" на странице восстановления пароля


# Личный кабинет
class ProfilePageLocators:
    profile_container = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Контейнер страницы профиля
    profile_tab = (By.XPATH, ".//a[text() = 'Профиль']")  # Вкладка "Профиль"
    order_history_tab = (By.XPATH, ".//a[text() = 'История заказов']")  # Вкладка "История заказов"
    logout_btn = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"
    save_changes_btn = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка "Сохранить"
    cancel_btn = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка "Отмена"