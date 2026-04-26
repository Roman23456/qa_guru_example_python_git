import allure

from pages.search_page import SearchPage


@allure.epic("Search")
@allure.feature("Product Search")
class TestSearch:

    @allure.story("Search for Products")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("search", "ui")
    @allure.label("owner", "qa_team")
    def test_search(self, authorized_driver, site_url):
        search_page = SearchPage(authorized_driver, site_url)

        with allure.step('Search input'):
            search_page.click_search_field()
            search_page.fill_search("Кофе")
            search_page.click_search_button()
            search_page.verify_search_results()
