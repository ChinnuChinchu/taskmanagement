from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAssignedUser, IsAdminOrSuperAdmin

class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

class UserTaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssignedUser]
    queryset = Task.objects.all()

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class TaskReportView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperAdmin]
    queryset = Task.objects.filter(status='COMPLETED')

    def get_object(self):
        task = super().get_object()

        if self.request.user.is_superuser:
            return task

        if task.assigned_by != self.request.user:
            raise PermissionDenied("Not allowed to view this report")

        return task

