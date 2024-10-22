from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','bhashanet_v2.settings')

app = Celery('bhashanet_v2')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS STARTS
app.conf.beat_schedule = {
    'update-registry-list-every-15-days': {
        'task': 'CORE.tasks.test_func',
        'schedule': crontab(day_of_month='1-31/4', hour=9, minute=10)
    }
}
# CELERY BEAT SETTINGS ENDS

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request : {self.request!r}')
    
