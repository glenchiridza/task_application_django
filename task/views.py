from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins

from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer, TaskDeleteSerializer


class TaskListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskUpdateSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'


class TaskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskDeleteSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'
