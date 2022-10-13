from datetime import date
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account import app_settings
from allauth.utils import import_attribute
from allauth.account.signals import user_signed_up
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import pre_social_login
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Account
from django.conf import settings
from django.shortcuts import redirect
from my_test_reference import testingImage, create_or_get_path



class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save(self, request, sociallogin, form=None):
        super(DefaultSocialAccountAdapter, self).save(request, sociallogin, form=form)
        return redirect('social_profile')

@receiver(user_signed_up)
def retrieve_social_data(request, user, **kwargs):
    """Signal, that gets extra data from sociallogin and put it to profile."""
    # get the profile where i want to store the extra_data
    profile = Account(username=user)
    # in this signal I can retrieve the obj from SocialAccount
    data = SocialAccount.objects.filter(user=user, provider='google')
    # check if the user has signed up via social media
    if data:
        picture = data[0].get_avatar_url()
        if picture:

            image_url = f"{picture}"
            # custom def to save the pic in the profile
            path = f'media_cdn/profile/user_{profile.id}'
            create_or_get_path(path)

            filename = f'media_cdn/profile/user_{profile.id}/profile.jpeg'

            testingImage(image_url, filename)
            name = data[0].extra_data['name']
            profile.name = name
            profile.picture = f'/profile/user_{profile.id}/profile.jpeg'
        profile.save()
        return redirect('blog:blog')
    