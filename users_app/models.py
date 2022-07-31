from django.db import models

class users(models.Model):
    name = models.CharField(max_length = 30, null=False,)
    lastname = models.CharField(max_length = 30, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length = 100, null=False)
    date_joined = models.DateField(null=False,)
