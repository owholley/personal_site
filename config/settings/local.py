from .base import *
from .base import env

# General
# ------------------------------------------------------
DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1', '192.168.88.128']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

