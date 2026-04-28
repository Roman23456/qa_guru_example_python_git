
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=50)

    @allure.step("Открываем сайт")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Выбор города из выпадающего списка")
    def select_city_from_dropdown(self, city_name):
        """
         Тест смены города.
        """
        input_field = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.input-city"))
        )
        input_field.clear()
        input_field.send_keys(city_name)
        suggestion_locator = (
            By.CSS_SELECTOR,
            f"div.suggestion-item[data-city-name='{city_name}']"
        )

        suggestion = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(suggestion_locator)
        )

        suggestion.click()