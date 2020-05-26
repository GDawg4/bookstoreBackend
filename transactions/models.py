from django.db import models

# Create your models here.


class Transaction(models.Model):
    total = models.FloatField()
    buyer = models.ForeignKey(
        'users.Reader',
        on_delete=models.CASCADE,
        related_name='purchases_made',
    )
    given_to = models.ForeignKey(
        'users.Reader',
        on_delete=models.CASCADE,
        related_name='given_to',
        null=False
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        related_name='purchases_involved'
    )
    date_made = models.DateTimeField(auto_now=True)