# Generated by Django 3.2.19 on 2023-06-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20230623_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
