from django.shortcuts import render, HttpResponse 
from .models import Todo

def index(req):
    todos = Todo.objects.all()
    return render(req,'todo/index.html',{'todos': todos })