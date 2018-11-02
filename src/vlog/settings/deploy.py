from .base import *


DEBUG = False


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
