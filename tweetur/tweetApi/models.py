from django.db import models

# Create your models here.


class User(models.Model):
    # id - autogenerate?
    username = models.CharField(max_length=200, blank=False)  # unique constraint
    password = models.CharField(max_length=200, blank=False)


class Tweet(models.Model):
    # user = FK to username
    # date = auto generate?
    text = models.CharField(max_length=200, blank=False)

# class Follows(models.Model):
#     # User follows user
