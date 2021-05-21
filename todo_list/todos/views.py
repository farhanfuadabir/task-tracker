from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def index(request):
    # return HttpResponse('Hello World')
    todos_list = Todo.objects.all()
    context = {
        'todos': todos_list
    }
    return render(request, 'index.html', context)

def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)
