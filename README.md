# django-app

- virtual-env ; requirements.txt
- django-admin startproject dproject
    - settings.py - BASE_DIR, SECRET, 
    - source .env
    - remove-default-migrations; installed_apps; middleware
        remove default installed_apps; 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions'
        remove default AutheticationMiddleware
- cd dproject; python manage.py startapp dapp
- manage.py check --deploy
