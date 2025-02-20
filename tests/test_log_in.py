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
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.header_login_btn)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_email_input)).send_keys(User.email)
        driver.find_element(*LoginPageLocators.login_password_input).send_keys(User.password)
        driver.find_element(*LoginPageLocators.login_submit_btn).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HomePageLocators.order_button))
        assert driver.current_url == LINKS.HOME, "Вход не выполнен"

    # Вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver):
        driver.get(LINKS.HOME)

        # Ожидание и клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.header_personal_account_btn)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_email_input)).send_keys(User.email)
        driver.find_element(*LoginPageLocators.login_password_input).send_keys(User.password)
        driver.find_element(*LoginPageLocators.login_submit_btn).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HomePageLocators.order_button))
        assert driver.current_url == LINKS.HOME, "Вход через личный кабинет не выполнен"

    # Вход через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.get(LINKS.REGISTER)

        # Ожидание и клик по кнопке "Войти" на странице регистрации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationPageLocators.login_link)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_email_input)).send_keys(User.email)
        driver.find_element(*LoginPageLocators.login_password_input).send_keys(User.password)
        driver.find_element(*LoginPageLocators.login_submit_btn).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HomePageLocators.order_button))
        assert driver.current_url == LINKS.HOME, "Вход через форму регистрации не выполнен"

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_recover_password_form(self, driver):
        driver.get(LINKS.FORGOT_PASSWORD)

        # Ожидание и клик по кнопке "Войти" на странице восстановления пароля
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ForgotPasswordPageLocators.login_link)).click()

        # Ввод данных для входа
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_email_input)).send_keys(User.email)
        driver.find_element(*LoginPageLocators.login_password_input).send_keys(User.password)
        driver.find_element(*LoginPageLocators.login_submit_btn).click()

        # Проверка успешного входа через наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HomePageLocators.order_button))
        assert driver.current_url == LINKS.HOME, "Вход через форму восстановления пароля не выполнен"