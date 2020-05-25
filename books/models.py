from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    bought_by = models.ManyToManyField(
        'users.Reader',
        through='transactions.Transaction',
        through_fields=('book', 'buyer')
    )
    author = models.ForeignKey(
        'authors.Author',
        related_name='books_written',
        default=0,
        on_delete=models.SET(0)
    )
    publisher = models.ForeignKey(
        'publishers.Publisher',
        related_name='books_published',
        on_delete=models.SET(0)
    )
    tags = models.ManyToManyField(
        'tags.Tag',
        related_name='books',
        null = True
    )