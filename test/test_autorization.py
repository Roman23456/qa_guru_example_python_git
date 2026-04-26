import allure
from pages.authorization_page import AuthorizationPage


@allure.epic("Authentication")
@allure.feature("User Login")
class TestAuthorization:

    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "auth")
    @allure.label("owner", "qa_team")
    def test_authorization_form(self, setup_browser, site_url):
        authorization_page = AuthorizationPage(setup_browser, site_url)

        with allure.step('Authorization form'):
            authorization_page.open()
            authorization_page.open_account_menu()
            authorization_page.fill_email()
            authorization_page.fill_password()
            authorization_page.password_click()
