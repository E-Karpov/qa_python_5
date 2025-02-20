from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import User
from locators import HomePageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from links import LINKS

class TestLogin:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver):
        driver.get(LINKS.HOME)

        # Ожидание и клик по кнопке "Войти в аккаунт"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.HEADER_LOGIN_BTN)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL_INPUT)).send_keys(User.EMAIL)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(HomePageLocators.ORDER_BUTTON)
        ), "Кнопка 'Оформить заказ' не отображается"
        assert driver.current_url == LINKS.HOME, "Вход не выполнен"

    # Вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver):
        driver.get(LINKS.HOME)

        # Ожидание и клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.HEADER_PERSONAL_ACCOUNT_BTN)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL_INPUT)).send_keys(User.EMAIL)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(HomePageLocators.ORDER_BUTTON)
        ), "Кнопка 'Оформить заказ' не отображается"
        assert driver.current_url == LINKS.HOME, "Вход через личный кабинет не выполнен"

    # Вход через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.get(LINKS.REGISTER)

        # Ожидание и клик по кнопке "Войти" на странице регистрации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL_INPUT)).send_keys(User.EMAIL)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(HomePageLocators.ORDER_BUTTON)
        ), "Кнопка 'Оформить заказ' не отображается"
        assert driver.current_url == LINKS.HOME, "Вход через форму регистрации не выполнен"

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_recover_password_form(self, driver):
        driver.get(LINKS.FORGOT_PASSWORD)

        # Ожидание и клик по кнопке "Войти" на странице восстановления пароля
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL_INPUT)).send_keys(User.EMAIL)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(HomePageLocators.ORDER_BUTTON)
        ), "Кнопка 'Оформить заказ' не отображается"
        assert driver.current_url == LINKS.HOME, "Вход через форму восстановления пароля не выполнен"