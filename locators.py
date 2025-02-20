from selenium.webdriver.common.by import By

# Главная страница Stellar Burgers
class HomePageLocators:
    MAIN_PAGE_CONTAINER = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")  # Контейнер главной страницы
    HEADER_LOGO = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Логотип в шапке сайта
    HEADER_PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный Кабинет" в шапке
    HEADER_LOGIN_BTN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт" в шапке
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ" на главной странице
    HEADER_CONSTRUCTOR_BTN = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" в шапке
    HEADER_ORDER_FEED_BTN = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента Заказов" в шапке
    INGREDIENT_CATEGORY_BUN = (By.XPATH, ".//span[text() = 'Булки']")  # Кнопка переключения на категорию "Булки"
    INGREDIENT_CATEGORY_SAUCE = (By.XPATH, ".//span[text() = 'Соусы']")  # Кнопка переключения на категорию "Соусы"
    INGREDIENT_CATEGORY_TOPPING = (By.XPATH, ".//span[text() = 'Начинки']")  # Кнопка переключения на категорию "Начинки"
    INGREDIENT_SECTION_SAUCES = (By.XPATH, ".//h2[text() = 'Соусы']")  # Заголовок раздела "Соусы"
    INGREDIENT_LIST_SAUCES = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # Список соусов
    INGREDIENT_SECTION_BUNS = (By.XPATH, ".//h2[text() = 'Булки']")  # Заголовок раздела "Булки"
    INGREDIENT_LIST_BUNS = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # Список булок
    INGREDIENT_SECTION_TOPPINGS = (By.XPATH, ".//h2[text() = 'Начинки']")  # Заголовок раздела "Начинки"
    INGREDIENT_LIST_TOPPINGS = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # Список начинок


# Форма "Вход"
class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Контейнер формы авторизации
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля на странице входа
    LOGIN_SUBMIT_BTN = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти" на странице входа
    REGISTER_LINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Ссылка "Зарегистрироваться" на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Ссылка "Восстановить пароль" на странице входа


# Форма "Регистрация"
class RegistrationPageLocators:
    REGISTER_NAME_INPUT = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени на странице регистрации
    REGISTER_EMAIL_INPUT = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email на странице регистрации
    REGISTER_PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля на странице регистрации
    REGISTER_SUBMIT_BTN = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти" на странице регистрации
    ERROR_EXISTING_USER = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка: пользователь уже существует
    ERROR_INVALID_PASSWORD = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка: некорректный пароль


# Форма "Восстановление пароля"
class ForgotPasswordPageLocators:
    RECOVERY_EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']")  # Поле ввода email на странице восстановления пароля
    RECOVERY_SUBMIT_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка "Восстановить"
    LOGIN_LINK = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти" на странице восстановления пароля


# Личный кабинет
class ProfilePageLocators:
    PROFILE_CONTAINER = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Контейнер страницы профиля
    PROFILE_TAB = (By.XPATH, ".//a[text() = 'Профиль']")  # Вкладка "Профиль"
    ORDER_HISTORY_TAB = (By.XPATH, ".//a[text() = 'История заказов']")  # Вкладка "История заказов"
    LOGOUT_BTN = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"
    SAVE_CHANGES_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка "Сохранить"
    CANCEL_BTN = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка "Отмена"