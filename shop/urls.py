from django.urls import path

from .views import HomeTemplateView, AboutTemplateView, BaseTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('base/', BaseTemplateView.as_view(), name='base'),
]
