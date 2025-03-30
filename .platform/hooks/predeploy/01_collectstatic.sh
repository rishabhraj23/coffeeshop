#!/bin/bash
# Activate the virtual environment
source /var/app/venv/*/bin/activate

# Navigate to the application directory
cd /var/app/current

# Run collectstatic without input prompt
python3 manage.py collectstatic --noinput
