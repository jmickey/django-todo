from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TaskItem
from .forms import NewTaskForm, TaskActionForm


def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NewTaskForm()
    tasks = TaskItem.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def complete_task(request):
    if request.method == 'POST':
        form = TaskActionForm(request.POST)
        if form.is_valid():
            task = TaskItem.objects.get(id=form.cleaned_data.get('id'))
            task.is_completed = True
            task.save()
    return HttpResponseRedirect('/')


def delete_task(request):
    if request.method == 'POST':
        form = TaskActionForm(request.POST)
        if form.is_valid():
            TaskItem.objects.get(id=form.cleaned_data.get('id')).delete()
    return HttpResponseRedirect('/')
