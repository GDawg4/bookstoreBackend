# Generated by Django 3.0.6 on 2020-05-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200524_2353'),
        ('transactions', '0004_transaction_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='book',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='quantity',
        ),
        migrations.AddField(
            model_name='transaction',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
    ]
