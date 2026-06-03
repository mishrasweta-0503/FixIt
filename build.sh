#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install all required Python packages (including Django, Gunicorn, and WhiteNoise)
pip install -r requirements.txt

# 2. Collect all CSS, Bootstrap, and JS assets into the 'staticfiles' directory
python manage.py collectstatic --no-input

# 3. Apply any new database migrations so your tables stay up to date
python manage.py migrate