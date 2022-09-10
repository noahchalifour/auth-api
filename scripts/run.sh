#!/bin/sh

./scripts/initialize.sh &
python manage.py runserver 0.0.0.0:8000
