import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class CartPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=50)

    @allure.step("Добавляет товар в корзину по ID")
    def add_to_cart(self, product_id: str):
        """
        Добавляет конкретный товар в корзину по его ID.
        """
        locator = (
            By.XPATH,
            f"//div[@class='add-to-cart-bar' and @data-product-id='{product_id}']//a["
            f"@class='button-add-to-cart']"
        )

        add_button = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(locator)
        )
        add_button.click()
        notification = WebDriverWait(self.driver, timeout=50).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.storum-notification")
            )
        )
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"
        assert "добавлен" in notification.text.lower(), \
            f"Неверное уведомление: {notification.text}"

        return self
