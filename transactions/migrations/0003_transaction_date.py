# Generated by Django 3.0.6 on 2020-05-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20200524_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]