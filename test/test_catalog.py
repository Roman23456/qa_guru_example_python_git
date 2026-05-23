import allure

from pages.brands_page import BrandsPage
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.search_page import SearchPage
from utils.config import env_config


@allure.epic("Search")
@allure.feature("Product Search")
@allure.story("Search for Products")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("search", "ui")
@allure.id("44021")
@allure.label("owner", "qa_team")
def test_search(authorized_driver):
    search_page = SearchPage(authorized_driver, env_config.site_url)

    with allure.step("Поиск товара"):
        search_page.click_search_field()
        search_page.fill_search("Кофе")
        search_page.click_search_button()
        search_page.verify_search_results("Кофе")


@allure.epic("Cart")
@allure.feature("Add to Cart")
@allure.story("Add Product to Cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("cart", "ui")
@allure.id("44017")
@allure.label("owner", "qa_team")
def test_add_to_cart(authorized_driver):
    search_page = SearchPage(authorized_driver, env_config.site_url)
    cart_page = CartPage(authorized_driver, env_config.site_url)

    with allure.step("Ищем товар"):
        search_page.fill_search("Кофе")
        search_page.click_search_button()

    with allure.step("Добавляем товар в корзину"):
        cart_page.add_to_cart(product_id="1011525")

    with allure.step("Проверяем, что товар  добавился в корзину"):
        cart_page.open_cart_page()
        cart_page.check_cart_has_items()
        cart_page.check_product_in_cart("1011525")


@allure.epic("Brands")
@allure.feature("Add Product from Brand")
@allure.story("Navigate to brand and add product to cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("brands", "ui")
@allure.id("44033")
@allure.label("owner", "qa_team")
def test_add_product_from_brand(authorized_driver):
    brands_page = BrandsPage(authorized_driver, env_config.site_url)
    cart_page = CartPage(authorized_driver, env_config.site_url)

    with allure.step("Переход на страницу бренда"):
        brands_page.open_brands()
        brands_page.select_brand("BioCos")

    with allure.step("Добавление товара в корзину"):
        product_id = brands_page.add_first_product_to_cart()
        brands_page.check_product_added_notification()

    with allure.step("Проверка наличия товара в корзине"):
        cart_page.open_cart_page()
        cart_page.check_cart_has_items()
        cart_page.check_product_in_cart(product_id)


@allure.epic("Cart")
@allure.feature("Clear Cart")
@allure.story("Clear all products from cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("cart", "ui")
@allure.label("owner", "qa_team")
def test_clear_cart(authorized_driver):
    search_page = SearchPage(authorized_driver, env_config.site_url)
    cart_page = CartPage(authorized_driver, env_config.site_url)

    with allure.step("Ищем товар и добавляем в корзину"):
        search_page.fill_search("Кофе")
        search_page.click_search_button()
        cart_page.add_to_cart(product_id="1011525")
        cart_page.check_add_notification()

    with allure.step("Открываем страницу корзины"):
        cart_page.open_cart_page()

    with allure.step("Очищаем корзину"):
        cart_page.clear_cart()

    with allure.step("Проверяем, что корзина пуста"):
        cart_page.check_cart_is_empty()


@allure.epic("Category")
@allure.feature("Add Product from Category")
@allure.story("Add Product from Category Menu")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("category", "ui")
@allure.id("44016")
@allure.label("owner", "qa_team")
def test_add_product_category(authorized_driver):
    category_page = CategoryPage(authorized_driver, env_config.site_url)
    cart_page = CartPage(authorized_driver, env_config.site_url)

    with allure.step("Добавление товара через категорию"):
        category_page.open_category_menu()
        category_page.select_category("Здоровое питание, экологичные товары")
        category_page.select_subcategory("Вегетарианские продукты")
        category_page.select_subcategory("Бульоны, приправы, специи")
        category_page.add_product_to_cart("279358")
        category_page.check_add_notification()

    with allure.step("Проверка наличия товара в корзине"):
        cart_page.open_cart_page()
        cart_page.check_cart_has_items()
        cart_page.check_product_in_cart("279358")
