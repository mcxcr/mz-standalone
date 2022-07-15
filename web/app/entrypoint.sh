#!/bin/bash

APP_PORT=${PORT:-8000}
cd /app/
/opt/venvmz/bin/gunicorn --worker-tmp-dir /dev/shm app.wsgi:application --bind "0.0.0.0:${APP_PORT}"