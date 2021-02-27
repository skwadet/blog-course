from django.db import models
from apps.users.models import BlogUser
from apps.posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(BlogUser, related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
