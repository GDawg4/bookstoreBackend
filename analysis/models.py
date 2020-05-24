from django.db import models

# Create your models here.
class Analysis(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    book = models.ForeignKey(
        'books.Book',
        related_name='analysis_starred',
        on_delete=models.CASCADE
    )
    writer = models.ForeignKey(
        'users.Reader',
        related_name='analysis_written',
        on_delete=models.SET_NULL,
        null=True
    )
