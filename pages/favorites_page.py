import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class ProductFavoritesPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Добавляет товар в избранное")
    def test_add_remove_favorites_flow(self, product_id="1011525"):
        """
         Добавление товара в избранное.
        """
        add_btn_locator = (
            By.CSS_SELECTOR, f"a.button-add-to-wishlist[data-product-id='{product_id}']")
        remove_btn_locator = (
            By.CSS_SELECTOR, f"a.button-remove-from-wishlist[data-product-id='{product_id}']")

        remove_buttons = self.driver.find_elements(*remove_btn_locator)

        if remove_buttons:
            self.driver.execute_script("arguments[0].click();", remove_buttons[0])

        add_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(add_btn_locator)
        )
        add_button.click()

        WebDriverWait(self.driver, timeout=10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".storum-notification"),
                "добавлен в избранное"
            )
        )
