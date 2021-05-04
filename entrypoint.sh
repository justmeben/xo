#!/bin/bash
python manage.py migrate
gunicorn xo.wsgi:application -w 2 --timeout 300 --access-logfile - --error-logfile - --bind 0.0.0.0:80