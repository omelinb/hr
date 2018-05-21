from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    rank = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
