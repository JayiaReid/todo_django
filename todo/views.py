from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Item

# Create your views here. (4 7)
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def todo_list(request):
    todos = Item.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Item.objects.create(task=task)
        return redirect('todo_list')
    return render(request, 'add.html')

def complete_todo(request, todo_id):
    todo = Item.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')