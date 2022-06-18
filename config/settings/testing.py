from pickle import TRUE
from .base import *
from .base import env

# General 
# ------------------------------------------------------
SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['www.mainedogco.com', 'mainedogco.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True