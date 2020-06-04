# Generated by Django 3.0.4 on 2020-06-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
