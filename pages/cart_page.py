import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    @allure.step("Добавляет товар в корзину по ID")
    def add_to_cart(self, product_id: str):
        locator = (
            By.XPATH,
            f"//div[@class='add-to-cart-bar' and @data-product-id='{product_id}']//a["
            f"@class='button-add-to-cart']",
        )
        add_button = self.wait.until(EC.element_to_be_clickable(locator))
        add_button.click()
        notification = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.storum-notification"))
        )
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"
        assert "добавлен" in notification.text.lower(), f"Неверное уведомление: {notification.text}"
        return self
