from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import HomePageLocators, ProfilePageLocators, LoginPageLocators
from links import LINKS

# Переход в личный кабинет
class TestProfileArea:

    # Проверка перехода по клику на «Личный кабинет».
    def test_navigate_to_personal_area_from_main_page(self, driver, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.header_personal_account_btn))
        driver.find_element(*HomePageLocators.header_personal_account_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.logout_btn))
        save_btn_displayed = driver.find_element(*ProfilePageLocators.save_changes_btn).is_displayed()

        assert driver.current_url == LINKS.PROFILE and save_btn_displayed

    # Проверка перехода по клику на «Конструктор»
    def test_navigate_to_constructor_from_personal_area_via_constructor_btn(self, driver, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.header_personal_account_btn))
        driver.find_element(*HomePageLocators.header_personal_account_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.logout_btn))
        driver.find_element(*HomePageLocators.header_constructor_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ingredient_section_buns))
        bun_displayed = driver.find_element(*HomePageLocators.ingredient_section_buns).is_displayed()

        assert driver.current_url == LINKS.HOME and bun_displayed

    # Проверка перехода по клику на логотип Stellar Burgers.
    def test_navigate_to_constructor_from_personal_area_via_logo(self, driver, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.header_personal_account_btn))
        driver.find_element(*HomePageLocators.header_personal_account_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.logout_btn))
        driver.find_element(*HomePageLocators.header_logo).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ingredient_section_buns))
        bun_displayed = driver.find_element(*HomePageLocators.ingredient_section_buns).is_displayed()

        assert driver.current_url == LINKS.HOME and bun_displayed

    #   Проверка выхода по кнопке «Выйти» в личном кабинете.
    def test_logout_from_personal_area(self, driver, get_login_driver):
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.header_personal_account_btn))
        driver.find_element(*HomePageLocators.header_personal_account_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.logout_btn))
        driver.find_element(*ProfilePageLocators.logout_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.login_submit_btn))
        login_btn_displayed = driver.find_element(*LoginPageLocators.login_submit_btn).is_displayed()

        assert driver.current_url == LINKS.LOGIN and login_btn_displayed