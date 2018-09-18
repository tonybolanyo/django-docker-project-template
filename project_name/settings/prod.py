import os
from .base import *


DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

ADMINS = (
    (os.environ.get('ADMIN_EMAIL_NAME', ''),
     os.environ.get('ADMIN_EMAIL_ADDRESS', '')),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', 5432)
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATIC_ROOT', "static/"))
STATIC_URL = os.environ.get('STATIC_URL', STATIC_URL)

MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get('MEDIA_ROOT', "media/"))
MEDIA_URL = os.environ.get('MEDIA_URL', "/media/")

# For HTTPS use
# Force redirection from HTTP to HTTPS, I'm sure you're doing this on NGINX
#SECURE_SSL_REDIRECT = True
# Encrypt session cookie (sends only with HTTPS)
#SESSION_COOKIE_SECURE = True
# Encrypt CSRF cookie (sends only with HTTPS)
#CSRF_COOKIE_SECURE = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
