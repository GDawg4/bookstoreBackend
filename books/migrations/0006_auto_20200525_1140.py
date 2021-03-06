# Generated by Django 3.0.6 on 2020-05-25 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_auto_20200525_1137'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authors', '0001_initial'),
        ('books', '0005_auto_20200525_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bought_by',
            field=models.ManyToManyField(through='transactions.Transaction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=0, on_delete=models.SET('NO AUTHOR'), related_name='books_written', to='authors.Author'),
        ),
    ]
