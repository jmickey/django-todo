from django.shortcuts import render
from .models import TaskItem


def home(request):
    tasks = TaskItem.objects.all()
    return render(request, 'home.html', {'tasks': tasks})
