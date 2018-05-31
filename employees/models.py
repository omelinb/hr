from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser

from django.db import models

import uuid


class Employee(AbstractUser):
    RANKS = (
        ('J', 'Junior'),
        ('M', 'Middle'),
        ('S', 'Senior'),
        ('H', 'Head')
    )
    DEPARTMENTS = (
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('BU', 'BUYING'),
        ('DG', 'DIGITAL')
    )
    rank = models.CharField(max_length=1, choices=RANKS)
    department = models.CharField(max_length=2, choices=DEPARTMENTS)
    phone = models.IntegerField(null=True)
    email = models.EmailField()
    about = models.TextField(blank=True, null=True)

    class Meta():
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def set_temporary_password(self):
        password = str(uuid.uuid4())
        self.set_password(password)
        MESSAGE = """
            Glad to see you in our team!
            Login: {username}
            Password: {password}
        """
        send_mail(
            'Temporary password',
            MESSAGE.format(username=self.username, password=password),
            'HR Department',
            [self.email],
            fail_silently=False)

    def save(self, *args, **kwargs):
        if self.department == 'HR':
            self.is_staff = True
        if self.email and not self.password:
            self.set_temporary_password()
        super().save(*args, **kwargs)
