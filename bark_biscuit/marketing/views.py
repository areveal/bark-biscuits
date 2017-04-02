from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.template import loader

from bark_biscuit import settings


class Home(TemplateView):
    template_name = 'marketing/home.html'
