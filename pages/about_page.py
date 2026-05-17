import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AboutPage(BasePage):

    @allure.step("Клик на 'О нас' в навигации")
    def open_about(self):
        link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "li.menu-item[data-name='about_us'] a.menu-link")
            )
        )
        link.click()
        self.wait.until(EC.url_contains("about"))

    @allure.step("Проверка заголовка страницы")
    def check_heading(self, expected="О НАС"):
        heading = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.page-heading"))
        )
        assert (
            heading.text.strip() == expected
        ), f"Заголовок: ожидалось '{expected}', получено '{heading.text}'"

    @allure.step("Проверка текста описания компании")
    def check_description_text(self):
        text_block = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.my-box p"))
        )
        text = text_block.text
        assert "Storum" in text, f"Текст не содержит 'Storum': {text}"
        assert len(text) > 50, f"Текст слишком короткий: {text}"
        return text
