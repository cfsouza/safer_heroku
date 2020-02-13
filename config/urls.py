"""hprod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
try:
    if os.environ["DEBUG"]:
        from config.settings.base import INSTALLED_APPS
        if 'debug_toolbar' in INSTALLED_APPS:
            import debug_toolbar
            urlpatterns = [
                              path('__debug__/', include(debug_toolbar.urls)),
                          ] + urlpatterns
except KeyError:
    pass # if DEBUG is absent code is interpreted in production environment
