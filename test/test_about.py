import allure
from pages.about_page import AboutPage


@allure.epic("About")
@allure.feature("About Page")
@allure.story("Navigate to About page and verify content")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("about", "ui")
@allure.label("owner", "qa_team")
def test_about_page(authorized_driver, site_url):
    about_page = AboutPage(authorized_driver, site_url)

    with allure.step("Переход на страницу 'О нас'"):
        about_page.open_about()

    with allure.step("Проверка контента страницы"):
        about_page.check_heading("О НАС")
        about_page.check_description_text()
