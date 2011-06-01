import traceback, os

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = PROJECT_ROOT + '/media/'
TEMPLATE_DIRS = ( PROJECT_ROOT + '/templates/', )
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = ''

ADMIN_MEDIA_PREFIX = '/static/admin/'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

SOUTH_AUTO_FREEZE_APP = True

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'shortbow.urls'

TEMPLATE_DIRS = ( PROJECT_ROOT + '/templates/', )

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'front',
)

from local_settings import *
