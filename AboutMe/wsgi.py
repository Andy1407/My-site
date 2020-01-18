import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
os.environ['DJANGO_SETTINGS_MODULE'] = 'AboutMe.settings'

application = get_wsgi_application()
application = WhiteNoise(application)
