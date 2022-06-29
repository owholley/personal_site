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

# Sets up digital ocean spaces cloud storage
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET')
AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
AWS_STATIC_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'
STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_REGION_NAME = 'nyc3'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static-local')),)

STATIC_ROOT = 'static/'
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

## MEDIA SETTINGS
AWS_MEDIA_LOCATION = 'media'
MEDIA_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_MEDIA_LOCATION)
MEDIA_ROOT = 'media/'