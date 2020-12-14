# Heroku Demo App  
Runs at:  
https://janzak.herokuapp.com/

--- 
### Notes

#### Workflow  
Reference: https://stackabuse.com/deploying-django-apps-to-heroku-from-github/

only the subfolder (janzak) of pycharm project is pushed to GitHub


1. venv  
2. install django gunicorn  
3. django-admin startprject 
4. cd to project
5. in settings.py add '*' to allowed hosts, add STATIC_ROOT = os.path.join(BASE_DIR, 'static') and import os
6. add runtime.txt (python-3.7.6)
7. add procfile (web: gunicorn janzak.wsgi:application --log-file -)
8. pip freez > requirements txt
9. git init & push to GitHub

On heroku:
10. new pipeline: sellect git repo
11. new app: create new app
12. deploy master branch


13. debugging:  
heroku logs --tail --app janzak  
heroku restart --app janzak  
heroku ps:scale web=1 --app janzak  
