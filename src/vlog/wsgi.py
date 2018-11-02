"""
WSGI config for vlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 나중에 deploy 단계에서 wsgi 폴더 만들고 파일 나눌거임
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vlog.settings.local')

application = get_wsgi_application()
