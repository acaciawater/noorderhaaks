"""
Django settings for noorderhaaks project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.append('/home/theo/texelmeet/acaciadata')
SITE_ID = 1


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.acaciadata.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'debug_toolbar',
    'bootstrap3',
    'noorderhaaks',
    'acacia',
    'acacia.data',
]

MIDDLEWARE = [
#     'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'noorderhaaks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'noorderhaaks.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EXPORT_URL = '/export/'
EXPORT_ROOT = os.path.join(BASE_DIR, 'export')

UPLOAD_DATAFILES = 'datafiles' 
UPLOAD_THUMBNAILS = 'thumbnails' 
UPLOAD_IMAGES = 'images' 

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Grapelli admin
GRAPPELLI_ADMIN_TITLE='Noorderhaaks Beheerpagina'

# registration stuff
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/data/'

LOGGING_ROOT = os.path.join(BASE_DIR, 'logs')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'acacia.log'),
            'when': 'D',
            'interval': 1, # every day a new file
            'backupCount': 0,
            'formatter': 'default'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'update': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'update.log'),
            'when': 'D',
            'interval': 1, # every day a new file
            'backupCount': 0,
            'formatter': 'update'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'django.log'),
            'when': 'D',
            'interval': 1, # every day a new file
            'backupCount': 0,
        },
    },
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(name)s: %(message)s'
        },
        'update' : {
            'format': '%(levelname)s %(asctime)s %(datasource)s: %(message)s'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['django'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'acacia': {
            'handlers': ['file',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'noorderhaaks': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'update' : {
            'handlers': ['update', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

from secrets import *
