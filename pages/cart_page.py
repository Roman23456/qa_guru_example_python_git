import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):

    _NOTIFICATION = (By.CSS_SELECTOR, "div.storum-notification")

    @allure.step("Добавляет товар в корзину по ID")
    def add_to_cart(self, product_id: str):
        locator = (
            By.XPATH,
            f"//div[@class='add-to-cart-bar' and @data-product-id='{product_id}']"
            f"//a[@class='button-add-to-cart']",
        )
        self.click_element(locator)

    @allure.step("Проверяет уведомление о добавлении товара")
    def check_add_notification(self):
        notification = self.wait.until(EC.presence_of_element_located(self._NOTIFICATION))
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"
        assert "добавлен" in notification.text.lower(), f"Неверное уведомление: {notification.text}"
        return notification.text
