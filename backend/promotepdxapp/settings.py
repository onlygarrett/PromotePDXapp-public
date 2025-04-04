import os
from pathlib import Path
import environ
import logging.config

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()
LOGGING_CONFIG = None

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "EventCalendar",
    "corsheaders",
    "rest_framework",
    "custom_commands",
    "django_object_actions",
    "UserAccounts",
    "django_celery_beat",
    "django_celery_results",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CSRF_TRUSTED_ORIGINS = ["https://www.promotepdx.com", "https://promotepdx.com"]


CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",  # The default port for create-react-app
]
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "promotepdxapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "promotepdxapp.wsgi.application"

# Database
POSTGRES_USER = env("POSTGRES_USER")
POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")
POSTGRES_DB = env("POSTGRES_DB")
POSTGRES_HOST = env("POSTGRES_HOST")
POSTGRES_PORT = env("POSTGRES_PORT")


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": POSTGRES_DB,
#         "USER": POSTGRES_USER,
#         "PASSWORD": POSTGRES_PASSWORD,
#         "HOST": POSTGRES_HOST,
#         "PORT": POSTGRES_PORT,
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

# Password validation
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
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Google API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/django_static/"
STATIC_ROOT = BASE_DIR / "django_static"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

# Celery Env variables
################################################################
CELERY_BROKER_URL = env("REDIS_URL")

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = env(
    "CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP"
)
CELERY_BEAT_SCHEDULER = env("CELERY_BEAT_SCHEDULER")

# Task Tracking
CELERY_TRACK_STARTED = env("CELERY_TRACK_STARTED")
CELERY_TASK_TIME_LIMIT = int(
    env("CELERY_TASK_TIME_LIMIT", default=1800) or 1800
)  # Provide a default value and handle empty string

# Email env
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_SERVICE_ID = env("EMAIL_SERVICE_ID")
EMAIL_TEMPLATE_ID = env("EMAIL_TEMPLATE_ID")
EMAIL_USER_ID = env("EMAIL_USER_ID")

CREATE_SUPERUSER = env("CREATE_SUPERUSER")

# Logging
################################################################
LOGLEVEL = env("LOGLEVEL", default="INFO").upper()
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s |:| LEVEL: %(levelname)s |:| %(module)s |:| %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            }
        },
        "loggers": {
            "": {
                "level": "WARNING",
                "handlers": ["console"],
            },
            "app": {
                "level": LOGLEVEL,
                "handlers": ["console"],
                "propagate": False,
            },
        },
    }
)
