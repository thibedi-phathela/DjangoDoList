# Generated by Django 3.2.19 on 2023-06-20 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.CharField(default=datetime.date(2023, 6, 20), max_length=20),
        ),
    ]
