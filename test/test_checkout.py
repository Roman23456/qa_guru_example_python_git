import allure
from pages.checkout_page import CheckoutPage


@allure.epic("Checkout")
@allure.feature("Order Checkout")
@allure.story("Complete Order Checkout")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("checkout", "ui")
@allure.label("owner", "qa_team")
def test_checkout_order(cart_with_product, site_url):
    checkout_page = CheckoutPage(cart_with_product, site_url)

    with allure.step("Переход в корзину и оформление заказа"):
        checkout_page.open_cart()
        checkout_page.proceed_to_checkout()
        checkout_page.click_continue_address()
        checkout_page.click_continue_replacement()
        checkout_page.click_confirm_order()
