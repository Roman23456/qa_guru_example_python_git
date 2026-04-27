import allure

from pages.city_page import MainPage


@allure.epic("Delivery")
@allure.feature("Set Delivery City")
@allure.story("Select Delivery City")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("delivery", "ui")
@allure.label("owner", "qa_team")
def test_set_delivery_city(setup_browser, site_url):
    main_page = MainPage(setup_browser, site_url)

    with allure.step('Открываем сайт'):
        main_page.open()

    with allure.step("Вводим в инпут город"):
        main_page.select_city_from_dropdown("Ростов-на-Дону")
