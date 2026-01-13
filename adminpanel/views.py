from django.shortcuts import render
from accounts.models import User
from tasks.models import Task
from .decorators import admin_required,PermissionDenied
from tasks.forms import TaskCreateForm
from django.shortcuts import redirect

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
    user = request.user

    if user.is_superuser:
        qs = Task.objects.all()

    elif user.role == 'ADMIN':
        qs = Task.objects.filter(assigned_by=user)

    else:
        raise PermissionDenied

    return render(request, 'admin_panel/tasks.html', {'tasks': qs})




@admin_required
def reports(request):
    user = request.user

    if user.is_superuser:
        qs = Task.objects.filter(status='COMPLETED')

    elif user.role == 'ADMIN':
        qs = Task.objects.filter(
            status='COMPLETED',
            assigned_by=user
        )

    else:
        raise PermissionDenied

    return render(request, 'admin_panel/task_reports.html', {
        'tasks': qs
    })



@admin_required
def create_task(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, admin=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_by = request.user
            task.save()
            return redirect('/panel/tasks/')
    else:
        form = TaskCreateForm(admin=request.user)

    return render(request, 'admin_panel/create_task.html', {
        'form': form
    })
