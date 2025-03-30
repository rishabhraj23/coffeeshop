#!/bin/bash
# Run collectstatic to gather static files for production
source /var/app/venv/*/bin/activate
cd /var/app/current
python3 manage.py collectstatic --noinput
