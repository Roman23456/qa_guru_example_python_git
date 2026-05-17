import allure

from pages.cart_page import CartPage


@allure.epic("Cart")
@allure.feature("Add to Cart")
@allure.story("Add Product to Cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("cart", "ui")
@allure.id("44017")
@allure.label("owner", "qa_team")
def test_add_to_cart(perform_search, site_url):
    cart_page = CartPage(perform_search, site_url)

    with allure.step("Добавляем товар в корзину по ID"):
        cart_page.add_to_cart(product_id="1011525")
