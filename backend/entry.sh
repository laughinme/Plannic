#!/usr/bin/env bash
set -e

cd /app/backend

echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting the application..."
python -m app.main

