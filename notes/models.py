from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=10000, null=False)
    book = models.ForeignKey(
        'books.Book',
        null=False,
        on_delete=models.CASCADE
    )