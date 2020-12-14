venv
install django gunicorn
django-admin startprject 
cd to project
git init
in settings.py add '*' to allowed hosts, add STATIC_ROOT = os.path.join(BASE_DIR, 'static') and import os
add runtime.txt (python-3.7.6
)
add procfile (web: gunicorn janzak.wsgi:application --log-file -)
pip freez > requirements txt

on heroku:
