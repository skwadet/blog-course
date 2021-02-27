from django.db import models
from apps.users.models import BlogUser


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(BlogUser, related_name="comment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
