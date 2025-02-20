from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators
from links import LINKS
from data import UserGenerate
import pytest

class TestRegistrationPage:

    # Проверка успешной регистрации
    def test_successful_registration(self, setup):
        driver = setup["driver"]
        wait = setup["wait"]

        driver.get(LINKS.REGISTER)  # Переход на страницу регистрации
        user_data = UserGenerate()  # Используем случайные данные для регистрации

        # Заполняем форму регистрации
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.REGISTER_NAME_INPUT)).send_keys(user_data.USER_NAME)
        driver.find_element(*RegistrationPageLocators.REGISTER_EMAIL_INPUT).send_keys(user_data.EMAIL)
        driver.find_element(*RegistrationPageLocators.REGISTER_PASSWORD_INPUT).send_keys(user_data.PASSWORD)
        driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BTN).click()

        # Проверяем, что после успешной регистрации происходит переход на страницу авторизации
        assert WebDriverWait(driver, 15).until(EC.url_to_be(LINKS.LOGIN)), "Регистрация не удалась"
        # Проверяем наличие формы авторизации
        assert wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_FORM)), "Форма авторизации не отображается"

    # Проверка вывода ошибки для некорректного пароля (пароль менее 6 символов)
    def test_incorrect_password_registration(self, setup):
        driver = setup["driver"]
        wait = setup["wait"]

        driver.get(LINKS.REGISTER)  # Переход на страницу регистрации

        # Заполняем форму регистрации с некорректным паролем
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.REGISTER_NAME_INPUT)).send_keys("Test User")
        driver.find_element(*RegistrationPageLocators.REGISTER_EMAIL_INPUT).send_keys("test@example.com")
        driver.find_element(*RegistrationPageLocators.REGISTER_PASSWORD_INPUT).send_keys("123")  # Некорректный пароль
        driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BTN).click()

        # Проверяем, что отображается сообщение об ошибке
        error_message = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.ERROR_INVALID_PASSWORD))
        assert error_message.is_displayed(), "Сообщение об ошибке некорректного пароля не отображается"