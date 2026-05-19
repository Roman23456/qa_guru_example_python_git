# Проект автоматизации тестирования интернет-гипермаркета STORUM

> **STORUM** — сервис доставки продуктов и сопутствующих товаров для дома, офиса или дачи.
> Сайт: [storum.ru](https://storum.ru/)

![STORUM](image/image.png)

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
| 4 | **Корзина** | Добавление товара в корзину и проверка наличия в корзине | `NORMAL` |
| 5 | **Корзина** | Очистка корзины с подтверждением и проверка пустой корзины | `NORMAL` |
| 6 | **Бренды** | Переход на страницу бренда и добавление товара в корзину | `NORMAL` |
| 7 | **Категории** | Добавление товара через меню категорий | `NORMAL` |
| 8 | **Доставка** | Выбор города доставки из выпадающего списка | `MINOR` |
| 9 | **Контакты** | Заполнение формы обратной связи и проверка поля сообщения | `NORMAL` |
| 10 | **Контакты** | Переход на страницу реквизитов и проверка содержимого | `MINOR` |

---

## Технологический стек

<table align="center">
  <tr>
    <td align="center"><a href="https://www.python.org/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50"/></a><br/>Python</td>
    <td align="center"><a href="https://pytest.org/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" width="50"/></a><br/>Pytest</td>
    <td align="center"><a href="https://www.selenium.dev/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="50"/></a><br/>Selenium</td>
    <td align="center"><a href="https://allurereport.org/"><img src="https://github.com/allure-framework.png" width="50"/></a><br/>Allure</td>
    <td align="center"><a href="https://www.jenkins.io/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="50"/></a><br/>Jenkins</td>
    <td align="center"><a href="https://aerokube.com/selenoid/"><img src="https://github.com/aerokube.png" width="50"/></a><br/>Selenoid</td>
    <td align="center"><a href="https://telegram.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="50"/></a><br/>Telegram</td>
  </tr>
</table>

| Инструмент | Назначение |
|-----------|-----------|
| **Python 3.11** | Язык программирования |
| **Pytest** | Тест-фреймворк: запуск тестов, фикстуры, параметризация |
| **Selenium WebDriver** | Управление браузером в UI-тестах |
| **Page Object Model** | Архитектурный паттерн изоляции UI-логики |
| **Faker** | Генерация случайных тестовых данных |
| **Allure Report** | Формирование наглядных отчётов о прогоне |
| **Allure TestOps** | Управление тест-кейсами и история запусков |
| **Jenkins** | CI/CD: автоматический запуск тестов по расписанию и по коммиту |
| **Selenoid** | Удалённый запуск браузеров в Docker-контейнерах |
| **python-dotenv** | Чтение конфигурации из `.env`-файла |
| **Telegram Bot API** | Уведомления о результатах прогона в Telegram-чат |

---

## Структура проекта

```
qa_guru_yandex_example_python_git/
├── pages/                          # Page Objects
│   ├── base_page.py                # Базовый класс с общими методами ожидания
│   ├── authorization_page.py       # Страница авторизации
│   ├── registration_page.py        # Страница регистрации
│   ├── search_page.py              # Поиск
│   ├── cart_page.py                # Корзина
│   ├── brands_page.py              # Страница брендов
│   ├── category_page.py            # Категории товаров
│   ├── city_page.py                # Выбор города доставки
│   └── contacts_page.py            # Страница контактов и реквизитов
├── test/                           # Тесты
│   ├── conftest.py                 # Фикстуры и настройка браузера
│   ├── test_auth.py                # Авторизация и регистрация
│   ├── test_catalog.py             # Поиск, корзина, бренды, категории
│   └── test_navigation.py          # Контакты, доставка
├── utils/
│   ├── attach.py                   # Прикрепление скриншотов, логов, видео к Allure
│   └── config.py                   # Конфигурация через .env
├── .env                            # Переменные окружения (не в git)
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
REGISTRATION_PASSWORD=your_test_password

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
pytest test/test_auth.py -v
```

После прогона открыть Allure-отчёт:
```bash
allure serve allure-results
```

#### Параметры командной строки (pytest CLI)

| Параметр | По умолчанию | Описание |
|---------|-------------|---------|
| `--site-url` | из `SITE_URL` или `https://storum.ru/` | URL тестируемого сайта |
| `--browser` | `chrome` | Браузер (`chrome`, `firefox`) |
| `--selenoid-url` | из `SELENOID_URL` | URL Selenoid для удалённого запуска |
| `--headless` | `False` | Запуск без графического интерфейса |

#### Параметры через переменные окружения (`.env`)

| Переменная | По умолчанию | Описание |
|-----------|-------------|---------|
| `SITE_URL` | `https://storum.ru/` | URL тестируемого сайта |
| `SELENOID_URL` | — | URL Selenoid |
| `BROWSER_VERSION` | `128.0` | Версия браузера |
| `WINDOW_WIDTH` | `1920` | Ширина окна браузера |
| `WINDOW_HEIGHT` | `1080` | Высота окна браузера |
| `LOGIN_USER` | — | Email для авторизации |
| `PASSWORD_USER` | — | Пароль для авторизации |
| `REGISTRATION_PASSWORD` | — | Пароль для тестовой регистрации |

---

### Удалённый запуск в Jenkins

> [Открыть проект в Jenkins](https://jenkins.autotests.cloud/job/qa_guru_example/)

![Jenkins](image/image-1.png)

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

> [Открыть пример Allure-отчёта](https://jenkins.autotests.cloud/job/qa_guru_example/allure/)

По завершении прогона формируется Allure-отчёт с детальной информацией о каждом тесте.

![Allure Report](image/img.png)

Каждый тест содержит:
- Пошаговое описание выполненных действий
- Скриншот состояния браузера на момент завершения теста
- HTML-код страницы
- Логи браузерной консоли
- Видеозапись прогона (при запуске через Selenoid)

![Allure Report Details](image/image-3.png)

---

## Интеграция с Allure TestOps

> [Открыть запуск в Allure TestOps](https://allure.autotests.cloud/launch/52702/tree/776703)

Результаты синхронизируются с **Allure TestOps** — системой управления тестами, которая позволяет отслеживать историю запусков, анализировать статистику и управлять тест-кейсами.

---

## Telegram-уведомления

После каждого завершённого прогона Telegram-бот автоматически отправляет в чат сообщение с результатами:

- Количество пройденных и упавших тестов
- Ссылка на Allure-отчёт

![alt text](image/image-5.png)

> Уведомление приходит независимо от результата — как при 100% passed, так и при наличии упавших тестов.


[def]: image/img_2.png