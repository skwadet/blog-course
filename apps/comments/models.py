from django.db import models


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey('BlogUser')
    timestamp = models.DateTimeField()
