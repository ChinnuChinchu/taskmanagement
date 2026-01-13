from django.shortcuts import render
from accounts.models import User
from tasks.models import Task
from .decorators import admin_required

@admin_required
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html', {
        'total': Task.objects.count(),
        'completed': Task.objects.filter(status='COMPLETED').count(),
        'pending': Task.objects.filter(status='PENDING').count(),
    })

@admin_required
def users(request):
    return render(request, 'admin_panel/users.html', {
        'users': User.objects.filter(role='USER')
    })

@admin_required
def admins(request):
    return render(request, 'admin_panel/admins.html', {
        'admins': User.objects.filter(role='ADMIN')
    })

@admin_required
def tasks(request):
    qs = Task.objects.all()
    if request.user.role == 'ADMIN':
        qs = qs.filter(assigned_to__assigned_admin=request.user)
    return render(request, 'admin_panel/tasks.html', {'tasks': qs})

@admin_required
def reports(request):
    qs = Task.objects.filter(status='COMPLETED')
    if request.user.role == 'ADMIN':
        qs = qs.filter(assigned_to__assigned_admin=request.user)
    return render(request, 'admin_panel/task_reports.html', {'tasks': qs})
