from django.contrib import admin
from .models import User, Posts, PostsFile

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(PostsFile)
