"""
Django settings for HomebrewSite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nai66=(f2ddnz&!1hk&zkwboeoz*q%q4m1p8lf@24)64i4*jpo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homebrew',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'HomebrewSite.urls'

WSGI_APPLICATION = 'HomebrewSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homebrew',
<<<<<<< HEAD
        'USER': 'steve',
        'PASSWORD': 'steve123',
        'HOST': 'ec2-54-187-161-116.us-west-2.compute.amazonaws.com',
#         'USER': 'root',
#         'PASSWORD': 'H0meBrew!',
#         'HOST': '127.0.0.1',
=======
        # 'USER': 'steve',
        # 'PASSWORD': 'steve123',
        # 'HOST': 'ec2-54-187-161-116.us-west-2.compute.amazonaws.com',
        'USER': 'root',
        'PASSWORD': 'H0meBrew!',
        'HOST': '127.0.0.1',
>>>>>>> origin/master
        #'HOST': '54.187.161.116',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

<<<<<<< HEAD
AUTH_PROFILE_MODULE = 'homebrew.Profiles'
=======
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
>>>>>>> origin/master
