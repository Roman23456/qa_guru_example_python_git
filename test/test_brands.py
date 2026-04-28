import allure
from pages.brands_page import BrandsPage


@allure.epic("Brands")
@allure.feature("Add Product from Brand")
@allure.story("Navigate to brand and add product to cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("brands", "ui")
@allure.label("owner", "qa_team")
def test_add_product_from_brand(authorized_driver, site_url):
    brands_page = BrandsPage(authorized_driver, site_url)

    with allure.step("Переход на страницу бренда"):
        brands_page.open_brands()
        brands_page.select_brand("Alpina Green")

    with allure.step("Добавление товара в корзину и проверка"):
        brands_page.add_first_product_to_cart()
        brands_page.check_product_added_notification()
