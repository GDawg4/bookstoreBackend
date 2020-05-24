from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=10000, null=False)
    content = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(
        'users.Reader',
        related_name='notes_written',
        null=False,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        'books.Book',
        related_name='notes_taken',
        null=False,
        on_delete=models.CASCADE
    )