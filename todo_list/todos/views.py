from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos_list = Todo.objects.all()
    # return HttpResponse('Hello World')
    context = {
        'todos': todos_list
    }
    return render(request, 'index.html', context)