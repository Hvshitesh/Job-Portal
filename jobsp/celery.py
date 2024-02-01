from __future__ import absolute_import, unicode_literals
import os
import string
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobsp.settings")

app = Celery("jobsp")
# app1 = callable.__delattr__('slice')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.w
# - namespace='CELERY' means all lery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY_")

# Load task modules from all registered Django app configs.             
app.autodiscover_tasks() 