# encoding=utf8
from demo.celery import app
from celery import shared_task, current_app


@app.task
def add(x, y):
    return x+y


@shared_task
def commod(host, name):
    return 'commod'


@shared_task
def script(host, name):
    return 'script'


print app.conf.CELERY_BROKER_URL
print app.conf.CELERY_RESULT_BACKEND
for n in current_app.tasks:
    print n
