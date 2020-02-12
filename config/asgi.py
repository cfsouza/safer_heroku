"""
ASGI config for hprod project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
sys.path.append(os.path.join(app_path, 'hprod'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_asgi_application()