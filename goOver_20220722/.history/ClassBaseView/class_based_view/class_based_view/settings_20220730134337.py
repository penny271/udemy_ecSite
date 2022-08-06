"""
Django settings for class_based_view project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from lib2to3.pgen2.literals import simple_escapes
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-8&t+8sx=+#-h(aay^04i7oj6z6&0md%^m6sxpllrh!!-$&$z!g'

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
    'store',
]

MIDDLEWARE = [
    'class_based_view.middleware.PerformanceMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #- 自作middlewareを登録
    # 'class_based_view.middleware.MyMiddleware',
]

ROOT_URLCONF = 'class_based_view.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'class_based_view.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGGING = {
#     'version': 1, # ロガーのバージョン(1でよい)
#     'disable_existing_loggers': False, # デフォルトのログを無効化するかどうか(Falseでよい)
#     'formatters': { # フォーマッターの一覧を記載 },
#         'simple': { # formatter名
#             'format':'%(asctime)s %(levelname)s [%(pathname)s:%(lineno)s] %(message)s', # 形式
#         }
#     },
#     'handlers': { # ハンドラーの一覧を記載
#         'console_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#         'timed_file_handler':{
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join('logs', 'application.log'),
#             'when': 'S',
#             'interval': 10,
#             'backupCount':10,
#             'formatter': 'simple',
#             'encoding': 'utf-8',
#             'delay': True, #-ローテーション中の書き込みを最後まで待つ処理
#         },
#         'timed_error_handler':{
#             'level': 'ERROR',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join('logs', 'application_error.log'),
#             'when': 'S',
#             'interval': 10,
#             'backupCount':10,
#             'formatter': 'simple',
#             'encoding': 'utf-8',
#             'delay': True, #-ローテーション中の書き込みを最後まで待つ処理
#         },
#         'timed_performance_handler':{
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join('logs', 'application_performance.log'),
#             'when': 'S',
#             'interval': 10,
#             'backupCount':10,
#             'formatter': 'simple',
#             'encoding': 'utf-8',
#             'delay': True, #-ローテーション中の書き込みを最後まで待つ処理
#         },
#     },
#     'loggers': {# ロガーの一覧を記載 }
#         'application-logger': {
#             'handlers':['console_handler','timed_file_handler',],
#             'level': 'DEBUG', #- handlersのlevelよりも低いlevelは出力できないため設定しても無駄
#             'propagate': False,
#         },
#         'error-logger':{
#             'handlers':['timed_error_handler',],
#             'level': 'ERROR', #- handlersのlevelよりも低いlevelは出力できないため設定しても無駄
#             'propagate': False,
#         },
#         'performance-logger':{
#             'handlers':['timed_performance_handler',],
#             'level': 'INFO', #- handlersのlevelよりも低いlevelは出力できないため設定しても無駄
#             'propagate': False,
#         },

#     }
# }