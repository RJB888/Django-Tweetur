from django.db import models

# Create your models here.


class User(models.Model):
    # id - autogenerate?
    username = models.CharField(max_length=200, blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False)


class Tweet(models.Model):
    # user = FK to username
    date = models.DateTimeField()
    text = models.CharField(max_length=200, blank=False)

# class Follows(models.Model):
#     # User follows user
