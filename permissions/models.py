from django.db import models

from employees.models import Employee


class Permission(models.Model):
    type = models.CharField(max_length=150)
    date_start = models.DateTimeField('Start Date')
    date_end = models.DateTimeField('End Date')
    employee = models.ForeignKey(
        Employee,
        related_name='permissions',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.type
