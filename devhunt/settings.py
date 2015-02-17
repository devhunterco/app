"""
Configuraciones de Django para el proyecto devhunt.
"""
from __future__ import unicode_literals
import os

# Extender configuraciones del la app para el foro
from foro.settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'devhunt.urls'

WSGI_APPLICATION = 'devhunt.wsgi.application'

# Zona horaia destino

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

INSTALLED_APPS += (
    'landing',
    'django_gravatar',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Configuraciones para trabajar en local y en produccion

# Incluir configuracon local de ejemplo
# Descargar -> https://gist.github.com/5a6fa6eebb997a709040.git
# o hacer su propia configuracion local.

try:
    from .local_settings import *
except ImportError:
    pass

# Para servidor de produccion

try:
    from .production_settings import *
except ImportError:
    pass
