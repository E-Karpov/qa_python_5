from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from locators import HomePageLocators, LoginPageLocators
from links import LINKS
from data import User


@pytest.fixture
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    yield driver
    # Закрытие драйвера после завершения теста
    driver.quit()


# Фикстура для авторизации пользователя перед выполнением тестов. Возвращает драйвер с выполненной авторизацией
@pytest.fixture
def get_login_driver(driver):
    driver.get(LINKS.HOME)
    driver.find_element(*HomePageLocators.HEADER_PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys(User.EMAIL)
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(User.PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(HomePageLocators.ORDER_BUTTON))

    return driver


# Фикстура для настройки тестов. Инициализирует драйвер и объект WebDriverWait
@pytest.fixture(autouse=True)
def setup(driver):
    return {
        "driver": driver,
        "wait": WebDriverWait(driver, 10)
    }