import os

from celery import Celery
from celery.schedules import crontab
import requests


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')

app = Celery('celery_app')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'


app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test_task() every 30 seconds.
    sender.add_periodic_task(30.0, test_task.s(), name='fetch movies 30')

   


@app.task
def test_task():
    r = requests.get('http://www.omdbapi.com/?s=movie&apikey=a9457c8e')
    data = r.json()
    for m in data:
        print(m)