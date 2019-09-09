# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import Tasks


# Create your views here.
class TasksList(ListView):
    model = Tasks


class TasksCreate(CreateView):
    model = Tasks
    fields = [
        'name',
        'priority',
        'event_id',
        'user',
    ]
    success_url = reverse_lazy('tasks-list')