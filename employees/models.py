from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    phone = models.IntegerField()
    rank = models.CharField(max_length=64)
    department = models.CharField(max_length=64)

    class Meta():
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
