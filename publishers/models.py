from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    publisher_pic = models.ImageField(upload_to="publishers/%Y/%m", null=True, blank=True)
