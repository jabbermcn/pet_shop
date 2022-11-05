from django.http import HttpRequest
from django.views.generic import TemplateView

from blog.forms import ContactForm


class ContextMixin:
    context = {
        'site_title': 'PET SHOP - Pet Shop Website',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
    }


class HomeTemplateView(ContextMixin, TemplateView):
    template_name = 'shop/home.html'


class BaseTemplateView(ContextMixin, TemplateView):
    template_name = 'shop/base.html'


class AboutTemplateView(ContextMixin, TemplateView):
    template_name = 'shop/about.html'



