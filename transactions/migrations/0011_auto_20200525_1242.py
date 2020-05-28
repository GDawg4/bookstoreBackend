# Generated by Django 3.0.6 on 2020-05-25 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0010_transaction_given_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='given_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
