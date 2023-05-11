

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mpnpq0$)rtm+*_3+mal5wujf_4obijibbfxh8((b0xls^tu5zq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #Applications tiers
    #"django_resized ",
    "taggit",
    #Applications
    "app.apps.AppConfig",
    "authuser.apps.AuthuserConfig",
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "coupons.apps.CouponsConfig",
    "payment.apps.PaymentConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lecafe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'cart.context_processors.cart',
                'app.context_processors.category',
            ],
        },
    },
]

WSGI_APPLICATION = "lecafe.wsgi.application"

AUTH_USER_MODEL="authuser.User"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Africa/Douala"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CART_SESSION_ID = 'cart'


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Le Café Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Le Café",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Le Café",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "assets/img/logo.png",
}

#rrppeaysmpzfafpj   PASSWORD

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # ex: smtp.gmail.com
EMAIL_PORT = 587 # ex: 587
EMAIL_USE_TLS = True # ou False si vous n'utilisez pas TLS
EMAIL_HOST_USER = 'menraromial@gmail.com'
EMAIL_HOST_PASSWORD = 'bgwabcnsoxmprcvz'

STRIPE_PUBLISHABLE_KEY='pk_test_51N6VLaI0TlN0GZ9zypE1diZbJwEJuglpIHVKZ53HPLC7aecijz9PqkINr2BbWCyucOgk816zGhZhZM38VwWVoqkK00W1fS3rzQ'
STRIPE_SECRET_KEY='sk_test_51N6VLaI0TlN0GZ9z1XGAdfjt4LDCBq1pZktJBsGEbLCup2z0km95sVLU01AB7vtn2rTzoqQQCk8DJdDF0FMWySg400Uh9z9JeJ'
STRIPE_API_VERSION='2022-08-01'
