# Create your views here.
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'marketing/home.html'
