# Generated by Django 2.2 on 2019-12-08 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 14, 14, 57, 720676, tzinfo=utc)),
        ),
    ]
