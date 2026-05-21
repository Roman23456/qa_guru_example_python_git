import allure

from pages.city_page import CityPage
from pages.contacts_page import ContactsPage
from utils.config import env_config


@allure.epic("Contacts")
@allure.feature("Contact Form")
@allure.story("Fill contact form and verify message content")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("contacts", "form", "ui")
@allure.label("owner", "qa_team")
def test_contact_form(authorized_driver):
    contacts_page = ContactsPage(authorized_driver, env_config.site_url)

    with allure.step("Открываем страницу 'Контакты'"):
        contacts_page.open()
        contacts_page.open_contacts()

    with allure.step("Заполняем форму обратной связи"):
        contacts_page.fill_message("Тестовое сообщение для проверки формы")

    with allure.step("Проверяем, что сообщение заполнено"):
        contacts_page.check_message_filled("Тестовое сообщение для проверки формы")


@allure.epic("Contacts")
@allure.feature("Contacts Page")
@allure.story("Navigate to Contacts and verify Requisites page")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("contacts", "requisites", "ui")
@allure.label("owner", "qa_team")
def test_contacts_requisites(setup_browser):
    contacts_page = ContactsPage(setup_browser, env_config.site_url)

    with allure.step("Открываем главную страницу"):
        contacts_page.open()

    with allure.step("Переходим на страницу 'Контакты'"):
        contacts_page.open_contacts()

    with allure.step("Переходим в 'Реквизиты организации'"):
        contacts_page.open_requisites()

    with allure.step("Проверяем заголовок страницы"):
        contacts_page.check_requisites_heading("Реквизиты организации")

    with allure.step("Проверяем содержимое реквизитов"):
        contacts_page.check_requisites_content()


@allure.epic("Delivery")
@allure.feature("Set Delivery City")
@allure.story("Select Delivery City")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("delivery", "ui")
@allure.id("44022")
@allure.label("owner", "qa_team")
def test_set_delivery_city(setup_browser):
    city_page = CityPage(setup_browser, env_config.site_url)

    with allure.step("Открываем сайт"):
        city_page.open()

    with allure.step("Выбираем город доставки"):
        city_page.select_city_from_dropdown("Ростов-на-Дону")

    with allure.step("Проверяем, что город выбран"):
        city_page.verify_city_selected("Ростов-на-Дону")
