import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AuthorizationPage(BasePage):

    _ACCOUNT_MENU = (
        By.XPATH,
        "//a[@class='main-link']//span[@class='fa fa-chevron-down']",
    )
    _EMAIL_INPUT = (By.ID, "input-email")
    _PASSWORD_INPUT = (By.ID, "input-password")
    _SUBMIT_BTN = (By.ID, "button-submit-login-form")
    _ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, 'route=account')]")

    @allure.step("Открыть сайт")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Клик на дропдаун авторизации")
    def open_account_menu(self):
        self.click_element(self._ACCOUNT_MENU)

    @allure.step("Ввод mail")
    def fill_email(self, text=None):
        if text is None:
            text = os.getenv("LOGIN_USER")
        email_input = self.find_element(self._EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(text)

    @allure.step("Ввод пароля")
    def fill_password(self, text=None):
        if text is None:
            text = os.getenv("PASSWORD_USER")
        password_input = self.find_element(self._PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(text)

    @allure.step("Клик на кнопку отправки формы авторизации")
    def click_submit(self):
        self.click_element(self._SUBMIT_BTN)

    @allure.step("Проверка успешной авторизации")
    def verify_authorized(self):
        account_link = self.find_visible(self._ACCOUNT_LINK)
        assert account_link.is_displayed(), "Пользователь не авторизован — ссылка аккаунта не отображается"
