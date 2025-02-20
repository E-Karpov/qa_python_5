from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators
from links import LINKS
import pytest

# Раздел «Конструктор», проверяем что работают переходы к разделам:
class TestConstructorPage:

    # Переход к разделу «Булки»
    def test_constructor_buns_section(self, driver):
        driver.get(LINKS.HOME)

        # Переходим к разделу "Соусы", чтобы затем вернуться к "Булкам"
        driver.find_element(*HomePageLocators.ingredient_category_sauce).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ingredient_section_sauces))

        # Переходим к разделу "Булки"
        driver.find_element(*HomePageLocators.ingredient_category_bun).click()

        # Ожидаем, что раздел "Булки" отображается
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ingredient_section_buns)), "Раздел 'Булки' не отображается"

    # Переход к разделу «Соусы»
    def test_constructor_sauces_section(self, driver):
        driver.get(LINKS.HOME)

        # Переходим к разделу "Соусы"
        driver.find_element(*HomePageLocators.ingredient_category_sauce).click()

        # Ожидаем, что раздел "Соусы" отображается
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ingredient_section_sauces)), "Раздел 'Соусы' не отображается"

    # Переход к разделу «Начинки»
    def test_constructor_toppings_section(self, driver):
        driver.get(LINKS.HOME)

        # Переходим к разделу "Начинки"
        driver.find_element(*HomePageLocators.ingredient_category_topping).click()

        # Ожидаем, что раздел "Начинки" отображается
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ingredient_section_toppings)), "Раздел 'Начинки' не отображается"