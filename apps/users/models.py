from django.db import models
from django.contrib.auth.models import User


class BlogUser(User):
    birthdate = models.DateField()
    bio = models.TextField()
