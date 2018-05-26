from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    phone = models.IntegerField(null=True)
    rank = models.CharField(max_length=64, blank=True, null=True)
    department = models.CharField(max_length=64, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta():
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def verification(self):
        pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.email:
            self.verification()
