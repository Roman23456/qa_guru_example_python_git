import os
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthorizationPage(BasePage):

    @allure.step("Открыть сайт")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Клик на дропдаун авторизации")
    def open_account_menu(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='main-link']//span[@class='fa fa-chevron-down']")
            )
        )
        element.click()

    @allure.step("Ввод mail")
    def fill_email(self, text=None):
        if text is None:
            text = os.getenv("LOGIN_USER")

        element = self.wait.until(
            EC.presence_of_element_located((By.ID, "input-email"))
        )
        element.clear()
        element.send_keys(text)
        assert element.get_attribute("value") == text, f"Email не заполнен. Ожидалось: {text}"

    @allure.step("Ввод пароля")
    def fill_password(self, text=None):
        if text is None:
            text = os.getenv("PASSWORD_USER")

        element = self.wait.until(
            EC.presence_of_element_located((By.ID, "input-password"))
        )
        element.clear()
        element.send_keys(text)
        assert len(element.get_attribute("value")) > 0, "Пароль не заполнен"

    @allure.step("Клик на кнопку авторизации")
    def password_click(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, "button-submit-login-form"))
        )
        element.click()
