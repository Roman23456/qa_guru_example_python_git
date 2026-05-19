import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):

    _NOTIFICATION = (By.CSS_SELECTOR, "div.storum-notification")
    _CART_PAGE_HEADING = (By.CSS_SELECTOR, "h1.simple-page-heading")
    _CLEAR_CART_BTN = (By.CSS_SELECTOR, "a#button-clear-cart")
    _CONFIRM_YES_BTN = (By.CSS_SELECTOR, "a.button-yes.btn.btn-storum-primary")
    _CART_EMPTY_WARNING = (By.CSS_SELECTOR, "div.cart-page--warning-cart-empty")

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

    @allure.step("Открывает страницу корзины")
    def open_cart_page(self):
        self.driver.get(f"{self.base_url}/index.php?route=checkout/cart")
        self.wait.until(EC.presence_of_element_located(self._CART_PAGE_HEADING))

    @allure.step("Очищает корзину")
    def clear_cart(self):
        self.click_element(self._CLEAR_CART_BTN)
        self.click_element(self._CONFIRM_YES_BTN)

    @allure.step("Проверяет, что корзина пуста")
    def check_cart_is_empty(self):
        empty_block = self.wait.until(EC.visibility_of_element_located(self._CART_EMPTY_WARNING))
        assert empty_block.is_displayed(), "Блок 'корзина пуста' не отображается"
