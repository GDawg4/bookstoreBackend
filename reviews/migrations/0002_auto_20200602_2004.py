# Generated by Django 3.0.4 on 2020-06-03 02:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
