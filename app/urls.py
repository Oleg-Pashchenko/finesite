from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('finance/', views.finance, name='finance'),
    path('tasks/', views.tasks, name='tasks'),
    path('targets/', views.targets, name='targets'),
    path('notes/', views.notes, name='notes'),

    path('add-transaction/', views.add_transaction, name='add_transaction'),

    path('add-note/', views.add_note, name='add_note'),
    path('view-note/<int:note_id>', views.view_note, name='add_note'),

    path('add-target/', views.add_target, name='add_target'),
    path('view-target/<int:target_id>', views.view_target, name='view_target'),

    path('add-task/', views.add_task, name='add_task'),
    path('view-tasks/<int:task_id>', views.view_task, name='view_task'),


]
