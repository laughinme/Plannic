# bot/Dockerfile
FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false

# Устанавливаем только "bot" (+ базовые) зависимости
RUN poetry install --no-interaction --no-ansi --only bot --no-root

COPY bot /app/bot

CMD ["poetry", "run", "python", "bot/main.py"]