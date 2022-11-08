from django.urls import path

from .views import HomeTemplateView, AboutTemplateView, ProductTemplateView, ServiceTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('product/', ProductTemplateView.as_view(), name='product'),
    path('service/', ServiceTemplateView.as_view(), name='service'),
]
