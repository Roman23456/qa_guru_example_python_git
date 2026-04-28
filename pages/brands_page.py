import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BrandsPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=50)

    @allure.step("Клик на 'Бренды' в навигации")
    def open_brands(self):
        brands_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "li.menu-item[data-name='brands'] a.menu-link")
            )
        )
        brands_link.click()
        self.wait.until(EC.url_contains("brands"))

    @allure.step("Выбор бренда '{brand_name}'")
    def select_brand(self, brand_name: str):
        brand_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[contains(@class,'cl-inh') and normalize-space(text())='{brand_name}']")
            )
        )
        brand_link.click()
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.add-to-cart-bar"))
        )

    @allure.step("Добавление первого товара в корзину")
    def add_first_product_to_cart(self):
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button-add-to-cart"))
        )
        add_btn.click()

    @allure.step("Проверка уведомления о добавлении товара")
    def check_product_added_notification(self):
        notification = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.storum-notification"))
        )
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"
        assert "добавлен" in notification.text.lower(), \
            f"Неверный текст уведомления: {notification.text}"
        return notification.text
