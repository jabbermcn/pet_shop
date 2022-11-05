from django.urls import path

from blog.views import ContactCreateView, PostListView, PostDetailView

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='detail'),
]
