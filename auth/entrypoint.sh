#!/bin/bash

echo "Installing all dependancies and netcat to make a loop that will save few seconds takes too long, so i just sleep 5"
sleep 5

python manage.py migrate
gunicorn auth.wsgi:application -w 2 --timeout 300 --access-logfile - --error-logfile - --bind 0.0.0.0:80