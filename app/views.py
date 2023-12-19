from django.http import HttpRequest
from django.shortcuts import render

from app.models import Task


def home(request: HttpRequest):
    return render(request, 'app/home/home.html')


def finance(request: HttpRequest):
    return render(request, 'app/home/home.html')


def tasks(request: HttpRequest):
    return render(request, 'app/home/home.html', {'tasks': Task.objects.all().filter(user_id=request.user)})


def targets(request: HttpRequest):
    return render(request, 'app/home/home.html')


def notes(request: HttpRequest):
    return render(request, 'app/home/home.html')


def add_transaction(request: HttpRequest):
    return render(request, 'app/home/home.html')


def add_note(request: HttpRequest):
    return render(request, 'app/home/home.html')


def view_note(request: HttpRequest):
    return render(request, 'app/home/home.html')


def add_target(request: HttpRequest):
    return render(request, 'app/home/home.html')


def view_target(request: HttpRequest):
    return render(request, 'app/home/home.html')


def add_task(request: HttpRequest):
    return render(request, 'app/home/home.html')


def view_task(request: HttpRequest):
    return render(request, 'app/home/home.html')
