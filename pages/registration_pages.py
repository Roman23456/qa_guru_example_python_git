import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Открываем сайт")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Клик на дропдаун")
    def open_account_menu(self):
        """
         Регистрация пользователя.
        """
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='main-link']//span[@class='fa fa-chevron-down']"))
        )
        element.click()

    @allure.step("Клик на кнопку регистрации")
    def click_register(self):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.ID, "link-register"))
        )
        element.click()

    @allure.step("Вводим имя")
    def fill_first_name(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-firstname"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Вводим фамилию")
    def fill_last_name(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-lastname"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Вводим email")
    def fill_email(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-email"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Вводим телефон")
    def fill_phone(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-telephone"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Вводим город")
    def fill_city(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-city"))
        )
        element.clear()
        element.send_keys(text)

        suggestion = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.suggestions-list div.suggestion-item"))
        )
        suggestion.click()

    @allure.step("Вводим улицу")
    def fill_street(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-street"))
        )
        element.clear()
        element.send_keys(text)

        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.suggestions-list"))
        )

        suggestion = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.suggestion-item div.main-text"))
        )
        suggestion.click()

    @allure.step("Вводим номер дома")
    def fill_house(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-house"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Вводим пароль")
    def password(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-password"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Вводим подтверждение пароля")
    def password_confirm(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-password-confirm"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Клик на чекбокс")
    def checkbox_name(self, ):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-agree"))
        )
        element.click()

    @allure.step("Клик на чекбокс регистрации")
    def click_register_button(self):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-storum-primary"))
        )

        element.click()
