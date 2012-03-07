import os
import sys

sys.path.append('/var/opt/voters_counter')

os.environ['DJANGO_SETTINGS_MODULE'] = 'voters_counter_project.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

