from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Table(models.Model):

    STATUS = (
        ('male', 'male'),
        ('female', 'female')
    )

    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    level = models.CharField(max_length=5)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, null=True, choices=STATUS)

    def __str__(self):
        return self.full_name



