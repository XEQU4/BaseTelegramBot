FROM python:3.13-slim

WORKDIR /app
EXPOSE 8008

# Avoid pip timeouts
RUN mkdir -p /etc/pip && echo "[global]\ntimeout = 180\nindex-url = https://pypi.org/simple" > /etc/pip/pip.conf

RUN pip install --upgrade pip

# Optionally install uv (you can keep this if using locally)
RUN pip install --default-timeout=120 --no-cache-dir uv

# Install test deps
RUN pip install pytest

# Copy project files
COPY . .

# Install all project dependencies explicitly
RUN pip install aiogram aiosqlite apscheduler apscheduler-di asyncpg dotenv loguru pytest python-decouple pytz redis ruff setuptools six sqlalchemy pytest-asyncio
RUN pip install -e .

# Optional: confirm installed packages
RUN pip freeze

CMD ["python", "./app/bot.py"]
