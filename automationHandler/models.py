from django.db import models

# Create your models here.
class ScriptConfig(models.Model):
    name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=500)
    description = models.TextField()
    is_scheduled = models.BooleanField(default=False)
    schedule_interval = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_run = models.DateTimeField(null=True)
    enabled = models.BooleanField(default=True)