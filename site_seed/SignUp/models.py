from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300, default=None)
    email = models.CharField(max_length=300, default=None)
    password = models.CharField(max_length=300, default=None)
