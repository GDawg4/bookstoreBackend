from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    pub_date = models.DateField()
    author = models.ForeignKey(
        'authors.Author',
        related_name='books_written',
        default='Anon',
        on_delete=models.SET('NO AUTHOR')
    )
    publisher = models.ForeignKey(
        'publishers.Publisher',
        related_name='books_published',
        on_delete=models.SET('NO PUBLISHER')
    )
    tags = models.ForeignKey(
        'tags.Tag',
        related_name='tags_marked',
        on_delete=models.SET_NULL
    )