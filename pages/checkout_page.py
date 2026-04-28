import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class CheckoutPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=50)

    @allure.step("Переход в корзину")
    def open_cart(self):
        """
         Оформление заказа.
        """
        cart_button = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, ""'module-cart')]//p[contains(text(), "
                           "'корзина')]")
            )
        )
        cart_button.click()

    @allure.step("Клик на  кнопку 'Оформить заказ'")
    def proceed_to_checkout(self):
        btn_checkout = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Оформить заказ')]")
            )
        )
        btn_checkout.click()

    @allure.step("Клик на  кнопку 'Продолжить' (выбор адреса)")
    def click_continue_address(self):
        continue_btn = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(
                (By.ID, "button--checkout-address--continue")
            )
        )
        continue_btn.click()

    @allure.step("Клик на кнопку 'Продолжить' (выбор замены товара)")
    def click_continue_replacement(self):
        continue_btn = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(
                (By.ID, "button--checkout-product-replacement--continue")
            )
        )
        continue_btn.click()

        WebDriverWait(self.driver, timeout=50).until(
            EC.visibility_of_element_located((By.ID, "checkout-payment-and-shipping"))
        )

    @allure.step("Клик на кнопку 'Оформить заказ' (Финальный шаг)")
    def click_confirm_order(self):
        confirm_btn = WebDriverWait(self.driver, timeout=50).until(
            EC.element_to_be_clickable(
                (By.ID, "button--checkout-confirm")
            )
        )

        confirm_btn.click()

        WebDriverWait(self.driver, timeout=50).until(
            EC.url_contains("success")
        )