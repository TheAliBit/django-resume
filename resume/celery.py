import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume.settings')

celery = Celery('config')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
