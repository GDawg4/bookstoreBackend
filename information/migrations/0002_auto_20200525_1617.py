# Generated by Django 3.0.6 on 2020-05-25 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='books_mentioned',
            new_name='book_mentioned',
        ),
    ]
