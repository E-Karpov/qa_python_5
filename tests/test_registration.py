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
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.register_name_input)).send_keys(user_data.user_name)
        driver.find_element(*RegistrationPageLocators.register_email_input).send_keys(user_data.email)
        driver.find_element(*RegistrationPageLocators.register_password_input).send_keys(user_data.password)
        driver.find_element(*RegistrationPageLocators.register_submit_btn).click()

        # Проверяем, что после успешной регистрации происходит переход на страницу авторизации
        WebDriverWait(driver, 15).until(EC.url_to_be(LINKS.LOGIN))
        assert driver.current_url == LINKS.LOGIN, "Регистрация не удалась"
        # Проверяем наличие формы авторизации
        wait.until(EC.presence_of_element_located(LoginPageLocators.login_form))

    # Проверка вывода ошибки для некорректного пароля (пароль менее 6 символов)
    def test_incorrect_password_registration(self, setup):
        driver = setup["driver"]
        wait = setup["wait"]

        driver.get(LINKS.REGISTER)  # Переход на страницу регистрации

        # Заполняем форму регистрации с некорректным паролем
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.register_name_input)).send_keys("Test User")
        driver.find_element(*RegistrationPageLocators.register_email_input).send_keys("test@example.com")
        driver.find_element(*RegistrationPageLocators.register_password_input).send_keys("123")  # Некорректный пароль
        driver.find_element(*RegistrationPageLocators.register_submit_btn).click()

        # Проверяем, что отображается сообщение об ошибке
        error_message = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.error_invalid_password))
        assert error_message.is_displayed(), "Сообщение об ошибке некорректного пароля не отображается"