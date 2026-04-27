import allure
from pages.registration_pages import RegistrationPage


@allure.epic("Registration")
@allure.feature("User Registration")
@allure.story("Register New User")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("registration", "ui")
@allure.label("owner", "qa_team")
def test_registration_form(setup_browser, site_url):
    registration_page = RegistrationPage(setup_browser, site_url)

    with allure.step('Fill form'):
        registration_page.open()
        registration_page.open_account_menu()
        registration_page.click_register()
        registration_page.fill_first_name("Иван")
        registration_page.fill_last_name("Иванов")
        registration_page.fill_email("ivan_connivance@.mail.ru")
        registration_page.fill_phone("9898989876")
        registration_page.fill_city("Ростов-на-Дону")
        registration_page.fill_street("пр-кт Маршала Жукова")
        registration_page.fill_house("14")
        registration_page.password("12345")
        registration_page.password_confirm("12345")
        registration_page.checkbox_name()
