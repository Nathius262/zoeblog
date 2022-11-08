from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog/<slug>/', BlogPostViewSet.as_view(), name='api_blog_detail'),
    path('blog/create', create_post_view, name='api_blog_create'),
    path('blog/', BlogPostViewSet.as_view(), name='api_blog'),
]