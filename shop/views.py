from django.http import HttpRequest
from django.views.generic import TemplateView

from blog.forms import EmailForm
from shop.models import Product, Client, Professional


class ContextMixin:
    context = {
        'site_title': 'PET SHOP',
        'site_name': 'mikhailouski_n',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://linkedin.com',
        'instagram': 'https://instagram.com',
        'address': 'ул. Старовиленский тракт 28/1, Минск',
        'email': 'jabber_mcn@tut.by',
        'phone': '+375 29 5692410',
        'Get_In_Touch_text': 'Here some text',
        'lorem_ipsum': 'lorem ipsum text for all the project',
        'mission': 'Text for mission',
        'vision': 'Text for vision',
    }

    def post(self, request: HttpRequest):
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)


class HomeTemplateView(ContextMixin, TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data()
        context.update(self.context)
        context['email_form'] = EmailForm()
        context['user'] = self.request.user
        return context


class ServiceTemplateView(ContextMixin, TemplateView):
    template_name = 'shop/service.html'
    context_object_name = 'clients'

    @staticmethod
    def get_queryset():
        return Client.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ServiceTemplateView, self).get_context_data()
        context.update(self.context)
        context['email_form'] = EmailForm()
        context['user'] = self.request.user
        context[self.context_object_name] = self.get_queryset()
        return context


class AboutTemplateView(ContextMixin, TemplateView):
    template_name = 'shop/about.html'
    context_object_name = 'professionals'

    @staticmethod
    def get_queryset():
        return Professional.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context.update(self.context)
        context['email_form'] = EmailForm()
        context['user'] = self.request.user
        context[self.context_object_name] = self.get_queryset()
        return context


class ProductTemplateView(ContextMixin, TemplateView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'products'

    @staticmethod
    def get_queryset():
        return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductTemplateView, self).get_context_data()
        context.update(self.context)
        context['email_form'] = EmailForm()
        context['user'] = self.request.user
        context[self.context_object_name] = self.get_queryset()
        return context
