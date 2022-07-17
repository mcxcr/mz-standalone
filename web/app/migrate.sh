#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@mazorka.com"}
cd /app/

/opt/venvmz/bin/python manage.py migrate --noinput
/opt/venvmz/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
