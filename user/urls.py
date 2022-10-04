from django.urls import path
from .views import (
    account_view,
    profile_view,
    follow_view,
    follow_view_get,
    must_authenticate_view,
)

app_name = 'user'

urlpatterns = [
    path('account/authenticate', must_authenticate_view, name='must_authenticate'),
    path('settings', account_view, name="settings"),
    path('<user>/', profile_view, name="profile"),
    path('follow', follow_view, name="follows"),
    path('get/follow/', follow_view_get, name="getfollower"),
]