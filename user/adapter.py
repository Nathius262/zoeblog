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
from profileAccount.models import Account
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        url = "https://zoeblog.pythonanywhere/account/confirm-email/" + emailconfirmation.key
        return url

def get_adapter(request=None):
    """
    The Adapter in app_settings.ADAPTER is set to CustomAccountAdapter.
    """
    return import_attribute(app_settings.ADAPTER)(request)


def pre_save_pre_social_login_receiver(sender, instance, sociallogin, *args, **kwargs):
    instance.picture = sociallogin.account.extra_data.get('picture', None)
    instance.name = 'yes'
    instance.save()


pre_social_login.connect(pre_save_pre_social_login_receiver, sender=Account)
