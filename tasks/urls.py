from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', UserTaskListView.as_view()),
    path('tasks/<int:pk>/', UserTaskUpdateView.as_view()),
    path('tasks/<int:pk>/report/', TaskReportView.as_view()),
]
