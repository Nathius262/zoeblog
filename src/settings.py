"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'some_random_default_string')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = ['zoeblog.pythonanywhere.com']

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # my installed app
    'user',
    'blog',
    'home',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django_extensions',

    'mptt',

    # ckeditor
    'ckeditor',
    'ckeditor_uploader',
    #'highlightjs',

    # django hitcount
    'hitcount',
    'django_social_share',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'home.views.latest_blog_post',
            ],
        },
    },
]

AUTH_USER_MODEL = 'user.Account'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
    os.path.join(BASE_DIR, "media/"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

<<<<<<< HEAD
=======

>>>>>>> 1bd82d9750aae4694d6280228c77092404fdb174
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'blogzoe18@gmail.com' #sender's email-id
DEFAULT_FROM_EMAIL = 'blogzoe18@gmail.com'
SERVER_EMAIL = 'blogzoe18@gmail.com'
EMAIL_HOST_PASSWORD = 'etzauornsuhmeutv' #password associated with above email-id


#ACCOUNT_ADAPTER = 'user.adapter.CustomAccountAdapter'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
<<<<<<< HEAD
=======

# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
>>>>>>> 1bd82d9750aae4694d6280228c77092404fdb174

LOGIN_REDIRECT_URL = "/account/profile/"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_FORMS = {'signup': 'user.forms.RegistrationForm'}
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/account/login'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SESSION_REMEMBER = True

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# SOCIALACCOUNT_ADAPTER = 'profileAccount.adapter.SocialAdapter'

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True

# ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'office2013',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,

        'extraPlugins': ','.join([
            'html5video',
            'video',
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            #'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
            'mathjax',
        ]),
    }
}