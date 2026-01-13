from rest_framework.permissions import BasePermission

class IsAssignedUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user

class IsAdminOrSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['ADMIN', 'SUPERADMIN']
