# Generated by Django 3.0.4 on 2020-05-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('books', '0013_auto_20200531_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='books', to='tags.Tag'),
        ),
    ]
