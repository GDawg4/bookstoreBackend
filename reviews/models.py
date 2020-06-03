from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=500, null=True, blank=True)
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        null=False
    )
    reviewer = models.ForeignKey(
        'users.Reader',
        related_name='reviews_written',
        on_delete=models.SET('NO AUTHOR')
    )
    book = models.ForeignKey(
        'books.Book',
        related_name='reviews_starred',
        on_delete=models.SET('NO BOOK AVAILABLE'),
        default=0
    )