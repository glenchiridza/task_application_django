from django.db import models


class Task(models.Model):
    description = models.TextField(unique=True)
    is_reminder_on = models.BooleanField(default=False)
    is_task_pending = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
