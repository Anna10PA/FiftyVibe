from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(default='other')
    b_day = models.DateField(default='2009-02-10')
    profile = models.ImageField(upload_to='profile/', default="")
    cover = models.ImageField(upload_to='cover/', default='')
    account_type = models.CharField(default='public')

class Posts(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(default='')
    image = models.JSONField(default=list)
    video = models.JSONField(default=list)
    like = models.JSONField(default=list)
    message = models.CharField(default='')
    share = models.JSONField(default=list)
    post_type = models.CharField(default='Public')