from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'user'

urlpatterns = [
    path('profile/<username>/settings/', UserProfileSetting.as_view(), name='api_profile_settings'),
    path('profile/<username>/', UserProfileGenericView.as_view(), name='api_profile_detail'),
    path('profile/', UserProfileGenericView.as_view(), name='api_profile_list'),
    path('login/', obtain_auth_token, name='api_login'),
    path('signup/', signup_view, name='api_signup'),
]