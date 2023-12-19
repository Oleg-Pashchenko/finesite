from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render

from authentification.forms import UserRegisterForm, UserLoginForm

from django.shortcuts import redirect
from functools import wraps


def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Если пользователь аутентифицирован, вызывается оригинальная функция
            return view_func(request, *args, **kwargs)
        else:
            # Если пользователь не аутентифицирован, перенаправляем его на страницу входа
            return redirect('/login/')

    return wrapper


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, f'Account created for {email}!')
            form = UserRegisterForm()  # Creating a new form to clear the previous data
            return redirect('/home')
        else:
            messages.warning(request, "Form submission error!")
    else:
        form = UserRegisterForm()
    return render(request, 'authentification/html/../templates/authentification/register.html', {'form': form})


def login_view(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('/home')
            else:
                messages.warning(request, 'Login failed!')
        else:
            messages.warning(request, 'Invalid form submission!')
    else:
        form = UserLoginForm()
    return render(request, 'authentification/html/../templates/authentification/login.html', {'form': form})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('/login/')
