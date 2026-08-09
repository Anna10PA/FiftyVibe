from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(default='other')
    b_day = models.DateField(default='2009-02-10')
    profile = models.ImageField(upload_to='profile/', default="")
    cover = models.ImageField(upload_to='cover/', default='')