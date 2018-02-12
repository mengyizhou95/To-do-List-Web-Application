# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

from todo.models import TodoList


def index(request, **kwargs):
    todo_list = TodoList.objects.all()
    todo_filter = 'all'

    return render(request, 'index.html', locals())


@require_http_methods(['POST'])
@csrf_protect
def add(request, **kwargs):
    action = request.POST.get('action')
    if action == 'add':
        content = request.POST.get('content')
        TodoList.objects.create(content=content)

    return HttpResponse(content='add item success')


@require_http_methods(['GET'])
def delete(request, pk, **kwargs):
    todo_item = get_object_or_404(TodoList, id=pk)
    todo_item.delete()

    return HttpResponse(content='delete {} success'.format(pk))


@require_http_methods(['GET'])
def complete(request, pk, **kwargs):
    todo_item = get_object_or_404(TodoList, id=pk)
    todo_item.is_completed = not todo_item.is_completed
    todo_item.save()

    return HttpResponse(content='toggle {} success'.format(pk))


@require_http_methods(['GET'])
def filter_index(request, pk, **kwargs):
    if pk == 'active':
        todo_list = TodoList.objects.filter(is_completed=False).all()
    elif pk == 'completed':
        todo_list = TodoList.objects.filter(is_completed=True).all()
    todo_filter = pk

    return render(request, 'index.html', locals())
