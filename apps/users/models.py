from django.db import models

# Create your models here.
class Bloguser(models.User):
    birthdate = models.DateField()
    bio = models.CharField()