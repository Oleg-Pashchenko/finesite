from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.test, name='home'),
    path('finance/', views.test, name='finance'),
    path('tasks/', views.test, name='tasks'),
    path('targets/', views.test, name='targets'),
    path('notes/', views.test, name='notes')
]
