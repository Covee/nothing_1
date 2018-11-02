from .base import *


# local 환경에서 개발할 때, 매번 "python manage.py runserver --settings=vlog.settings.local" 해주기 번거로우니
# 환경변수를 설정해준다.
# export DJANGO_SETTINGS_MODULE=vlog.settings.local
# echo $DJANGO_SETTINGS_MODULE


DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# 개발환경에 맞게 경로 설정 다르게 해줘야 하므로 일단 옮겨둠
# WSGI_APPLICATION = 'vlog.wsgi.application'
