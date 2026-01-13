from django.urls import path
from .views import dashboard, users, admins, tasks, reports,create_task

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', users, name='users'),
    path('admins/', admins, name='admins'),
    path('tasks/', tasks, name='tasks'),
    path('reports/', reports, name='reports'),
    path('tasks/create/', create_task, name='create_task'),
]
