import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AboutPage(BasePage):

    @allure.step("Клик на 'О нас' в навигации")
    def open_about(self):
        self.click_element(
            (By.CSS_SELECTOR, "li.menu-item[data-name='about_us'] a.menu-link")
        )
        self.wait.until(EC.url_contains("about"))

    @allure.step("Проверка заголовка страницы")
    def check_heading(self, expected="О НАС"):
        heading = self.find_visible((By.CSS_SELECTOR, "h1.page-heading"))
        assert (
            heading.text.strip() == expected
        ), f"Заголовок: ожидалось '{expected}', получено '{heading.text}'"

    @allure.step("Проверка текста описания компании")
    def check_description_text(self):
        text_block = self.find_visible((By.CSS_SELECTOR, "div.my-box p"))
        text = text_block.text
        assert "Storum" in text, f"Текст не содержит 'Storum': {text}"
        assert len(text) > 50, f"Текст слишком короткий: {text}"
        return text
