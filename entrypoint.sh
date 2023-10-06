#!/bin/bash

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn django_rest.wsgi:application --bind 0.0.0.0:8000