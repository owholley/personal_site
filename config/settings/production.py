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