from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.db import models
from django.db.models import Sum



def task_list(request):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    tasks_by_day = []

    for day in days_of_week:
        tasks_for_day = Task.objects.filter(day_of_week=day).order_by('start_time')
        tasks_by_day.append((day, tasks_for_day))

    total_time = Task.objects.aggregate(total=models.Sum('duration_minutes'))['total'] or 0
    remaining_time = (7 * 24 * 60) - total_time

    context = {
        'tasks_by_day': tasks_by_day,  # список кортежей: [('Monday', [задачи]), ...]
        'total_time': total_time,
        'remaining_time': remaining_time,
    }
    return render(request, 'task_list.html', context)



def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})