import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):

    _SEARCH_INPUT = (By.CSS_SELECTOR, "input.input-query")
    _SEARCH_BUTTON = (By.CSS_SELECTOR, "button.button-search")

    @allure.step("Клик по полю поиска")
    def click_search_field(self):
        self.click_element(self._SEARCH_INPUT)

    @allure.step("Ввод поискового запроса: {text}")
    def fill_search(self, text):
        search_input = self.find_element(self._SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(text)
        assert search_input.get_attribute("value") == text, f"Поисковый запрос не заполнен. Ожидалось: {text}"

    @allure.step("Нажать кнопку поиска")
    def click_search_button(self):
        self.click_element(self._SEARCH_BUTTON)
        self.wait.until(EC.url_contains("search"))

    @allure.step("Проверка результатов поиска")
    def verify_search_results(self):
        h1 = self.find_visible((By.TAG_NAME, "h1"))
        assert "Кофе" in h1.text, f"Заголовок неверный: {h1.text}"
        assert "search" in self.driver.current_url, "URL не содержит search"
