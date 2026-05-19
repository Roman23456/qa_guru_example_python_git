import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    _ACCOUNT_MENU = (
        By.XPATH,
        "//a[@class='main-link']//span[@class='fa fa-chevron-down']",
    )
    _REGISTER_BTN = (By.ID, "link-register")

    @allure.step("Клик на дропдаун")
    def open_account_menu(self):
        self.click_element(self._ACCOUNT_MENU)

    @allure.step("Клик на кнопку регистрации")
    def click_register(self):
        self.click_element(self._REGISTER_BTN)

    @allure.step("Вводим имя")
    def fill_first_name(self, text):
        first_name_input = self.find_element((By.ID, "input-firstname"))
        first_name_input.clear()
        first_name_input.send_keys(text)

    @allure.step("Вводим фамилию")
    def fill_last_name(self, text):
        last_name_input = self.find_element((By.ID, "input-lastname"))
        last_name_input.clear()
        last_name_input.send_keys(text)

    @allure.step("Вводим email")
    def fill_email(self, text):
        email_input = self.find_element((By.ID, "input-email"))
        email_input.clear()
        email_input.send_keys(text)

    @allure.step("Вводим телефон")
    def fill_phone(self, text):
        phone_input = self.find_element((By.ID, "input-telephone"))
        phone_input.clear()
        phone_input.send_keys(text)

    @allure.step("Вводим город")
    def fill_city(self, text):
        city_input = self.find_element((By.ID, "input-city"))
        city_input.clear()
        city_input.send_keys(text)
        self.click_element(
            (By.CSS_SELECTOR, "div.suggestions-list div.suggestion-item")
        )

    @allure.step("Вводим улицу")
    def fill_street(self, text):
        street_input = self.find_element((By.ID, "input-street"))
        street_input.clear()
        street_input.send_keys(text)
        self.find_element((By.CSS_SELECTOR, "div.suggestions-list"))
        self.click_element((By.CSS_SELECTOR, "div.suggestion-item div.main-text"))

    @allure.step("Вводим номер дома")
    def fill_house(self, text):
        house_input = self.find_element((By.ID, "input-house"))
        house_input.clear()
        house_input.send_keys(text)

    @allure.step("Вводим пароль")
    def password(self, text):
        password_input = self.find_element((By.ID, "input-password"))
        password_input.clear()
        password_input.send_keys(text)

    @allure.step("Вводим подтверждение пароля")
    def password_confirm(self, text):
        confirm_input = self.find_element((By.ID, "input-password-confirm"))
        confirm_input.clear()
        confirm_input.send_keys(text)

    @allure.step("Клик на чекбокс")
    def checkbox_name(self):
        self.find_element((By.ID, "input-agree")).click()

    @allure.step("Проверка, что кнопка отправки формы доступна")
    def verify_submit_button_visible(self):
        submit_btn = self.find_visible((By.CSS_SELECTOR, "button.btn-storum-primary"))
        assert submit_btn.is_displayed(), "Кнопка отправки формы не отображается"
        assert submit_btn.is_enabled(), "Кнопка отправки формы недоступна"
