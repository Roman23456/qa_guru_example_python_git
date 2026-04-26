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
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Переход в корзину")
    def open_cart(self):
        # Кликаем на блок корзины по тексту или классу
        cart_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'module-cart')]//p[contains(text(), 'корзина')]")
            )
        )
        cart_button.click()
        time.sleep(0.5)

    @allure.step("Нажимает кнопку 'Оформить заказ'")
    def proceed_to_checkout(self):
        # Ищем зеленую кнопку "Оформить заказ"
        btn_checkout = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Оформить заказ')]")
            )
        )
        btn_checkout.click()

    @allure.step("Нажимает кнопку 'Продолжить' (выбор адреса)")
    def click_continue_address(self):
        # Ищем кнопку по уникальному ID
        continue_btn = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.ID, "button--checkout-address--continue")
            )
        )
        continue_btn.click()

    @allure.step("Нажимает кнопку 'Продолжить' (выбор замены товара)")
    def click_continue_replacement(self):
        # Ищем кнопку по уникальному ID
        continue_btn = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.ID, "button--checkout-product-replacement--continue")
            )
        )
        continue_btn.click()

        # Ждем, пока появится следующий блок (Способ доставки и оплаты)
        # Его ID видно чуть ниже в HTML: checkout-payment-and-shipping
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.ID, "checkout-payment-and-shipping"))
        )

    @allure.step("Нажимает кнопку 'Оформить заказ' (Финальный шаг)")
    def click_confirm_order(self):
        # 1. Ищем кнопку по уникальному ID
        confirm_btn = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.ID, "button--checkout-confirm")
            )
        )

        # 2. Кликаем
        confirm_btn.click()

        # 3. Ждем завершения (страница "Спасибо" или перенаправление)
        # Обычно после этого URL меняется на .../success
        WebDriverWait(self.driver, timeout=10).until(
            EC.url_contains("success")
        )