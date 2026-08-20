from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(default='other')
    b_day = models.DateField(default='2009-02-10')
    profile = models.ImageField(upload_to='profile/', default="")
    cover = models.ImageField(upload_to='cover/', default='')
    account_type = models.CharField(default='public')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Hashtag(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(default='')
    like = models.JSONField(default=list)
    share = models.JSONField(default=list)
    post_type = models.CharField(default='Public')
    time = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name='posts')
    
    def __str__(self):
        return f"{self.user.username}'s Post ({self.id})"


class Comment(models.Model):
    comment = models.CharField(default='')
    user = models.ForeignKey(Posts, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class PostsFile(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='files')
    files = models.FileField(upload_to='post/')
        
    def __str__(self):
        return f"File for post #{self.post.id}"