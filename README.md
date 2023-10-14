# django-app

- virtual-env ; requirements.txt
- django-admin startproject dproject
    - settings.py - BASE_DIR, SECRET, 
    - source .env
    - remove-default-migrations; installed_apps; middleware
- cd dproject; python manage.py startapp dapp
- manage.py check --deploy
