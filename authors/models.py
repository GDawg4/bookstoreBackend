from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    birth_date = models.DateField()
    author_pic = models.ImageField(upload_to="authors/%Y/%m", null = True, blank = True)
    has_account = models.BooleanField(default=False)
    bio = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True)
    account_linked = models.OneToOneField(
        'users.Reader',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return '{}'.format(self.name)