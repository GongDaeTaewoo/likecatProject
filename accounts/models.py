from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    avatar = models.ImageField()
    age = models.IntegerField()
    univ = models.CharField(max_length=15)
    job = models.CharField(max_length=20)
    gender = models.CharField(max_length=7)
