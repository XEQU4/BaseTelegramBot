# BaseTelegramBot

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Aiogram](https://img.shields.io/badge/Aiogram-3.20.0+-green)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)

**📄 This README is also available in [Russian](./README.ru.md)**

BaseTelegramBot is a ready-made Telegram bot template using **aiogram v3**, developed with best practices in mind. It includes support for multiple roles, localization, PostgreSQL and Redis data storage, and an integrated task scheduler powered by APScheduler with DI support.

## 🖼️ Demo

Here's a sample interaction with the bot:

![Coming soon](assets/sample.png)

## 🔧 Tech Stack

- **Aiogram 3.20.0+**
- **PostgreSQL** via `asyncpg`
- **Redis** for both storage and scheduling
- **APScheduler** + `apscheduler-di`
- **Loguru** — advanced logging system
- **pytz**, **python-dotenv**, **sqlalchemy** (minimally used)
- **uv** — modern Python package manager

## 🛠️ Dependencies

```properties
aiogram>=3.20.0.post0
aiosqlite>=0.21.0
apscheduler>=3.11.0
apscheduler-di>=0.1.0
asyncpg>=0.30.0
dotenv>=0.9.9
loguru>=0.7.3
pytest>=8.3.5
pytest-asyncio>=0.26.0
python-decouple>=3.8
pytz>=2025.2
redis>=6.0.0
ruff>=0.11.7
setuptools>=80.1.0
six>=1.17.0
sqlalchemy>=2.0.40
```

## 🔄 Features

- ✅ `/start` command support for **admins** and **users**
- ✅ Admins managed through `.env`
- ✅ **Localization** support (`en`, `ru`) with scalability
- ✅ Reply and Inline **keyboards** management
- ✅ Integrated **task scheduler** using Redis and DI (via `apscheduler-di`)
- ✅ User data stored in **PostgreSQL**, tables auto-created

## 🔹 Automatic Table Creation

The file `app/database/create_tables.py` automatically creates necessary tables at launch:
- `id BIGINT PRIMARY KEY`
- `username VARCHAR(32)`
- `fullname TEXT`
- `lang VARCHAR(15)`

## 📁 Localization Structure

Texts are grouped by functionality:

- `app/locales/texts.py`
- `app/keyboards/reply_keyboards/texts.py`
- `app/keyboards/inline_keyboards/texts.py`

## 🌐 Adding New Language

Add translation keys to:
- `app/locales/texts.py`
- `app/keyboards/reply_keyboards/texts.py`
- `app/keyboards/inline_keyboards/texts.py`

And update `.env` → `SUPPORTED_LANGS`

## 📚 .env File

```env
# Admin IDs separated by slashes
ADMINS=123456789/987654321

# Telegram bot token
BOT_TOKEN="your_bot_token_here"

# Redis connection strings
REDIS_URL="redis://user:password@host:port/0"
REDIS_URL_SCHEDULER="redis://user:password@host:port/1"

# PostgreSQL connection string
POSTGRES_URL="postgres://username:password@host:port/database"

# Supported and default languages
SUPPORTED_LANGS=en,ru
DEFAULT_LANG=en
```

## 📂 Project Structure

```
├── .github/            # GitHub Actions workflows and tests
├── app/                # Main application module
│ ├── database/         # DB interactions and table creation
│ ├── errors/           # Error handlers
│ ├── filters/          # Custom filters
│ ├── handlers/         # Command and message handlers
│ ├── keyboards/        # Inline and reply keyboards
│ ├── locales/          # Localization
│ ├── logger/           # Loguru logger config
│ ├── middlewares/      # Middlewares
│ ├── redis/            # Redis client and tools
│ ├── scheduler/        # APScheduler logic
│ ├── utils/            # Helper utilities
│ ├── bot.py            # Bot entry point
│ ├── config.py         # Loads env variables
│ ├── dispatcher.py     # Dispatcher and middleware setup
│ └── test.py           # Test script
├── assets/             # Demo screenshots and GIFs
├── tests/              # Pytest test suite
├── .env                # Environment config
├── .env.example        # Sample .env file
├── docker-compose.yml  # Docker Compose for local stack testing
├── Dockerfile          # Docker config
├── pyproject.toml      # Dependencies (for UV)
├── uv.lock             # Lock file
├── README.ru.md        # Project documentation (Russian)
└── README.md           # Project documentation (English)
```

## 🚀 Running the Project (Without Docker)

1. Install [uv](https://github.com/astral-sh/uv):
   ```bash
   pip install -U uv
   ```
2. Create a virtual environment:
   ```bash
   uv venv
   ```
3. Activate the virtual environment:
   ```bash
   .venv/Scripts/activate
   ```
4. Install dependencies:
   ```bash
   uv sync
   ```
5. Configure your `.env` file (see above)
6. Run Redis and PostgreSQL (manually create the DB)
7. Start the bot:
   ```bash
   python ./app/bot.py
   ```

## 🐳 Docker Deployment

1. Build the image:
   ```bash
   docker build -t telegram-bot .
   ```
2. Run the container:
   ```bash
   docker run -d --env-file .env telegram-bot
   ```

## 🧪 Testing

Basic tests are included using `pytest` and `pytest-asyncio`.

---

> ⚠️ **Before running tests in Docker**, make sure:
>
> - Docker Desktop is **installed and running**
> - You see the 🐳 Docker icon in the system tray (Windows/macOS)
> - You can run `docker version` without errors

---

### 🧼 Run Locally (via uv)

```bash
   uv pip install pytest
   uv run pytest
   ```
### 🐳 Run in Docker (via docker-compose)
```bash
   docker-compose build
   docker-compose run --rm test
   ```
Make sure your Dockerfile contains lines like:
```
   RUN pip install pytest pytest-asyncio
   RUN pip install -e .
   ```

> ℹ️ **Note**
> 
> this runs tests only. To fully launch the bot with Redis and PostgreSQL, use:
> ```
> docker-compose up --build
> ```

## ✅ Project Status

Fully functional and extensible Telegram bot template.

## 📝 License

MIT License. See [LICENSE](./LICENSE) for more information.

---

**Author:** [XEQU](https://github.com/XEQU4)

