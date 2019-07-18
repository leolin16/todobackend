from todobackend.settings.base import *
# from base import *
import os

if os.environ.get('DEBUG'):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

# INSTALLED_APPS += ('django_nose', )
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')
# NOSE_ARGS = [
#     '--verbosity=2',
#     '--nologcapture',
#     '--with-coverage',
#     '--cover-package=todo',
#     '--with-spec',
#     '--spec-color',
#     '--with-xunit',
#     '--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
#     '--cover-xml',
#     '--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR,
# ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
        'USER': os.environ.get('MYSQL_USER', 'todo1'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
        'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
    }
}

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/todobackend/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/www/todobackend/media')