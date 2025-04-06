# backend/Dockerfile
FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false
RUN poetry install --only main,api --no-interaction --no-ansi --no-root

COPY backend /app/backend
COPY backend/entry.sh /app/entry.sh

RUN chmod +x /app/entry.sh

EXPOSE 8000

ENTRYPOINT ["/app/entry.sh"]