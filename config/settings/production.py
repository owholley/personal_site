from .base import *
from .base import env

# General 
# -----------------------------------------------------------------

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ['www.owenwholley.com', 'owenwholley.com']

# Deployment Security Settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True