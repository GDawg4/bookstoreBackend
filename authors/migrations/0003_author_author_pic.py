# Generated by Django 3.0.4 on 2020-05-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_pic',
            field=models.ImageField(blank=True, null=True, upload_to='authors/%Y/%m'),
        ),
    ]
