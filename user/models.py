import os

from PIL import Image
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from my_test_reference import testingImage, create_or_get_path


def image_location(instance, filename):
    file_path = 'profile/user_{username}/profile.jpeg'.format(
        username=str(instance.id), filename=filename,
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not name:
            raise ValueError("Users must have their name")
        if not password:
            raise ValueError("Must secure account with password")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, unique=False)
    picture = models.ImageField(upload_to=image_location, default="default.jpg", null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    login_status = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = MyAccountManager()

    @property
    def picture_url(self):
        try:
            pic = self.picture.url
        except :
            pic = ''
        return pic
    

    def get_absolute_url(self):
        return reverse('profile', args=[self.username])

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=Account)
def save_profile_img(sender, instance, *args, **kwargs):
    SIZE = 300, 300
    if instance.picture:
        pic = Image.open(instance.picture.path)
        try:
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(instance.picture.path)
        except:
            if pic.mode in ("RGBA", 'P'):
                profile_pic = pic.convert("RGB")
                profile_pic.thumbnail(SIZE, Image.LANCZOS)
                profile_pic.save(instance.picture.path)  

def save_profile(sender, instance, **kwargs):
    instance.user.name = instance.extra_data['name']
    picture = instance.get_avatar_url()
    if picture:
        picture_url = f"{picture}"
        #get or create path for user
        path = f'media_cdn/profile/user_{instance.user.id}'
        create_or_get_path(path)

        filename = f'media_cdn/profile/user_{instance.user.id}/profile.jpeg'
        testingImage(picture_url, filename)
        instance.user.picture = f'profile/user_{instance.user.id}/profile.jpeg'
    instance.user.save()

post_save.connect(save_profile, sender=SocialAccount)      



class Follower(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

