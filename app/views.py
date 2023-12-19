from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    return render(request, 'app/home/home.html')


def finance(request: HttpRequest):
    return render(request, 'app/home/home.html')


def tasks(request: HttpRequest):
    return render(request, 'app/home/home.html')


def targets(request: HttpRequest):
    return render(request, 'app/home/home.html')


def notes(request: HttpRequest):
    return render(request, 'app/home/home.html')
