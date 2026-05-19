import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CategoryPage(BasePage):

    _NOTIFICATION = (By.CSS_SELECTOR, "div.storum-notification")

    @allure.step("Открывает меню категорий")
    def open_category_menu(self):
        catalog_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    ".menu-header, .category-menu-toggle, button.navbar-toggle",
                )
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", catalog_button
        )
        self.driver.execute_script("arguments[0].click();", catalog_button)

    @allure.step("Выбирает категорию из меню")
    def select_category(self, category_name):
        self.click_element(
            (
                By.XPATH,
                f"//div[@class='d-table-cell for-text' and contains(text(), '{category_name}')]",
            )
        )

    @allure.step("Выбирает подкатегорию по названию")
    def select_subcategory(self, subcategory_name: str):
        self.click_element(
            (
                By.XPATH,
                f"//div[@class='subcategory-title' and text()='{subcategory_name}']",
            )
        )

    @allure.step("Добавляет товар в корзину со страницы категории")
    def add_product_to_cart(self, product_id):
        locator = (
            By.XPATH,
            f"//div[@class='add-to-cart-bar' and @data-product-id='{product_id}']"
            f"//a[@class='button-add-to-cart']",
        )
        self.click_element(locator)

    @allure.step("Проверяет уведомление о добавлении товара")
    def check_add_notification(self):
        notification = self.wait.until(
            EC.presence_of_element_located(self._NOTIFICATION)
        )
        assert notification.is_displayed(), "Уведомление о добавлении не появилось"
        assert (
            "добавлен" in notification.text.lower()
        ), f"Неверное уведомление: {notification.text}"
        return notification.text
