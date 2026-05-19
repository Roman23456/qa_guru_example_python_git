import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class BrandsPage(BasePage):

    _NOTIFICATION = (By.CSS_SELECTOR, "div.storum-notification")

    @allure.step("Клик на 'Бренды' в навигации")
    def open_brands(self):
        self.click_element(
            (By.CSS_SELECTOR, "li.menu-item[data-name='brands'] a.menu-link")
        )
        self.wait.until(EC.url_contains("brands"))

    @allure.step("Выбор бренда '{brand_name}'")
    def select_brand(self, brand_name: str):
        self.click_element(
            (
                By.XPATH,
                f"//a[contains(@class,'cl-inh') and normalize-space(text())='{brand_name}']",
            )
        )
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.add-to-cart-bar"))
        )

    @allure.step("Добавление первого товара в корзину")
    def add_first_product_to_cart(self):
        self.click_element(
            (
                By.CSS_SELECTOR,
                "div.add-to-cart-bar[data-opt='0'] " "a.button-add-to-cart",
            )
        )

    @allure.step("Проверка уведомления о добавлении товара")
    def check_product_added_notification(self):
        notification = self.find_visible(self._NOTIFICATION)
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"
        assert (
            "добавлен" in notification.text.lower()
        ), f"Неверный текст уведомления: {notification.text}"
        return notification.text
