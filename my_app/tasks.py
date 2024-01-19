from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task
def sub(x,y):
    sleep(10)
    return x-y

@shared_task
def clear_session_cache(id):
    print(f"session cache cleared:{id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"redis data cleared:{key}")
    return key

@shared_task
def clear_rabbitmq_data(a):
    print(f"rabbitmq data cleared:{a}")
    return a

### create shedule every 30 second

schedule, create = IntervalSchedule.objects.get_or_create(

    every = 30,
    period = IntervalSchedule.SECONDS
)

PeriodicTask.objects.get_or_create(
    name = 'clear rabbitMQ Periodic task',
    task = 'my_app.tasks.clear_rabbitmq_data',
    interval = schedule,
    args = json.dumps(['hello'])
)