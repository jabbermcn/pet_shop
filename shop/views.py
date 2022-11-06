from django.views.generic import TemplateView

from shop.models import Product


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


class ProductTemplateView(ContextMixin, TemplateView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'products'

    @staticmethod
    def get_queryset():
        return Product.objects.all.order_by('price')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductTemplateView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context
