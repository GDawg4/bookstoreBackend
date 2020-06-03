from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(
        max_length=200,
        null=False
    )
    reviewer = models.ForeignKey(
        'users.Reader',
        related_name='reviews_written',
        on_delete=models.SET(0),
        null=False
    )
    book = models.ForeignKey(
        'books.Book',
        related_name='reviews_starred',
        on_delete=models.SET('NO BOOK AVAILABLE'),
        default=0,
        null=False
    )
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        null=False
    )