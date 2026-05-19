import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ContactsPage(BasePage):

    @allure.step("Клик на 'Контакты' в навигации")
    def open_contacts(self):
        self.click_element((By.CSS_SELECTOR, "li.menu-item[data-name='contact'] a.menu-link"))
        self.wait.until(EC.url_contains("contact"))

    @allure.step("Клик на кнопку 'Реквизиты организации'")
    def open_requisites(self):
        self.click_element((By.CSS_SELECTOR, "a.btn.btn-storum-primary.text-uppercase[href*='requisites']"))
        self.wait.until(EC.url_contains("requisites"))

    @allure.step("Проверка заголовка страницы реквизитов")
    def check_requisites_heading(self, expected="Реквизиты организации"):
        heading = self.find_visible((By.CSS_SELECTOR, "h1"))
        assert heading.text.strip() == expected, (
            f"Заголовок: ожидалось '{expected}', получено '{heading.text}'"
        )

    @allure.step("Проверка текста реквизитов")
    def check_requisites_content(self):
        content = self.find_visible((By.CSS_SELECTOR, "div.condensed-text"))
        text = content.text
        assert "СТОРУМ" in text, f"Текст не содержит 'СТОРУМ': {text}"
        assert "ИНН" in text, f"Текст не содержит 'ИНН': {text}"
        return text
