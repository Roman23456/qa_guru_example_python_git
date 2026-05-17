import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CityPage(BasePage):

    @allure.step("Выбор города из выпадающего списка")
    def select_city_from_dropdown(self, city_name):
        input_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.input-city"))
        )
        input_field.clear()
        input_field.send_keys(city_name)
        suggestion_locator = (By.CSS_SELECTOR, f"div.suggestion-item[data-city-name='{city_name}']")
        suggestion = self.wait.until(EC.element_to_be_clickable(suggestion_locator))
        suggestion.click()

    @allure.step("Проверка, что город выбран")
    def verify_city_selected(self, city_name: str):
        city_link = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.module-geoip--current-city"))
        )
        assert (
            city_name in city_link.text
        ), f"Ожидался город '{city_name}', получено: '{city_link.text}'"
