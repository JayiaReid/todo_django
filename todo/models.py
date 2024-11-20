from django.db import models

# Create your models here.

class Item(models.Model):
    task = models.CharField(max_length=255, help_text="Title of the task")
    completed = models.BooleanField(default=False, help_text="Mark as completed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)