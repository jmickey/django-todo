from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TaskItem
from .forms import NewTaskForm


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
