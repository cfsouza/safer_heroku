"""
WSGI config for hprod project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

os.environ.get('DJANGO_SETTINGS_MODULE')

app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
sys.path.append(os.path.join(app_path, 'hprod'))

application = get_wsgi_application()
