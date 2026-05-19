import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CityPage(BasePage):

    @allure.step("Выбор города из выпадающего списка")
    def select_city_from_dropdown(self, city_name):
        city_input = self.find_element((By.CSS_SELECTOR, "input.input-city"))
        city_input.clear()
        city_input.send_keys(city_name)
        self.click_element(
            (By.CSS_SELECTOR, f"div.suggestion-item[data-city-name='{city_name}']")
        )

    @allure.step("Проверка, что город выбран")
    def verify_city_selected(self, city_name: str):
        city_link = self.find_visible((By.CSS_SELECTOR, "a.module-geoip--current-city"))
        assert (
            city_name in city_link.text
        ), f"Ожидался город '{city_name}', получено: '{city_link.text}'"
