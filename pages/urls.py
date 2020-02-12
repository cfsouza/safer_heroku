from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('lara/', views.LaraPageView.as_view(), name='lara'),
    path('marcos/', views.MarcosPageView.as_view(), name='marcos'),
    path('helena/', views.HelenaPageView.as_view(), name='helena'),
]