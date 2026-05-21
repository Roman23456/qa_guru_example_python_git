import allure
from faker import Faker

from pages.authorization_page import AuthorizationPage
from pages.registration_page import RegistrationPage
from utils.config import env_config

fake = Faker("ru_RU")


@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "auth")
@allure.id("44018")
@allure.label("owner", "qa_team")
def test_authorization_form(setup_browser):
    authorization_page = AuthorizationPage(setup_browser, env_config.site_url)

    with allure.step("Открытие формы авторизации"):
        authorization_page.open()
        authorization_page.open_account_menu()

    with allure.step("Ввод учётных данных"):
        authorization_page.fill_email()
        authorization_page.fill_password()

    with allure.step("Подтверждение успешной авторизации"):
        authorization_page.click_submit()
        authorization_page.verify_authorized()


@allure.epic("Registration")
@allure.feature("User Registration")
@allure.story("Register New User")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("registration", "ui")
@allure.id("44020")
@allure.label("owner", "qa_team")
def test_registration_form(setup_browser):
    registration_page = RegistrationPage(setup_browser, env_config.site_url)

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.numerify("9#########")

    with allure.step("Открытие формы регистрации"):
        registration_page.open()
        registration_page.open_account_menu()
        registration_page.click_register()

    with allure.step("Заполнение личных данных"):
        registration_page.fill_first_name(first_name)
        registration_page.fill_last_name(last_name)
        registration_page.fill_email(email)
        registration_page.fill_phone(phone)

    with allure.step("Заполнение адреса и пароля"):
        registration_page.fill_city("Ростов-на-Дону")
        registration_page.fill_street("пр-кт Маршала Жукова")
        registration_page.fill_house("14")
        registration_page.password(env_config.registration_password)
        registration_page.password_confirm(env_config.registration_password)
        registration_page.checkbox_name()

    with allure.step("Проверка готовности формы к отправке"):
        registration_page.verify_submit_button_visible()
