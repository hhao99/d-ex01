from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(req):
    todos = Todo.objects.all()
    return render(req,'todo/index.html',{'todos': todos })

def detail(req,pk):
    todo = get_object_or_404(Todo,pk=pk)
    return render(req,'todo/detail.html',{'todo': todo})

def edit(req,pk):
    return "edit"

def delete(req, pk):
    todo = get_object_or_404(Todo,pk=pk)
    todo.delete()
    return redirect('index')

def new(req):
    if req.method == 'POST':
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
        return render(req, 'todo/edit.html', {'form' : form})