from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/admin/login/')
        if request.user.role not in ['ADMIN', 'SUPERADMIN']:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper
