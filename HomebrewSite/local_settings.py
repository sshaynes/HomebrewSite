# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homebrew',
#        'USER': 'steve',
#        'PASSWORD': 'steve123',
#        'HOST': 'ec2-54-187-161-116.us-west-2.compute.amazonaws.com',
         'USER': 'root',
         'PASSWORD': 'H0meBrew!',
         'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Map AngularJS website as a Static folder
STATICFILES_DIRS = (
    BASE_DIR + "/../HomebrewWebsite",
)