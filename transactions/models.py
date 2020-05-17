from django.db import models

# Create your models here.
class Transaction(models.Model):
    transaction_id = models.CharField(max_length=16)
    total = models.FloatField()
    buyer = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='purchases',
    )
    books = models.ManyToManyField(
        'books.Book'
    )