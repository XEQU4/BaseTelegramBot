# BaseTelegramBot

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Aiogram](https://img.shields.io/badge/Aiogram-3.20.0+-green)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)

**📄 Этот README также доступен на [English](./README.en.md)**

BaseTelegramBot — это готовый шаблон Telegram-бота на библиотеке **aiogram v3**, разработанный с учетом лучших практик, включающий поддержку нескольких ролей, локализацию, систему хранения данных в PostgreSQL и Redis, а также встроенный планировщик задач APScheduler с поддержкой DI.

## 🖼️ Демонстрация

Немного примерного взаимодейства с ботом:

![Coming soon](https://via.placeholder.com/600x300?text=Telegram+Bot+Demo)

## 🔧 Стек технологий

- **Aiogram 3.20.0+**
- **PostgreSQL** через `asyncpg`
- **Redis** для хранения данных и планировщика задач
- **APScheduler** + `apscheduler-di`
- **Loguru** — продвинутая система логирования
- **pytz**, **python-dotenv**, **sqlalchemy** (минимальное использование)
- **uv** — современный пакетный менеджер Python

## 🛠️ Зависимости

```properties
aiogram>=3.20.0.post0
aiosqlite>=0.21.0
apscheduler>=3.11.0
apscheduler-di>=0.1.0
asyncpg>=0.30.0
dotenv>=0.9.9
loguru>=0.7.3
python-decouple>=3.8
pytz>=2025.2
redis>=6.0.0
ruff>=0.11.7
setuptools>=80.1.0
six>=1.17.0
sqlalchemy>=2.0.40
```

## 🔄 Функционал

- ✅ Поддержка команд `/start` для **админов** и **пользователей**
- ✅ Настройка администраторов через `.env`
- ✅ Поддержка **локализации** (`en`, `ru`) с легкой масштабируемостью
- ✅ Удобное управление **Reply** и **Inline** клавиатурами
- ✅ Подключение **планировщика задач** через Redis с поддержкой DI (через `apscheduler-di`)
- ✅ Хранение пользователей в **PostgreSQL** с автоматическим созданием таблиц

## 🔹 Автоматическое создание таблиц

Файл `app/database/create_tables.py` автоматически создаст все необходимые таблицы при запуске:
- `id BIGINT PRIMARY KEY`
- `username VARCHAR(32)`
- `fullname TEXT`
- `lang VARCHAR(15)`

## 📁 Структура локализации

Тексты разделены по функциональности:

- `app/locales/texts.py`
- `app/keyboards/reply_keyboards/texts.py`
- `app/keyboards/inline_keyboards/texts.py`

## 🌐 Добавление нового языка

Добавьте ключи перевода в:
- `app/locales/texts.py`
- `app/keyboards/reply_keyboards/texts.py`
- `app/keyboards/inline_keyboards/texts.py`

И не забудьте обновить `.env` → `SUPPORTED_LANGS`

## 📚 .env файл

```
# Список ID админов через слэш
ADMINS=123456789/987654321

# Токен Telegram-бота
BOT_TOKEN="your_bot_token_here"

# Строки подключения к Redis
REDIS_URL="redis://user:password@host:port/0"
REDIS_URL_SCHEDULER="redis://user:password@host:port/1"

# Строка подключения к PostgreSQL
POSTGRES_URL="postgres://username:password@host:port/database"

# Поддерживаемые языки и язык по умолчанию
SUPPORTED_LANGS=en,ru
DEFAULT_LANG=en
```

## 📂 Структура проекта
```
├── .github/            # Рабочие процессы и тесты push на GitHub
├── app/                # Основной модуль приложения
│ ├── database/         # Работа с базой данных и создание таблиц
│ ├── errors/           # Обработка ошибок
│ ├── filters/          # Кастомные фильтры
│ ├── handlers/         # Хендлеры команд и сообщений
│ ├── keyboards/        # Inline и reply клавиатуры
│ ├── locales/          # Локализация
│ ├── logger/           # Настройка логгера loguru
│ ├── middlewares/      # Промежуточные модули (middlewares)
│ ├── redis/            # Redis клиент и утилиты
│ ├── scheduler/        # Планировщик задач APScheduler
│ ├── utils/            # Вспомогательные утилиты
│ ├── bot.py            # Точка входа бота
│ ├── config.py         # Загрузка и парсинг переменных окружения
│ ├── dispatcher.py     # Настройка бота, диспетчера
│ └── test.py           # Тестовые вызовы
├── assets/             # Демонстрационные скриншоты и GIF-файлы
├── tests/              # Набор тестов Pytest
├── .env                # Переменные окружения
├── .env.example        # Пример .env
├── docker-compose.yml  # Docker Compose для тестирования локального стека
├── Dockerfile          # Docker конфигурация
├── pyproject.toml      # Зависимости (используется UV)
├── uv.lock             # Лок-файл зависимостей
├── README.ru.md        # Документация проекта (Русский)
└── README.md           # Документация проекта (Английский)
```
## 🚀 Запуск проекта (без Docker)

1. Установи [uv](https://github.com/astral-sh/uv) с браузера или вручную с pip:
   ```bash
   pip install -U uv
   ```
2. Создай виртуальное окружение:
   ```bash
   uv venv
   ```
3. Активируй виртаульное окружение:
   ```bash
   .venv/Scripts/activate
   ```
4. Установи зависимости:
   ```bash
   uv sync
   ```
5. Настрой `.env` файл (см. выше)
6. Запусти Redis и PostgreSQL (создай базу данных вручную)
7. Запусти бота:
   ```bash
   python ./app/bot.py
   ```

## 🐳 Docker запуск

1. Собери образ
   ```bash
   docker build -t telegram-bot .
   ```
2. Запустить контейнер
   ```bash
   docker run -d --env-file .env telegram-bot
   ```

## 🧪 Тестирование

Базовое тестирование включает использование `pytest`.

Запускаем вместе с:
```bash
  uv pip install pytest
  uv run pytest
  ```

## 🐳 В докере (через docker-compose)
```bash
  docker-compose build
  docker-compose run --rm test
  ```

## ✅ Статус проекта

Завершенный шаблон бота, готовый к использованию и расширению под собственные задачи.

## 📝 License

MIT License. See [LICENSE](./LICENSE) for more information.

---

**Автор:** [XEQU](https://github.com/XEQU4)

