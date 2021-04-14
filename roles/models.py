from django.db import models


class Role(models.Model):
    title_role = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    active = models.BooleanField(True)
    department = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)