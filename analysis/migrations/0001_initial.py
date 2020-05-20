# Generated by Django 3.0.4 on 2020-05-17 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_user_last_name'),
        ('books', '0002_book_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_starred', to='books.Book')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='analysis_written', to='users.User')),
            ],
        ),
    ]