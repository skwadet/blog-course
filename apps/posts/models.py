from django.db import models
from aps.users.models import BlogUser

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    user = models.ForeignKey(BlogUser, related_name="post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    auto_now = True
