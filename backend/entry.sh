#!/usr/bin/env bash
set -e

cd /app/backend

echo "Running Alembic migrations..."
alembic upgrade head

cd app

echo "Starting the application..."
python main.py

