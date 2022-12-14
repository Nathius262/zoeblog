"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import HomeStaticSitemap
from django.views.generic.base import TemplateView #import TemplateView

from home.views import (
    home_screen_view,
    search_view,
    GoogleVerifyView,
)

sitemaps = {
    'static': HomeStaticSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),

    path('', home_screen_view, name="home"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('search/', search_view, name='search'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),  #add the robots.txt file
    path("dns.txt",TemplateView.as_view(template_name="dns.txt", content_type="text/plain")),  #add the robots.txt file
    path('googleb1215a559aaa2a13.html', GoogleVerifyView.as_view()),

    path('profile/', include('user.urls', 'user')),
    path('blog/', include('blog.urls', 'blog')),

    # REST FRAMEWORK
    path('api/', include('blog.api.urls', 'blog_api')),
    path('api/', include('user.api.urls', 'user_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)