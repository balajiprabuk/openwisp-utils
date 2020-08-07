import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '@s8$swhj9du^aglt5+@ut^)wepr+un1m7r*+ixcq(-5i^st=y^'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openwisp_utils.admin_theme',
    'django.contrib.sites',
    # test project
    'test_project',
    # admin
    'django.contrib.admin',
    # rest framework
    'rest_framework',
    'drf_yasg',
]

EXTENDED_APPS = ['django_netjsonconfig']  # Just for testing purposes

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'openwisp_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'openwisp_utils.loaders.DependencyLoader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'openwisp_utils.admin_theme.context_processor.menu_items',
                'openwisp_utils.admin_theme.context_processor.admin_theme_settings',
            ],
        },
    },
]

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'openwisp_utils.db',}
}

OPENWISP_ADMIN_SITE_CLASS = 'test_project.site.CustomAdminSite'

SITE_ID = 1
EMAIL_PORT = '1025'
LOGIN_REDIRECT_URL = 'admin:index'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

# during development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# only for automated test purposes
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'test_project.test_api.throttling.CustomScopedRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {'anon': '20/hour'},
}

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from local_settings import *
except ImportError:
    pass
