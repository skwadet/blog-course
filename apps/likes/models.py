from django.db import models


class Like(models.Model):
    user = models.ForeignKey('BlogUser')
    post = models.ForeignKey('Post')
    timestamp = models.DateTimeField()
