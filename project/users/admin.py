from django.contrib import admin
from .models import User, Posts, PostsFile, Hashtag, Comment

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(PostsFile)
admin.site.register(Hashtag)
admin.site.register(Comment)