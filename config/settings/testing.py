from pickle import TRUE
from .base import *
from .base import env

# General 
# ------------------------------------------------------
SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['www.mainedogco.com', 'mainedogco.com']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"