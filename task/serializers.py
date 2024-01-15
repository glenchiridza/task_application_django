from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id", "description", "is_reminder_on", "is_task_pending",
            "created_date", "updated_date",
        )


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__',)


class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
