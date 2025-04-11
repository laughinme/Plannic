#!/usr/bin/env bash
set -e

cd /app/backend

echo "Running Alembic migrations..."
alembic upgrade head

echo "Setting up PYTHONPATH..."
export PYTHONPATH=$PYTHONPATH:/app/backend

echo "Starting the application..."
python main.py

