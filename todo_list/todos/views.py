from django.shortcuts import render, redirect
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

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo_time = request.POST['todo_time']

        todo = Todo(title=title, text=text, todo_time=todo_time)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')
