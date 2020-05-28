# Generated by Django 3.0.6 on 2020-05-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0003_book_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=0, on_delete=models.SET('NO AUTHOR'), related_name='books_written', to='authors.Author'),
        ),
    ]
