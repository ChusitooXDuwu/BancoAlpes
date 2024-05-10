"""
Django settings for BancoAlpes project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_ROOT = os.path.join(BASE_DIR, 'docsClientes')
DOC_URL = '/docsClientes/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m7z871+_bhwr@onex3bv4ps8f4ddwuxyt!s9fk5ey-6x+#5bhy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cliente',
    'documents',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'BancoAlpes.middleware.UseForwardedPortMiddleware',

]

ROOT_URLCONF = 'BancoAlpes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'BancoAlpes', 'templates')],
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

WSGI_APPLICATION = 'BancoAlpes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'monitoring_db',
        'USER': 'chu',
        'PASSWORD': 'chu',
        'HOST': '10.128.0.52',
        'PORT': '',
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
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static', 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


USE_X_FORWARDED_HOST = True
#now with port 8000



# Configurar el encabezado y valor esperado para determinar si la solicitud es segura (HTTP)
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

# Configuración de autenticación
LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SOCIAL_AUTH_TRAILING_SLASH = False  # Eliminar la barra final de las rutas
SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-7ozdnqo6jnj1t00s.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'q9F3TDPUOIYjuB4xMqywSHYYx5oUWZz3'
SOCIAL_AUTH_AUTH0_SECRET = 'NSrEdzQs3KAXh3HYrNIlG1wk92efLHLlw8t9_ddxIoJsxmmrYzsTTGHDWuRzliJX'
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email',
    'role',
]

# settings.py

# Usar el encabezado X-Forwarded-Host para determinar el host original



# Backend de autenticación
AUTHENTICATION_BACKENDS = {
    'BancoAlpes.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
}

