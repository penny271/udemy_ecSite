"""
Django settings for TemplateProject project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

#- windows、Mac両方対応できるように下記をimport
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#- settings.pyファイルがあるparentのparentのフォルダ => TemplateProjectフォルダを指す
BASE_DIR = Path(__file__).resolve().parent.parent
#- templatesフォルダを読み込む階層を指定する
#- 'DIRS': [], に TEMPLATE_DIRを追加する
TEMPLATE_DIR  = os.path.join(BASE_DIR, 'templates')
#- saticフォルダの場所を指定する - 20220630 lec98
STATIC_DIR = os.path.join(BASE_DIR, 'static')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2$r!1n6f-&ln)6zgqn5)%t*ahg)7j0gb%hoh-@+#^_id5zq+gf'

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
    'TemplateApp',
]

#- 間違えて 'TemplateApp'を MIDDLEWAREの中に入れていたためエラーが起きた - 20220629
# django.core.exceptions.ImproperlyConfigured: WSGI application 'TemplateProject.wsgi.application' could not be loaded; Error importing module.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TemplateProject.urls'

#- 'DIRS': [], に TEMPLATE_DIRを追加する
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'TemplateProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#- lec98 staticフォルダを参照できるようにするには以下の設定が必要!
#! STATICSFILES_DIRSを STATICFILES_DIRSと間違えて記載しており、画像が表示できなかった
# https://tinyurl.com/2bqxzrxc
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static"),
    # STATIC_DIR,
)

#- lec98 staticフォルダに識別子を加える事ができる
#- sample.htmlでファイルの読み込みの際に download/home.css の用に
#- 識別子を加える
STATICSFILES_DIRSを = [
    ('download', STATIC_DIR),
]