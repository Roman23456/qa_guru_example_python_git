# Проект автоматизации тестирования интернет-гипермаркета STORUM

> **STORUM** — сервис доставки продуктов и сопутствующих товаров для дома, офиса или дачи.
> Сайт: [storum.ru](https://storum.ru/)

![STORUM](image.png)

---

## Содержание

- [О проекте](#о-проекте)
- [Покрытый функционал](#покрытый-функционал)
- [Технологический стек](#технологический-стек)
- [Структура проекта](#структура-проекта)
- [Запуск тестов](#запуск-тестов)
  - [Локальный запуск](#локальный-запуск)
  - [Удалённый запуск в Jenkins](#удалённый-запуск-в-jenkins)
- [Allure-отчёт](#allure-отчёт)
- [Интеграция с Allure TestOps](#интеграция-с-allure-testops)
- [Telegram-уведомления](#telegram-уведомления)

---

## О проекте

Проект реализует UI-автоматизацию тестирования интернет-гипермаркета **STORUM** с применением паттерна **Page Object Model (POM)**. Тесты запускаются локально или удалённо через **Jenkins** с использованием **Selenoid** в качестве браузерной фермы. Результаты публикуются в **Allure Report** и **Allure TestOps**, а по завершении сборки приходит уведомление в **Telegram** с ссылкой на отчёт.

---

## Покрытый функционал

| # | Функциональная область | Тест | Severity |
|---|----------------------|------|----------|
| 1 | **Авторизация** | Вход в аккаунт по email и паролю | `CRITICAL` |
| 2 | **Регистрация** | Заполнение формы регистрации нового пользователя | `NORMAL` |
| 3 | **Поиск** | Поиск товара через строку поиска и проверка результатов | `NORMAL` |
| 4 | **Корзина** | Добавление товара в корзину по ID | `NORMAL` |
| 5 | **Бренды** | Переход на страницу бренда и добавление товара в корзину | `NORMAL` |
| 6 | **Категории** | Добавление товара через меню категорий | `NORMAL` |
| 7 | **Доставка** | Выбор города доставки из выпадающего списка | `MINOR` |
| 8 | **О нас** | Переход на страницу «О нас» и проверка контента | `MINOR` |

---

## Технологический стек

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" title="Python"/>
  &nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/pytest.svg" width="50" title="Pytest"/>
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="50" title="Selenium"/>
  &nbsp;&nbsp;
  <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="50" title="Allure Report"/>
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="50" title="Jenkins"/>
  &nbsp;&nbsp;
  <img src="https://avatars.githubusercontent.com/u/26328555?s=200&v=4" width="50" title="Selenoid"/>
  &nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="50" title="Telegram"/>
</p>

| Инструмент | Назначение |
|-----------|-----------|
| **Python 3.11** | Язык программирования |
| **Pytest** | Тест-фреймворк |
| **Selenium WebDriver** | Управление браузером |
| **Page Object Model** | Архитектурный паттерн |
| **Allure Report** | Отчётность по тестам |
| **Allure TestOps** | Test-менеджмент система |
| **Jenkins** | CI/CD для автозапуска тестов |
| **Selenoid** | Удалённый запуск браузеров в Docker |
| **python-dotenv** | Управление конфигурацией через `.env` |
| **Telegram Bot API** | Уведомления о результатах прогона |

---

## Структура проекта

```
qa_guru_yandex_example_python_git/
├── pages/                          # Page Objects
│   ├── about_page.py               # Страница «О нас»
│   ├── authorization_page.py       # Страница авторизации
│   ├── brands_page.py              # Страница брендов
│   ├── cart_page.py                # Корзина
│   ├── category_page.py            # Категории товаров
│   ├── city_page.py                # Выбор города
│   ├── registration_pages.py       # Регистрация
│   └── search_page.py              # Поиск
├── test/                           # Тесты
│   ├── conftest.py                 # Фикстуры, настройка браузера, Telegram-уведомления
│   ├── test_about.py
│   ├── test_add_product_from_category_menu.py
│   ├── test_add_to_cart.py
│   ├── test_autorization.py
│   ├── test_brands.py
│   ├── test_registration_form.py
│   ├── test_search.py
│   └── test_set_delivery_city.py
├── utils/
│   └── attach.py                   # Прикрепление скриншотов, логов, видео к Allure
├── .env                            # Переменные окружения (не коммитить!)
├── pytest.ini                      # Конфигурация pytest и Allure
└── requirements.txt                # Зависимости
```

---

## Запуск тестов

### Предварительная настройка

1. Клонировать репозиторий и перейти в него:
```bash
git clone <repo-url>
cd qa_guru_yandex_example_python_git
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Создать файл `.env` в корне проекта:
```env
SITE_URL=https://storum.ru/
LOGIN_USER=your_email@example.com
PASSWORD_USER=your_password

# Опционально — для Telegram-уведомлений
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Опционально — для запуска через Selenoid
SELENOID_URL=https://user:pass@selenoid.example.com/wd/hub
```

---

### Локальный запуск

Запуск всех тестов в Chrome:
```bash
pytest test/ -v
```

Запуск в headless-режиме:
```bash
pytest test/ -v --headless
```

С указанием конкретного браузера и версии:
```bash
pytest test/ -v --browser=chrome --browser-version=128.0
```

Запуск отдельного тест-файла:
```bash
pytest test/test_autorization.py -v
```

После прогона открыть Allure-отчёт:
```bash
allure serve allure-results
```

#### Доступные параметры запуска

| Параметр | По умолчанию | Описание |
|---------|-------------|---------|
| `--site-url` | `https://storum.ru/` | URL тестируемого сайта |
| `--browser` | `chrome` | Браузер (`chrome`, `firefox`) |
| `--browser-version` | `128.0` | Версия браузера |
| `--selenoid-url` | — | URL Selenoid для удалённого запуска |
| `--headless` | `False` | Запуск без графического интерфейса |
| `--window-width` | `1920` | Ширина окна браузера |
| `--window-height` | `1080` | Высота окна браузера |

---

### Удалённый запуск в Jenkins

Проект в Jenkins: [qa_guru_example](https://jenkins.autotests.cloud/job/qa_guru_example/)

![Jenkins](image-1.png)

**Шаги для запуска:**

1. Открыть проект по ссылке выше
2. Нажать **Build with Parameters** в левом меню
3. При необходимости изменить параметры сборки (URL сайта, браузер, версию и т.д.)
4. Нажать **Build**
5. Дождаться завершения сборки
6. Открыть Allure-отчёт по ссылке в результатах сборки

> Перед запуском Jenkins автоматически создаёт файл `.env` в рабочей директории с нужными переменными окружения.

---

## Allure-отчёт

По завершении прогона формируется Allure-отчёт с детальной информацией о каждом тесте.

![Allure Report](image-2.png)

Каждый тест содержит:
- Пошаговое описание выполненных действий
- Скриншот состояния браузера на момент завершения теста
- HTML-код страницы
- Логи браузерной консоли
- Видеозапись прогона (при запуске через Selenoid)

![Allure Report Details](image-3.png)

---

## Интеграция с Allure TestOps

Результаты синхронизируются с **Allure TestOps** — системой управления тестами, которая позволяет отслеживать историю запусков, анализировать статистику и управлять тест-кейсами.

[Открыть запуск в Allure TestOps](https://allure.autotests.cloud/launch/52702/tree/776703)

---

## Telegram-уведомления

После каждого завершённого прогона Telegram-бот автоматически отправляет в чат сообщение с результатами:

- Количество пройденных и упавших тестов
- Ссылка на Allure-отчёт

> Уведомление приходит независимо от результата — как при 100% passed, так и при наличии упавших тестов.
