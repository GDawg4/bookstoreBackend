from django.db import models


# Create your models here.
class Information(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    book_mentioned = models.ManyToManyField(
        'books.Book',
        related_name='info_mentions'
    )

