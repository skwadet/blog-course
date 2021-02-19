from django.db import models


class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    user = models.ForeignKey('BlogUser')
    timestamp = models.DateTimeField()
    auto_now = True
