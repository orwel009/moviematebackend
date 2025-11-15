#!/usr/bin/env bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Running admin seed if needed..."
python manage.py seed_admin_movies || true

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn moviematebackend.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3