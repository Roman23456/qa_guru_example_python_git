import allure

from pages.category_page import CategoryPage


@allure.epic("Category")
@allure.feature("Add Product from Category")
@allure.story("Add Product from Category Menu")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("category", "ui")
@allure.label("owner", "qa_team")
def test_add_product_category(authorized_driver, site_url):
    category_page = CategoryPage(authorized_driver, site_url)

    with allure.step('Add product to cart'):
        category_page.open_category_menu()
        category_page.select_category("Здоровое питание, экологичные товары")
        category_page.select_subcategory("Вегетарианские продукты")
        category_page.select_subcategory_2("Бульоны, приправы, специи")
        category_page.add_product_to_cart("279358")
