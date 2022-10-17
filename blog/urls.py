from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap
from .views import (

    create_blog_view,
    blog_view,
    CatListView,
    edit_blog_view,
    comment_view,
    delete_post,
    like_view,
    likesCount,
    DetailPostView,
    category_list,
    commet_reply_view

)

app_name = 'blog'

sitemaps = {
    'blog':BlogPostSitemap
}

urlpatterns = [

    path('create/', create_blog_view, name='create'),
    path('<slug>/edit', edit_blog_view, name='edit'),
    path('category/<category>', CatListView.as_view(), name='category'),
    path('get/category/', category_list, name='category_list'),
    path('<slug:slug>/', DetailPostView.as_view(), name='details'),
    path('comment', comment_view, name='comment'),
    path('comment/reply', commet_reply_view, name='comment_reply'),
    path('postLike', like_view, name='like'),
    path('likes', likesCount, name='likesCount'),
    path('delete', delete_post, name='delete_post'),
    path('', blog_view, name='blog'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
