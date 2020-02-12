from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class LaraPageView(TemplateView):
    template_name = 'lara.html'


class MarcosPageView(TemplateView):
    template_name = 'marcos.html'


class HelenaPageView(TemplateView):
    template_name = 'helena.html'
