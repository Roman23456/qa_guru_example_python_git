import allure

from pages.favorites_page import ProductFavoritesPage


@allure.epic("Favorites")
@allure.feature("Add to Favorites")
@allure.story("Add Product to Favorites")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("favorites", "ui")
@allure.label("owner", "qa_team")
def test_add_product_to_favorites(perform_search, site_url):
    favorites_page = ProductFavoritesPage(perform_search, site_url)

    with allure.step("Добавляем товар в избранное"):
        favorites_page.test_add_remove_favorites_flow()
