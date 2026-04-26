import pytest
import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from pages.authorization_page import AuthorizationPage
from pages.cart_page import CartPage
from pages.search_page import SearchPage

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

import requests as http_requests

from utils.attach import add_screenshot, add_page_source, add_console_logs, add_video


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not bot_token or not chat_id:
        return

    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    error = len(terminalreporter.stats.get("error", []))
    total = passed + failed + error

    status = "✅ Все тесты прошли" if exitstatus == 0 else "❌ Есть падения"
    text = (
        f"{status}\n"
        f"Всего: {total} | ✅ {passed} | ❌ {failed} | ⚠️ {error}"
    )

    try:
        resp = http_requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={"chat_id": chat_id, "text": text},
            timeout=10,
        )
        logger.info(f"Telegram response: {resp.status_code} {resp.text}")
    except Exception as e:
        logger.error(f"Telegram send failed: {e}")


def pytest_addoption(parser):
    """Добавляем параметры командной строки"""
    parser.addoption("--test-number", action="store", default="1234356")
    parser.addoption("--test-text", action="store", default="wwwwww")
    parser.addoption("--test-password", action="store", default="1234qj")
    parser.addoption("--test-date", action="store", default="10.08.1994")
    parser.addoption("--site-url", action="store",
                     default=os.getenv("SITE_URL") or "https://storum.ru/",
                     help="URL тестируемого сайта")
    parser.addoption("--selenoid-url", action="store", default=os.getenv("SELENOID_URL"),
                     help="URL удаленного браузера (selenoid)")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер: chrome, firefox")
    parser.addoption("--browser-version", action="store", default="128.0",
                     help="Версия браузера")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Запуск в headless режиме")
    parser.addoption("--window-width", action="store", default="1920",
                     help="Ширина окна")
    parser.addoption("--window-height", action="store", default="1080",
                     help="Высота окна")


@pytest.fixture(scope="session")
def site_url(request):
    return request.config.getoption("--site-url")


@pytest.fixture(scope="function")
def authorized_driver(setup_browser, request):
    """Фикстура для авторизованного драйвера"""

    base_url = os.getenv("SITE_URL") or "https://storum.ru"
    auth_page = AuthorizationPage(setup_browser, base_url)

    # Авторизация
    logger.info("Выполняем авторизацию...")
    auth_page.open()
    auth_page.open_account_menu()
    auth_page.fill_email()
    auth_page.fill_password()
    auth_page.password_click()

    logger.info("Авторизация выполнена")
    return setup_browser


@pytest.fixture(scope="function")
def perform_search(authorized_driver):
    """
    Фикстура которая выполняет поиск и возвращает драйвер
    с уже выполненным поиском
    """

    base_url = os.getenv("SITE_URL") or "https://storum.ru"
    search_page = SearchPage(authorized_driver, base_url)

    # Выполняем поиск (можно передать запрос через параметры)
    search_query = "Кофе"
    search_page.fill_search(search_query)
    search_page.click_search_button()

    return authorized_driver


# @pytest.fixture(scope="function")
# def cart_with_product(perform_search, request):
#     """
#     Фикстура, которая добавляет товар в корзину.
#     Возвращает драйвер с уже добавленным товаром в корзине.
#     """
#     base_url = os.getenv("SITE_URL") or "https://storum.ru"
#     cart_page = CartPage(perform_search, base_url)
#
#     # Добавляем товар в корзину
#     cart_page.add_to_cart()
#
#     return perform_search

@pytest.fixture(scope="function")
def cart_with_product(perform_search, request):
    """
    Фикстура, которая добавляет ДВА товара в корзину,
    чтобы общая сумма была > 950 руб.
    Возвращает драйвер с уже добавленными товарами.
    """
    base_url = os.getenv("SITE_URL") or "https://storum.ru"
    cart_page = CartPage(perform_search, base_url)

    # Товар 1: Кофе NESCAFE GOLD Арома 120гр — 832.50 р.
    cart_page.add_to_cart(product_id="1011525")

    # Товар 2: Тот же кофе, но 500г — 2656.00 р. (или любой другой)
    # Можно использовать тот же ID — тогда будет 2 шт одного товара → 1665 р.
    cart_page.add_to_cart(product_id="1011525")  # Или замените на "1011950"

    return perform_search


@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser-version")
    headless = request.config.getoption("--headless")
    window_width = request.config.getoption("--window-width")
    window_height = request.config.getoption("--window-height")
    selenoid_url = request.config.getoption("--selenoid-url")

    # Логирование полученных параметров
    logger.info("=" * 50)
    logger.info("CONFIGURATION:")
    logger.info(f"  Browser: {browser}")
    logger.info(f"  Browser Version: {browser_version}")
    logger.info(f"  Headless: {headless}")
    logger.info(f"  Window Size: {window_width}x{window_height}")
    logger.info(f"  Selenoid URL: {selenoid_url}")
    logger.info(f"  Site URL: {request.config.getoption('--site-url')}")
    logger.info("=" * 50)

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument(f'--window-size={window_width},{window_height}')
    options.add_argument('--disable-blink-features=AutomationControlled')

    if headless:
        options.add_argument('--headless')

    # Логика выбора: удаленный браузер или локальный
    if selenoid_url:
        # Если указан URL селенойда, используем Remote
        selenoid_capabilities = {
            "browserName": browser,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        # Если URL не указан, запускаем локальный Chrome
        driver = webdriver.Chrome(options=options)

    yield driver

    add_screenshot(driver)
    add_page_source(driver)
    add_console_logs(driver)
    add_video(driver)
    driver.quit()