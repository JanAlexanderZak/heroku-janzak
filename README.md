only subfolder janzak is pushed to git

https://stackabuse.com/deploying-django-apps-to-heroku-from-github/
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
new pipeline: sellect git repo
new app: create new app
deploy master branch


debugging:
heroku logs --tail --app janzak
heroku restart --app janzak
heroku ps:scale web=1 --app janzak
