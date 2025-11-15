set -e

python manage.py migrate --noinput
python seed_admin_movies.py || true
python manage.py collectstatic --noinput

exec gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3