from django.db import models


class User(models.Model):
    """
    Modle class to keep user related data, we keep minimum no of fields here.
        1. username
        2. password
        3. auth_token
    """
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)
