import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BiaBegard.settings')

app = Celery('BiaBegard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
