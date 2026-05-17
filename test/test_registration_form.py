import allure
from faker import Faker
from pages.registration_pages import RegistrationPage

fake = Faker("ru_RU")


@allure.epic("Registration")
@allure.feature("User Registration")
@allure.story("Register New User")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("registration", "ui")
@allure.id("44020")
@allure.label("owner", "qa_team")
def test_registration_form(setup_browser, site_url):
    registration_page = RegistrationPage(setup_browser, site_url)

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
        registration_page.password("12345")
        registration_page.password_confirm("12345")
        registration_page.checkbox_name()

    with allure.step("Проверка готовности формы к отправке"):
        registration_page.verify_submit_button_visible()
