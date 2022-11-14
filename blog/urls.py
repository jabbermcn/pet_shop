from django.urls import path

from blog.views import ContactCreateView, PostListView, PostDetailView, CommentListView

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('detail/<slug:post_slug>/', PostDetailView.as_view(), name='detail-post'),
]
