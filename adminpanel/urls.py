from django.urls import path
from .views import dashboard, users, admins, tasks, reports

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', users, name='users'),
    path('admins/', admins, name='admins'),
    path('tasks/', tasks, name='tasks'),
    path('reports/', reports, name='reports'),
]
