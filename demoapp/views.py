from __future__ import absolute_import, unicode_literals
from django.http import HttpResponse

from proj.celery import app
from .tasks import add

def add_view(request):
    num1 = request.GET.get('n')
    num2 = request.GET.get('m')
    task = add.delay(int(num1), int(num2))
    return HttpResponse('Task created! <a href="/result/?task_id={}">Get result.</a>'.format(task.id))

def get_result(request):
    task_id = request.GET.get('task_id')
    task = app.AsyncResult(task_id)
    if task.ready():
        return HttpResponse(
            'Task {}. Result: {}'.format(task.status, task.result))
    else:
        return HttpResponse('Task: {}'.format(task.status))
