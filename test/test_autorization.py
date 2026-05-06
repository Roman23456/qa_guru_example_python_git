import allure
from pages.authorization_page import AuthorizationPage


@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "auth")
@allure.id("44018")
@allure.label("owner", "qa_team")
def test_authorization_form(setup_browser, site_url):
    authorization_page = AuthorizationPage(setup_browser, site_url)

    with allure.step('Открытие формы авторизации'):
        authorization_page.open()
        authorization_page.open_account_menu()

    with allure.step('Ввод учётных данных'):
        authorization_page.fill_email()
        authorization_page.fill_password()

    with allure.step('Подтверждение успешной авторизации'):
        authorization_page.password_click()

