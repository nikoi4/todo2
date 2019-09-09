# from django.shortcuts import render
from django.views.generic import ListView
from .models import Tasks


# Create your views here.
class TasksList(ListView):
    model = Tasks
