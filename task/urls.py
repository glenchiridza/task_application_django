from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = "task"

urlpatterns = [
    path('create-task', TaskCreateView.as_view(), name='create-task'),
    path('list-task', TaskListView.as_view(), name='list-task'),
    path('update/<int:id>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete/<int:id>/', TaskDeleteView.as_view(), name='delete-task'),
]
