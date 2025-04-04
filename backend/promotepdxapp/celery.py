from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "promotepdxapp.settings")

app = Celery("promotepdxapp")

# Load settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
