# Generated by Django 3.0.4 on 2020-06-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0002_auto_20200601_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
