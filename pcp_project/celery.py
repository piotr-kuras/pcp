from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.apps import apps

from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcp_project.settings')

app = Celery('pcp_project')
app.config_from_object("django.conf:settings", namespace='CELERY')
apps.populate(settings.INSTALLED_APPS)
app.autodiscover_tasks()

app.conf_beat_schedule = {
    "refresh_products_prices": {
        "task": "pcp.tasks.refresh_products_prices",
        "schedule": crontab(minute=0, hour=10),
        # "schedule": crontab(minute="*/1"),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")