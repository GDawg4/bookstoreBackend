from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        'users.Reader',
        null=False,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        'books.Book',
        null=False,
        on_delete=models.CASCADE
    )