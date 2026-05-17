import allure

from pages.city_page import CityPage


@allure.epic("Delivery")
@allure.feature("Set Delivery City")
@allure.story("Select Delivery City")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("delivery", "ui")
@allure.id("44022")
@allure.label("owner", "qa_team")
def test_set_delivery_city(setup_browser, site_url):
    city_page = CityPage(setup_browser, site_url)

    with allure.step("Открываем сайт"):
        city_page.open()

    with allure.step("Выбираем город доставки"):
        city_page.select_city_from_dropdown("Ростов-на-Дону")

    with allure.step("Проверяем, что город выбран"):
        city_page.verify_city_selected("Ростов-на-Дону")
