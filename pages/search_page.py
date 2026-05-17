import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_INPUT = (By.CSS_SELECTOR, "input.input-query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.button-search")
    SEARCH_FORM = (By.CSS_SELECTOR, "form.module-site-search")

    @allure.step("Click search field")
    def click_search_field(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        element.click()
        return self

    @allure.step("Fill search query: {text}")
    def fill_search(self, text):
        element = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        element.clear()
        element.send_keys(text)
        assert (
            element.get_attribute("value") == text
        ), f"Поисковый запрос не заполнен. Ожидалось: {text}"
        return self

    @allure.step("Click search button")
    def click_search_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        element.click()
        self.wait.until(EC.url_contains("search"))
        return self

    @allure.step("Verify search results")
    def verify_search_results(self):
        h1 = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        assert "Кофе" in h1.text, f"Заголовок неверный: {h1.text}"
        assert "search" in self.driver.current_url, "URL не содержит search"
        return self
