from django.db import models

# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=10000)
    books = models.ManyToManyField(
        'books.Book'
    )