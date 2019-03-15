# Create your tasks here
from __future__ import absolute_import, unicode_literals
from time import sleep
from celery import shared_task


@shared_task
def add(x, y):
    sleep(10)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
