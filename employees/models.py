from django.db import models

from roles.models import Role


class Employee(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)
    dni = models.CharField(max_length=150)
    age = models.IntegerField()
    tel = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(
        Role,
        related_name='employees',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name