
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Open url")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Click on account dropdown arrow")
    def open_account_menu(self):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='main-link']//span[@class='fa fa-chevron-down']"))
        )
        element.click()

    @allure.step("Click Registration button")
    def click_register(self):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.ID, "link-register"))
        )
        element.click()

    @allure.step("Fill First Name")
    def fill_first_name(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-firstname"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Fill Last Name")
    def fill_last_name(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-lastname"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Fill Email")
    def fill_email(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-email"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Fill Phone")
    def fill_phone(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-telephone"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Fill City")
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

    @allure.step("Fill street")
    def fill_street(self, text):
        # 1. Находим поле и вводим текст
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-street"))
        )
        element.clear()
        element.send_keys(text)

        # 2. Ждем появления списка подсказок
        # По скриншоту видно, что список имеет класс suggestions-list
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.suggestions-list"))
        )

        # 3. Кликаем по первой подсказке в списке
        # На скриншоте подсказка находится внутри div.suggestion-item -> div.main-text
        suggestion = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.suggestion-item div.main-text"))
        )
        suggestion.click()

        # Даем время на обработку выбора (опционально)

    @allure.step("Fill House")
    def fill_house(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-house"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Password")
    def password(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-password"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Password Confirm")
    def password_confirm(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-password-confirm"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Checkbox")
    def checkbox_name(self, ):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "input-agree"))
        )
        element.click()

    @allure.step("Click Register Button")
    def click_register_button(self):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-storum-primary"))
        )

        element.click()

        # На сайте регистрации капча ее никак не обойти