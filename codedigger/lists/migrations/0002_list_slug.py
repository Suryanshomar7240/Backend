# Generated by Django 3.1.4 on 2020-12-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='slug',
            field=models.SlugField(default=' ', max_length=20),
        ),
    ]
