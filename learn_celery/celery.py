import os

from celery import Celery
from time import sleep
from datetime import timedelta
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_celery.settings')

app = Celery('learn_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task()
def add(x, y):
    sleep(20)
    return x+y

app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'my_app.tasks.clear_session_cache',
        'schedule': timedelta(seconds=15),
        'args': ('1111',),
    },
#     # Add more periodic tasks as needed
}