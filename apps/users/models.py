from django.db import models
from django.contrib.auth.models import User


class BlogUser(User):
    birthdate = models.DateField()
    bio = models.TextField()


class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    user = models.ForeignKey('BlogUser')
    timestamp = models.DateTimeField()
    auto_now = True


class Like(models.Model):
    user = models.ForeignKey('BlogUser')
    post = models.ForeignKey('Post')
    timestamp = models.DateTimeField()
