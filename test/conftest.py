import logging
from dataclasses import dataclass

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.authorization_page import AuthorizationPage
from utils.attach import add_console_logs, add_page_source, add_screenshot, add_video
from utils.config import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


@dataclass
class _BrowserConfig:
    browser: str
    headless: bool
    selenoid_url: str


def pytest_addoption(parser):
    parser.addoption(
        "--site-url",
        action="store",
        default=None,
        help="URL тестируемого сайта (переопределяет SITE_URL из .env)",
    )
    parser.addoption(
        "--selenoid-url",
        action="store",
        default=None,
        help="URL Selenoid для удалённого запуска",
    )
    parser.addoption(
        "--browser", action="store", default="chrome", help="Браузер: chrome, firefox"
    )
    parser.addoption(
        "--browser-version", action="store", default=None, help="Версия браузера"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless " "режиме",
    )


@pytest.fixture(scope="session", autouse=True)
def apply_cli_config(request):
    cli_site_url = request.config.getoption("--site-url")
    if cli_site_url:
        config.site_url = cli_site_url
    cli_browser_version = request.config.getoption("--browser-version")
    if cli_browser_version:
        config.browser_version = cli_browser_version


def _read_browser_config(request) -> _BrowserConfig:
    return _BrowserConfig(
        browser=request.config.getoption("--browser"),
        headless=request.config.getoption("--headless"),
        selenoid_url=request.config.getoption("--selenoid-url") or "",
    )


def _log_config(cfg: _BrowserConfig):
    logger.info("=" * 50)
    logger.info("CONFIGURATION:")
    logger.info(f"  Browser:      {cfg.browser} {config.browser_version}")
    logger.info(f"  Headless:     {cfg.headless}")
    logger.info(f"  Window Size:  {config.window_width}x{config.window_height}")
    logger.info(f"  Selenoid URL: {cfg.selenoid_url or '—'}")
    logger.info(f"  Site URL:     {config.site_url}")
    logger.info("=" * 50)


def _build_options(cfg: _BrowserConfig) -> Options:
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--window-size={config.window_width},{config.window_height}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    if cfg.headless:
        options.add_argument("--headless")
    return options


@pytest.fixture(scope="function")
def setup_browser(request):
    cfg = _read_browser_config(request)
    _log_config(cfg)
    options = _build_options(cfg)

    if cfg.selenoid_url:
        options.capabilities.update(
            {
                "browserName": cfg.browser,
                "browserVersion": config.browser_version,
                "selenoid:options": {"enableVNC": True, "enableVideo": True},
            }
        )
        driver = webdriver.Remote(command_executor=cfg.selenoid_url, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    yield driver

    add_screenshot(driver)
    add_page_source(driver)
    add_console_logs(driver)
    add_video(driver)
    driver.quit()


@pytest.fixture(scope="function")
def authorized_driver(setup_browser):
    auth_page = AuthorizationPage(setup_browser, config.site_url)
    logger.info("Выполняем авторизацию...")
    auth_page.open()
    auth_page.open_account_menu()
    auth_page.fill_email()
    auth_page.fill_password()
    auth_page.password_click()
    logger.info("Авторизация выполнена")
    return setup_browser
