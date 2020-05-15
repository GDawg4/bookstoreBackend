from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
