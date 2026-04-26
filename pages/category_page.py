import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class CategoryPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Открывает меню категорий")
    def open_category_menu(self):
        # Иконка гамбургера или кнопка с классом
        catalog_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".menu-header, .category-menu-toggle, button.navbar-toggle")
            )
        )
        catalog_button.click()
        time.sleep(0.5)

    @allure.step("Выбирает категорию из меню")
    def select_category(self, category_name):
        category_item = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//div[@class='d-table-cell for-text' and contains(text(), '{category_name}')]")
            )
        )
        category_item.click()

    @allure.step("Выбирает подкатегорию по названию")
    def select_subcategory(self, subcategory_name: str):
        subcategory = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='subcategory-title' and text()='{subcategory_name}']")
            )
        )
        subcategory.click()
        time.sleep(3)

    @allure.step("Выбирает подкатегорию по названию")
    def select_subcategory_2(self, subcategory_name: str):
        subcategory = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='subcategory-title' and text()='{subcategory_name}']")
            )
        )
        subcategory.click()

    @allure.step("Добавляет товар в корзину со страницы категории")
    def add_product_to_cart(self, product_id):
        # Локатор кнопки "В корзину" внутри блока конкретного товара
        cart_btn_locator = (
            By.XPATH,
            f"//div[@class='add-to-cart-bar' and @data-product-id='{product_id}']//a["
            f"@class='button-add-to-cart']"
        )
        cart_btn = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(cart_btn_locator)
        )
        cart_btn.click()

        # Проверка: появилось уведомление об успешном добавлении
        notification = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.storum-notification")
            )
        )
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"

        # Проверка: в уведомлении есть текст "добавлен в корзину"
        notification_text = notification.text
        assert "добавлен" in notification_text.lower(), \
            f"Неверное уведомление: {notification_text}"

        return self
