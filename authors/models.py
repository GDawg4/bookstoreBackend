from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    birth_date = models.DateField()
    has_account = models.BooleanField(default=False)
    account_linked = models.OneToOneField(
        'users.Reader',
        on_delete=models.SET_NULL,
        null=True
    )