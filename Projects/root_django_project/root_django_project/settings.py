"""
Django settings for root_django_project project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# importing os
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t4-14w@xh@gri*6g9*r5$lc!ivu+8l8+%14j*xsya0bsi-wu4w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DEBUG = False

# universal allowance of hosting
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'world',

    # custom user model
    'user',

    'templating',
    'modelextra',
    'modelpractice',
    'modelrelation',
    'formspractice',
    'staticmedia',

    'crud',
    'classbased',

    #for login middlwware,cache,mail
    'login',

    # accounts handlig app
    'accounts',

    # status app
    'statusapp',


    #DRF rest app
    'rest',
    'rest_framework',

    # DRF authentication
    # authtoken for rest framework
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # custom middelware
    # 'login.middleware.MyCustomMiddleware',
    # 'root_django_project.middleware.MyCustomMiddleware',
]

ROOT_URLCONF = 'root_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # others location directory of templates like /home/dilli/SSD1/Folder
        ],
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

WSGI_APPLICATION = 'root_django_project.wsgi.application'

# print(BASE_DIR)
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# our custom user model
AUTH_USER_MODEL= 'user.User'


# configurations of static url
# or use this(optional)
# http://127.0.0.1:8000/static-demo-url/main.js
# STATIC_URL = '/static-demo-url/'
# configuring the static root for all staticfiles

STATIC_ROOT = os.path.join(BASE_DIR, 'prod-static')
print(STATIC_ROOT)

# hit ./manage.py collectstatic
# for static server python3 -m http.server

#----Alternative way to store static files--
# for static files to bring all of them
# in a single dirs
# STATICFILES_DIRS = [
#     STATIC_ROOT
# ]


# configurations of media url
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# MailTrap.io settings for django
# Testing mails from django
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = 'e4dc6eab56c062'
# EMAIL_HOST_PASSWORD = '5254e289d31297'
# EMAIL_PORT = '2525'


#tls transport layer security
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'dillihangrae@gmail.com'
# EMAIL_HOST_PASSWORD = 'dilli21April1999@gmail.com'
# EMAIL_PORT = 587

# for loginrequired decorator to work
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'open'
# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = 'accounts/login_view'

