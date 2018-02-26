from django.db import models


class TaskItem(models.Model):
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
