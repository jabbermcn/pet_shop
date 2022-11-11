from django.views.generic import ListView, DetailView, CreateView

from blog.forms import ContactForm, EmailForm
from blog.models import Post, Comment


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
        'Get_In_Touch_text': 'Here some text'
    }


class PostListView(ContextMixin, ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('date_published')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context


class CommentListView(ContextMixin, ListView):
    model = Comment
    template_name = 'blog/detail.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(is_published=True).order_by('date_published')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommentListView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context


class PostDetailView(ContextMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context


class ContactCreateView(ContextMixin, CreateView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data()
        context.update(self.context)
        context['contact_form'] = ContactForm()
        context['email_form'] = EmailForm()
        context['user'] = self.request.user
        return context
