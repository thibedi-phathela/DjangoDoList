# Generated by Django 3.2.19 on 2023-06-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.CharField(default='Not set', max_length=15),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
