from django.db import models

# Create your models here.
#Can change
class User(models.Model):
    name = models.CharField(max_length=100)