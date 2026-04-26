
import time

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class SearchPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    # Локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.input-query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.button-search")
    SEARCH_FORM = (By.CSS_SELECTOR, "form.module-site-search")

    @allure.step("Click search field")
    def click_search_field(self):
        """Кликаем по полю поиска."""
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )
        element.click()
        return self

    @allure.step("Fill search query: {text}")
    def fill_search(self, text):
        """Вводим поисковый запрос."""
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        element.clear()
        element.send_keys(text)
        assert element.get_attribute(
            "value") == text, f"Поисковый запрос не заполнен. Ожидалось: {text}"
        return self

    @allure.step("Click search button")
    def click_search_button(self):
        """Кликаем кнопку поиска."""
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        element.click()
        time.sleep(20)
        return self

    @allure.step("Verify search results")
    def verify_search_results(self):
        """Проверка только заголовка"""

        # Проверяем заголовок h1
        h1_text = self.driver.find_element(By.TAG_NAME, "h1").text
        assert "Кофе" in h1_text, f"Заголовок неверный: {h1_text}"

        # Проверяем что URL содержит search
        assert "search" in self.driver.current_url, "URL не содержит search"

        print("✓ Поиск выполнен успешно")
        return self