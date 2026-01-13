from django import forms
from .models import Task
from accounts.models import User

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']

    def __init__(self, *args, **kwargs):
        admin = kwargs.pop('admin', None)
        super().__init__(*args, **kwargs)

        # Admin can only assign their users
        if admin and admin.role == 'ADMIN':
            self.fields['assigned_to'].queryset = User.objects.filter(
                assigned_admin=admin
            )
