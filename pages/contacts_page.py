import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ContactsPage(BasePage):

    _CONTACT_MESSAGE = (By.ID, "input-contact-message")
    _CONTACT_SUBMIT = (By.ID, "button-send-contact-form")

    @allure.step("Клик на 'Контакты' в навигации")
    def open_contacts(self):
        self.click_element(
            (By.CSS_SELECTOR, "li.menu-item[data-name='contact'] a.menu-link")
        )
        self.wait.until(EC.url_contains("contact"))

    @allure.step("Клик на кнопку 'Реквизиты организации'")
    def open_requisites(self):
        self.click_element(
            (
                By.CSS_SELECTOR,
                "a.btn.btn-storum-primary.text-uppercase[href*='requisites']",
            )
        )
        self.wait.until(EC.url_contains("requisites"))

    @allure.step("Проверка заголовка страницы реквизитов")
    def check_requisites_heading(self, expected="Реквизиты организации"):
        heading = self.find_visible((By.CSS_SELECTOR, "h1"))
        assert (
            heading.text.strip() == expected
        ), f"Заголовок: ожидалось '{expected}', получено '{heading.text}'"

    @allure.step("Проверка текста реквизитов")
    def check_requisites_content(self):
        content = self.find_visible((By.CSS_SELECTOR, "div.condensed-text"))
        text = content.text
        assert "СТОРУМ" in text, f"Текст не содержит 'СТОРУМ': {text}"
        assert "ИНН" in text, f"Текст не содержит 'ИНН': {text}"
        return text

    @allure.step("Заполняет поле сообщения: {message}")
    def fill_message(self, message: str):
        msg_input = self.find_element(self._CONTACT_MESSAGE)
        msg_input.clear()
        msg_input.send_keys(message)

    @allure.step("Проверяет, что сообщение заполнено")
    def check_message_filled(self, expected: str):
        msg_input = self.find_element(self._CONTACT_MESSAGE)
        actual = msg_input.get_attribute("value")
        assert (
            actual == expected
        ), f"Сообщение не заполнено. Ожидалось: '{expected}', получено: '{actual}'"
