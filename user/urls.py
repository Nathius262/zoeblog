from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import AccountSitemap
from .views import *

app_name = 'user'

sitemaps = {
    'user':AccountSitemap
}

urlpatterns = [
    path('screen-mode/', screen_mode_view, name='screen_mode'),
    path('account/authenticate/', must_authenticate_view, name='must_authenticate'),
    path('settings', account_view, name="settings"),
    path('<user>/', profile_view, name="profile"),
    path('follow', follow_view, name="follows"),
    path('get/follow/', follow_view_get, name="getfollower"),
    path('login/status', login_status_view, name="login_status"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]