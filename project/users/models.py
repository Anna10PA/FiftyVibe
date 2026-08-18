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
    like = models.JSONField(default=list)
    comment = models.CharField(default='')
    share = models.JSONField(default=list)
    post_type = models.CharField(default='Public')
    time = models.DateTimeField(auto_now_add=True)


class PostsFile(models.Model):
    files_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    files = models.FileField(upload_to='post/')