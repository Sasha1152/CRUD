import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.forms import ModelForm
from . models import Task


# Create your views here.

def get_all_tasks(request):
    tasks_all = Task.objects.all()
    data = (', ').join([i.title for i in tasks_all])
    return HttpResponse(data)

def get_todo_tasks(request):
    tasks_todo = Task.objects.filter(status='todo')
    data = serializers.serialize('json', tasks_todo)
    return HttpResponse(data)

def get_inprogress_tasks(request):
    tasks_inprogress = Task.objects.filter(status='inprogress')
    data = serializers.serialize('json', tasks_inprogress)
    return HttpResponse(data)

def get_done_tasks(request):
    tasks_done = Task.objects.filter(status='done')
    data = serializers.serialize('json', tasks_done)
    return HttpResponse(data)

def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_task = Task.objects.create(**data)
        # new_task.save()
        return HttpResponse('"POST" method activated! Created new task where id=%d.' % new_task.id)

    elif request.method == 'GET':
        return HttpResponse('"GET" method activated!')


def delete_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            task = Task.objects.get(id=data['id'])
            task.delete()
            return HttpResponse('"POST" method activated! Deleted task where id=%d.' % data['id'])
        except Task.DoesNotExist:
            return HttpResponse('Sorry, but task where id=%d does not exist' % data['id'])

    elif request.method == 'GET':
        return HttpResponse('"GET" method activated!')

def show_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            task = Task.objects.get(id=data['id'])
            return HttpResponse(f'"POST" method activated! You chose task #{task.id}:"{task.title}"')
        except Task.DoesNotExist:
            return HttpResponse('Sorry, but task where id=%d does not exist' % data['id'])

    elif request.method == 'GET':
        return HttpResponse('"GET" method activated!')

def update_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            task = Task.objects.get(id=data['id'])
            for key in data.keys():
                if key in task.__dict__.keys():
                    task.__dict__[key] = data[key]
            task.save()
            return HttpResponse(task.__dict__.items())
        except Task.DoesNotExist:
            return HttpResponse('Sorry, but task where id=%d does not exist' % data['id'])

    elif request.method == 'GET':
        return HttpResponse('"GET" method activated!')
