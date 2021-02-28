"""
Django settings for bike project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a71agnv&mmx%@te$!ed!17rj8l&mu6gb-n**@yno*rk98%68@('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bikeapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bike.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'),
                 os.path.join(BASE_DIR, 'static').replace('\\', '/')], #change
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

WSGI_APPLICATION = 'bike.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bikerental',			# Database name
        'USER': 'root',       		    # Username
        'PASSWORD': '123123',           # Password
        'HOST': 'localhost',		    # The default one
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False #New setting


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# When running python manage.py collectstatic 的时候
# STATIC_ROOT folder is used to copy all the file  and the files in static in each app are copied over
# Putting these files together is to make it easier to deploy with apache
# STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
# the file name is static in os.path.join(BASE_DIR, "static")
# os.path.join(BASE_DIR, "common_static")
#Put jquery.js under common_static/js/ so that you can access it in /static/js/jquery.js!
#You can also specify static files shared by all apps in settings.py, such as jquery.js etc. common_static folder
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
    # ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    # ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
    # ('font', os.path.join(STATIC_ROOT, 'font').replace('\\', '/')),
)

#Default setting.
# By default, Django will find files in the folders in STATICFILES_DIRS
# and the static folders under each app
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
