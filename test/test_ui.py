import allure

from pages.about_page import AboutPage
from pages.city_page import CityPage
from utils.config import config


@allure.epic("About")
@allure.feature("About Page")
@allure.story("Navigate to About page and verify content")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("about", "ui")
@allure.id("44032")
@allure.label("owner", "qa_team")
def test_about_page(authorized_driver):
    about_page = AboutPage(authorized_driver, config.site_url)

    with allure.step("Переход на страницу 'О нас'"):
        about_page.open_about()

    with allure.step("Проверка контента страницы"):
        about_page.check_heading("О НАС")
        about_page.check_description_text()


@allure.epic("Delivery")
@allure.feature("Set Delivery City")
@allure.story("Select Delivery City")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("delivery", "ui")
@allure.id("44022")
@allure.label("owner", "qa_team")
def test_set_delivery_city(setup_browser):
    city_page = CityPage(setup_browser, config.site_url)

    with allure.step("Открываем сайт"):
        city_page.open()

    with allure.step("Выбираем город доставки"):
        city_page.select_city_from_dropdown("Ростов-на-Дону")

    with allure.step("Проверяем, что город выбран"):
        city_page.verify_city_selected("Ростов-на-Дону")
